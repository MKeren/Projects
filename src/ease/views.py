import io
import PyPDF2
import docx
import openpyxl
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ease.forms import TranscriptUploadForm
from ease.models import Course, NewCatalog,OldCatalog, Transcript
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login_page.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login_page.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def Home(request):
    return render(request, 'home.html')

@login_required
def StudentTranscriptView(request):
    transcripts = Transcript.objects.all()  
    return render(request, 'transcript.html',{'transcripts': transcripts})

@login_required
def Course_catalog(request):
    return render(request, 'course_catalog.html')

@login_required
def old_catalog(request):
    old_courses = OldCatalog.objects.all()
    return render(request, 'old_catalog.html',{'old_courses': old_courses})

@login_required
def new_catalog(request):
    new_courses = NewCatalog.objects.all()
    return render(request, 'new_catalog.html', {'new_courses': new_courses})

@login_required
def upload_transcript(request):
    if request.method == 'POST':
        form = TranscriptUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']

            if file.name.endswith('.csv'):
                df = process_csv(file)
            elif file.name.endswith('.xlsx') or file.name.endswith('.xls'):
                df = process_excel(file)
            elif file.name.endswith('.pdf'):
                df = process_pdf(file)
            elif file.name.endswith('.docx') or file.name.endswith('.doc'):
                df = process_docx(file)
            elif file.name.endswith('.txt'):
                df = process_txt(file)
            else:
                return render(request, 'upload_transcript.html', {
                    'form': form,
                    'error': 'Unsupported file format.'        
                })
                
            # Filter and clean the DataFrame based on the course catalog

            course_codes = set(Course.objects.values_list('course_code', flat=True))
            df = df[df['Code'].isin(course_codes)]
                

            # Ensure the DataFrame has the correct columns
            columns = ['Code', 'Title of Course', 'ECTS Credits', 'Grade', 'Credits', 'Gr.Pts']
            df = df.reindex(columns=columns)

            # remove any extra columns
            df = df[columns]
        
            # Update the grades in the Course model      
            for index, row in df.iterrows():
                    code = row['Code']
                    grades = row['Grade']    
                
                    course, created = Course.objects.get_or_create(course_code=code)
                    print(f"Updating course {course.course_code} with grade {grades}")
                    course.grade = grades
                    course.save()

                    transcript, created = Transcript.objects.update_or_create(code=code)
                    transcript.grades = grades
                    transcript.save()    
            
            return redirect('course_catalog')
        return df
        
    else:
        form = TranscriptUploadForm()
    return render(request, 'upload_transcript.html', {'form': form})

def process_csv(file: io.BufferedReader) -> pd.DataFrame:
    df = pd.read_csv(file)
    return df

def process_excel(file: io.BufferedReader) -> pd.DataFrame:
    wb = openpyxl.load_workbook(file)
    sheet = wb.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(list(row))
    df = pd.DataFrame(data[1:], columns=data[0])
    
    return df

def process_pdf(file: io.BufferedReader) -> pd.DataFrame:
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return process_text_data(text)

def process_docx(file: io.BufferedReader) -> pd.DataFrame:
    doc = docx.Document(file)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return process_text_data(text)

def process_txt(file: io.BufferedReader) -> pd.DataFrame:
    text = file.read().decode('utf-8')
    return process_text_data(text)

def process_text_data(text: str) -> pd.DataFrame:
    data = {
        'Code': [],
        'Title of Course': [],
        'ECTS Credits': [],
        'Grade': [],
        'Credits': [],
        'Gr.Pts': []
    }
    
    lines = text.split('\n')
    columns = ['Code', 'Title of Course', 'ECTS Credits', 'Grade', 'Credits', 'Gr.Pts']
    header_found = False

    for line in lines:
        if not header_found:
            if all(col in line for col in columns):
                header_found = True
            continue
        
        if header_found:
            fields = line.split()
            if len(fields) >= 6:
                data['Code'].append(fields[-5])
                data['Title of Course'].append(' '.join(fields[1:-4]))
                data['ECTS Credits'].append(fields[-3])
                data['Grade'].append(fields[-4])
                data['Credits'].append(fields[-2])
                data['Gr.Pts'].append(fields[-1])          
    
    df = pd.DataFrame(data)
    print("Processed DataFrame from text data:", df)
    return df
