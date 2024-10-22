from gettext import translation
import io
import re
from venv import logger
import PyPDF2
import fitz
from django.http import HttpResponse
import docx
import pandas as pd
from django.utils import translation
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#from AcademEase import settings
from ease.forms import  DynamicAreaElectiveCourseForm, TranscriptUploadForm
from ease.models import AI_Catalog, Architecture_and_Fine_Arts_Course, AreaElectiveCourse_AI_Catalog, AreaElectiveCourse_ARCHI_NewCatalog, AreaElectiveCourse_ARCHI_OldCatalog, AreaElectiveCourse_BA_NewCatalog, AreaElectiveCourse_BA_OldCatalog, AreaElectiveCourse_BAM_Catalog, AreaElectiveCourse_BE_Catalog, AreaElectiveCourse_BFA_NewCatalog, AreaElectiveCourse_BFA_OldCatalog, AreaElectiveCourse_Civil_Newcatalog,AreaElectiveCourse_Computer_Newcatalog, AreaElectiveCourse_Computer_OldCatalog, AreaElectiveCourse_ECO_Catalog, AreaElectiveCourse_EE_Newcatalog, AreaElectiveCourse_EE_OldCatalog, AreaElectiveCourse_ELT_MidleCatalog, AreaElectiveCourse_ELT_NewCatalog, AreaElectiveCourse_ELT_OldCtalog, AreaElectiveCourse_GPC_MidleCatalog, AreaElectiveCourse_GPC_NewCatalog, AreaElectiveCourse_GPC_OldCtalog, AreaElectiveCourse_IFB_NewCatalog, AreaElectiveCourse_IFB_OldCatalog, AreaElectiveCourse_INTLAW_NewCatalog, AreaElectiveCourse_INTLAW_OldCatalog, AreaElectiveCourse_ITB_NewCatalog, AreaElectiveCourse_ITB_OldCatalog, AreaElectiveCourse_IntArch_NewCatalog, AreaElectiveCourse_IntArch_OldCatalog, AreaElectiveCourse_LAW_NewCatalog, AreaElectiveCourse_LAW_OldCatalog, AreaElectiveCourse_MDM_Catalog, AreaElectiveCourse_MIS_NewCatalog, AreaElectiveCourse_MIS_OldCatalog, AreaElectiveCourse_Nursing_Catalog, AreaElectiveCourse_Nutrition_Catalog, AreaElectiveCourse_PE_MidleCatalog, AreaElectiveCourse_PE_NewCatalog, AreaElectiveCourse_PE_OldCtalog, AreaElectiveCourse_PFCP_Curriculum, AreaElectiveCourse_PSIR_NewCatalog, AreaElectiveCourse_PSIR_OldCatalog, AreaElectiveCourse_PSYE_NewCatalog, AreaElectiveCourse_PSYE_OldCatalog, AreaElectiveCourse_PSYT_NewCatalog, AreaElectiveCourse_PSYT_OldCatalog, AreaElectiveCourse_PharmacyEM_Catalog, AreaElectiveCourse_PharmacyEP_Catalog, AreaElectiveCourse_PharmacyT_Catalog, AreaElectiveCourse_SET_NewCatalog, AreaElectiveCourse_SET_OldCatalog, AreaElectiveCourse_Software_Newcatalog, AreaElectiveCourse_Software_Oldcatalog, AreaElectiveCourse_TLT_MidleCatalog, AreaElectiveCourse_TLT_NewCatalog, AreaElectiveCourse_TLT_OldCtalog, AreaElectiveCourse_civil_OldCatalog, AreaElectiveCourse_dentistryE_Catalog, AreaElectiveCourse_dentistryT_Catalog, AreaElectiveCourse_physio_TNewCatalog, AreaElectiveCourse_physio_TOldCatalog, AreaElectiveCourse_physio_engl_Catalog, AreaTechnicalCourse_AI_Catalog, AreaTechnicalCourse_ARCHI_NewCatalog, AreaTechnicalCourse_ARCHI_OldCatalog, AreaTechnicalCourse_BA_NewCatalog, AreaTechnicalCourse_BA_OldCatalog, AreaTechnicalCourse_BAM_Catalog, AreaTechnicalCourse_BE_Catalog, AreaTechnicalCourse_BFA_NewCatalog, AreaTechnicalCourse_BFA_OldCatalog, AreaTechnicalCourse_Civil_Newcatalog, AreaTechnicalCourse_Computer_Newcatalog, AreaTechnicalCourse_Computer_OldCatalog, AreaTechnicalCourse_ECO_Catalog, AreaTechnicalCourse_EE_Newcatalog, AreaTechnicalCourse_EE_OldCatalog, AreaTechnicalCourse_ELT_MidleCatalog, AreaTechnicalCourse_ELT_NewCatalog, AreaTechnicalCourse_ELT_OldCtalog, AreaTechnicalCourse_GPC_MidleCatalog, AreaTechnicalCourse_GPC_NewCatalog, AreaTechnicalCourse_GPC_OldCtalog, AreaTechnicalCourse_IFB_NewCatalog, AreaTechnicalCourse_IFB_OldCatalog, AreaTechnicalCourse_INTLAW_NewCatalog, AreaTechnicalCourse_INTLAW_OldCatalog, AreaTechnicalCourse_ITB_NewCatalog, AreaTechnicalCourse_ITB_OldCatalog, AreaTechnicalCourse_IntArch_NewCatalog, AreaTechnicalCourse_IntArch_OldCatalog, AreaTechnicalCourse_LAW_NewCatalog, AreaTechnicalCourse_LAW_OldCatalog, AreaTechnicalCourse_MDM_Catalog, AreaTechnicalCourse_MIS_NewCatalog, AreaTechnicalCourse_MIS_OldCatalog, AreaTechnicalCourse_Nursing_Catalog, AreaTechnicalCourse_Nutrition_Catalog, AreaTechnicalCourse_PE_MidleCatalog, AreaTechnicalCourse_PE_NewCatalog, AreaTechnicalCourse_PE_OldCtalog, AreaTechnicalCourse_PFCP_Curriculum, AreaTechnicalCourse_PSIR_NewCatalog, AreaTechnicalCourse_PSIR_OldCatalog, AreaTechnicalCourse_PSYE_NewCatalog, AreaTechnicalCourse_PSYE_OldCatalog, AreaTechnicalCourse_PSYT_NewCatalog, AreaTechnicalCourse_PSYT_OldCatalog, AreaTechnicalCourse_PharmacyEM_Catalog, AreaTechnicalCourse_PharmacyEP_Catalog, AreaTechnicalCourse_PharmacyT_Catalog, AreaTechnicalCourse_SET_NewCatalog, AreaTechnicalCourse_SET_OldCatalog, AreaTechnicalCourse_Software_Newcatalog, AreaTechnicalCourse_Software_Oldcatalog, AreaTechnicalCourse_TLT_MidleCatalog, AreaTechnicalCourse_TLT_NewCatalog, AreaTechnicalCourse_TLT_OldCtalog, AreaTechnicalCourse_civil_OldCatalog, AreaTechnicalCourse_dentistryE_Catalog, AreaTechnicalCourse_dentistryT_Catalog, AreaTechnicalCourse_physio_TNewCatalog, AreaTechnicalCourse_physio_TOldCatalog, AreaTechnicalCourse_physio_engl_Catalog, Arts_and_Sciences_Course, BA_New_catalog, BA_Old_catalog, BAM_catalog, BE_catalog, BFA_New_catalog, BFA_Old_catalog, Civil_Newcatalog, Dent_English_catalog, Dent_Turkish_catalog, EE_Newcatalog, EE_OldCatalog, Econo_catalog, Economics_and_Administrative_Sciences_Course, Edu_ELT2018_catalog, Edu_ELT2021_catalog, Edu_ELT_catalog, Edu_GPC2018_catalog, Edu_GPC2021_catalog, Edu_GPC_catalog, Edu_PE2018_catalog, Edu_PE2021_catalog, Edu_PE_catalog, Edu_PFCP_catalog, Edu_SET2018_catalog, Edu_SET2021_catalog, Edu_TLT2018_catalog, Edu_TLT2021_catalog, Edu_TLT_catalog, Educational_Sciences_Course, Engineering_Course, Computer_Newcatalog,Computer_OldCatalog, Faculty, Health_Sciences_Course, IFB_New_catalog, IFB_Old_catalog, ITB_New_catalog, ITB_Old_catalog, Int_Law_New_catalog, Int_Law_Old_catalog, Law_Course, Law_New_catalog, Law_Old_catalog, MIS_New_catalog, MIS_Old_catalog, MarkDigM_catalog, PSIR_New_catalog, PSIR_Old_catalog,Phamarcy_Course,Dentistry_Course, Pharmay_English_Mpharm_catalog, Pharmay_English_PharmD_catalog, Pharmay_Turkish_English_PharmD_catalog, Pharmay_Turkish_catalog, Psychologyy_Turkish_New_catalog, Psychologyy_Turkish_Old_catalog, Psycholoy_English_New_catalog, Psycholoy_English_Old_catalog, Software_Newcatalog, Software_Oldcatalog,Transcript, archi_New_catalog, archi_Old_catalog, civil_OldCatalog, interior_New_catalog, interior_Old_catalog, nursing_catalog, nutrition_catalog, physiotherapy_engl_catalog, physiotherapy_turk_new_catalog, physiotherapy_turk_old_catalog
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.utils.translation import gettext as _
from django.utils.translation import activate
from typing import Type
from django.db.models import Model

LANGUAGE_SESSION_KEY = 'django_language' 

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
    Engineering_Course.objects.all().update(grade=None)
    Phamarcy_Course.objects.all().update(grade=None)
    Educational_Sciences_Course.objects.all().update(grade=None)
    Law_Course.objects.all().update(grade=None)
    Health_Sciences_Course.objects.all().update(grade=None)
    Architecture_and_Fine_Arts_Course.objects.all().update(grade=None)
    Arts_and_Sciences_Course.objects.all().update(grade=None)
    Economics_and_Administrative_Sciences_Course.objects.all().update(grade=None)
    Dentistry_Course.objects.all().update(grade=None)

    #########################################################################

    AreaElectiveCourse_Computer_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_Computer_Newcatalog.objects.all().update(grade=None)
    AreaElectiveCourse_Civil_Newcatalog.objects.all().update(grade=None)
    AreaElectiveCourse_civil_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_EE_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_EE_Newcatalog.objects.all().update(grade=None)
    AreaElectiveCourse_AI_Catalog.objects.all().update(grade=None)
    AreaElectiveCourse_Software_Newcatalog.objects.all().update(grade=None)
    AreaElectiveCourse_Software_Oldcatalog.objects.all().update(grade=None)
    AreaElectiveCourse_dentistryE_Catalog.objects.all().update(grade=None)
    AreaElectiveCourse_dentistryT_Catalog.objects.all().update(grade=None)
    AreaElectiveCourse_PharmacyEP_Catalog.objects.all().update(grade=None)
    AreaElectiveCourse_PharmacyEM_Catalog.objects.all().update(grade=None)
    AreaElectiveCourse_PharmacyT_Catalog.objects.all().update(grade=None)
    AreaElectiveCourse_ELT_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_ELT_MidleCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_ELT_OldCtalog.objects.all().update(grade=None)
    AreaElectiveCourse_PE_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_PE_MidleCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_PE_OldCtalog.objects.all().update(grade=None)
    AreaElectiveCourse_SET_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_SET_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_GPC_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_GPC_MidleCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_GPC_OldCtalog.objects.all().update(grade=None)
    AreaElectiveCourse_TLT_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_TLT_MidleCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_TLT_OldCtalog.objects.all().update(grade=None)
    AreaElectiveCourse_PFCP_Curriculum.objects.all().update(grade=None)
    AreaElectiveCourse_PSYE_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_PSYE_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_PSYT_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_PSYT_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_LAW_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_LAW_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_INTLAW_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_INTLAW_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_BA_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_BA_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_BE_Catalog.objects.all().update(grade=None)
    AreaElectiveCourse_BAM_Catalog.objects.all().update(grade=None)
    AreaElectiveCourse_BFA_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_BFA_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_MDM_Catalog.objects.all().update(grade=None)
    AreaElectiveCourse_ECO_Catalog.objects.all().update(grade=None)
    AreaElectiveCourse_PSIR_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_PSIR_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_IFB_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_IFB_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_ITB_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_ITB_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_MIS_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_MIS_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_IntArch_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_IntArch_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_ARCHI_NewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_ARCHI_OldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_Nutrition_Catalog.objects.all().update(grade=None)
    AreaElectiveCourse_physio_engl_Catalog.objects.all().update(grade=None)
    AreaElectiveCourse_physio_TNewCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_physio_TOldCatalog.objects.all().update(grade=None)
    AreaElectiveCourse_Nursing_Catalog.objects.all().update(grade=None)

    #########################################################################

    AreaTechnicalCourse_Computer_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_Computer_Newcatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_Civil_Newcatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_civil_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_EE_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_EE_Newcatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_AI_Catalog.objects.all().update(grade=None)
    AreaTechnicalCourse_Software_Newcatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_Software_Oldcatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_dentistryE_Catalog.objects.all().update(grade=None)
    AreaTechnicalCourse_dentistryT_Catalog.objects.all().update(grade=None)
    AreaTechnicalCourse_PharmacyEP_Catalog.objects.all().update(grade=None)
    AreaTechnicalCourse_PharmacyEM_Catalog.objects.all().update(grade=None)
    AreaTechnicalCourse_PharmacyT_Catalog.objects.all().update(grade=None)
    AreaTechnicalCourse_ELT_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_ELT_MidleCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_ELT_OldCtalog.objects.all().update(grade=None)
    AreaTechnicalCourse_PE_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_PE_MidleCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_PE_OldCtalog.objects.all().update(grade=None)
    AreaTechnicalCourse_SET_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_SET_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_GPC_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_GPC_MidleCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_GPC_OldCtalog.objects.all().update(grade=None)
    AreaTechnicalCourse_TLT_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_TLT_MidleCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_TLT_OldCtalog.objects.all().update(grade=None)
    AreaTechnicalCourse_PFCP_Curriculum.objects.all().update(grade=None)
    AreaTechnicalCourse_PSYE_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_PSYE_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_PSYT_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_PSYT_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_LAW_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_LAW_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_INTLAW_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_INTLAW_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_BA_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_BA_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_BE_Catalog.objects.all().update(grade=None)
    AreaTechnicalCourse_BAM_Catalog.objects.all().update(grade=None)
    AreaTechnicalCourse_BFA_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_BFA_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_MDM_Catalog.objects.all().update(grade=None)
    AreaTechnicalCourse_ECO_Catalog.objects.all().update(grade=None)
    AreaTechnicalCourse_PSIR_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_PSIR_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_IFB_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_IFB_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_ITB_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_ITB_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_MIS_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_MIS_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_IntArch_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_IntArch_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_ARCHI_NewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_ARCHI_OldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_Nutrition_Catalog.objects.all().update(grade=None)
    AreaTechnicalCourse_physio_engl_Catalog.objects.all().update(grade=None)
    AreaTechnicalCourse_physio_TNewCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_physio_TOldCatalog.objects.all().update(grade=None)
    AreaTechnicalCourse_Nursing_Catalog.objects.all().update(grade=None)

    Transcript.objects.all().delete()
    

    logout(request)
    return redirect('login')

@login_required
def Home(request):
    return render(request, 'home.html')

#def switch_language(request):
    print(request.GET) 
    lang = request.GET.get('lang','')
    next_url = request.GET.get('next','/')
    activate(lang)
    response = redirect(next_url)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    return response

def switch_language(request):
    if request.method == 'POST':
        #lang_code = request.POST.get('language', settings.LANGUAGE_CODE)
        #if lang_code in dict(settings.LANGUAGES):  # Ensure it's a valid language code
            #translation.activate(lang_code)
            #request.session[translation.LANGUAGE_SESSION_KEY] = lang_code
            user_language = request.POST.get('language')
            translation.activate(user_language)
            #request.session[translation.LANGUAGE_SESSION_KEY] = user_language
            request.session[LANGUAGE_SESSION_KEY] = user_language
            logger.debug(f"Language switched to: {user_language}")  

    return redirect(request.META.get('HTTP_REFERER', '/'))  # Redirect back to the previous page

@login_required
def StudentTranscriptView(request):
    transcripts = Transcript.objects.all()  
    return render(request, 'transcript.html',{'transcripts': transcripts})

@login_required
def Faculties(request):
    return render(request, 'faculties.html')

def add_area_elective_course(request):
    if request.method == 'POST':
        # Collect the data from the form
        form_data = request.POST
        faculty = form_data.get('faculty')  # Get the selected faculty/department

        course_data = []
        i = 1

        # Collect course data from form
        while f'course_code_{i}' in form_data:
            course = {
                'course_code': form_data.get(f'course_code_{i}'),
                'title': form_data.get(f'course_title_{i}'),
                'category': form_data.get(f'course_category_{i}'),
                'hours_lecture': form_data.get(f'hours_lecture_{i}'),
                'hours_tutorial': form_data.get(f'hours_tutorial_{i}'),
                'hours_lab': form_data.get(f'hours_lab_{i}'),
                'ects_credit': form_data.get(f'ects_credit_{i}'),
                'total_credits': form_data.get(f'total_credits_{i}')
            }
            course_data.append(course)
            i += 1

        # Save each course to the corresponding faculty's table
        model_mapping = {
            'Computer_OldCatalog': AreaElectiveCourse_Computer_OldCatalog,
            'Computer_Newcatalog': AreaElectiveCourse_Computer_Newcatalog,
            'Civil_Newcatalog': AreaElectiveCourse_Civil_Newcatalog,
            'Civil_Oldcatalog': AreaElectiveCourse_civil_OldCatalog,
            'EE_OldCatalog': AreaElectiveCourse_EE_OldCatalog,
            'EE_Newcatalog': AreaElectiveCourse_EE_Newcatalog,
            'AI_Catalog': AreaElectiveCourse_AI_Catalog,
            'Software_Newcatalog': AreaElectiveCourse_Software_Newcatalog,
            'Software_Oldcatalog': AreaElectiveCourse_Software_Oldcatalog,
            'dentistryE_Catalog': AreaElectiveCourse_dentistryE_Catalog,
            'dentistryT_Catalog': AreaElectiveCourse_dentistryT_Catalog,
            'PharmacyEP_Catalog': AreaElectiveCourse_PharmacyEP_Catalog,
            'PharmacyEM_Catalog': AreaElectiveCourse_PharmacyEM_Catalog,
            'PharmacyT_Catalog': AreaElectiveCourse_PharmacyT_Catalog,
            'ELT_NewCatalog': AreaElectiveCourse_ELT_NewCatalog,
            'ELT_MidleCatalog': AreaElectiveCourse_ELT_MidleCatalog,
            'ELT_OldCtalog': AreaElectiveCourse_ELT_OldCtalog,
            'PE_NewCatalog': AreaElectiveCourse_PE_NewCatalog,
            'PE_MidleCatalog': AreaElectiveCourse_PE_MidleCatalog,
            'PE_OldCtalog': AreaElectiveCourse_PE_OldCtalog,
            'SET_NewCatalog': AreaElectiveCourse_SET_NewCatalog,
            'SET_OldCatalog': AreaElectiveCourse_SET_OldCatalog,
            'GPC_NewCatalog': AreaElectiveCourse_GPC_NewCatalog,
            'GPC_MidleCatalog': AreaElectiveCourse_GPC_MidleCatalog,
            'GPC_OldCtalog': AreaElectiveCourse_GPC_OldCtalog,
            'TLT_NewCatalog': AreaElectiveCourse_TLT_NewCatalog,
            'TLT_MidleCatalog': AreaElectiveCourse_TLT_MidleCatalog,
            'TLT_OldCtalog': AreaElectiveCourse_TLT_OldCtalog,
            'PFCP_Curriculum': AreaElectiveCourse_PFCP_Curriculum,
            'PSYE_NewCatalog': AreaElectiveCourse_PSYE_NewCatalog,
            'PSYE_OldCatalog': AreaElectiveCourse_PSYE_OldCatalog,
            'PSYT_NewCatalog': AreaElectiveCourse_PSYT_NewCatalog,
            'PSYT_OldCatalog': AreaElectiveCourse_PSYT_OldCatalog,
            'LAW_NewCatalog': AreaElectiveCourse_LAW_NewCatalog,
            'LAW_OldCatalog': AreaElectiveCourse_LAW_OldCatalog,
            'INTLAW_NewCatalog': AreaElectiveCourse_INTLAW_NewCatalog,
            'INTLAW_OldCatalog': AreaElectiveCourse_INTLAW_OldCatalog,
            'BA_NewCatalog': AreaElectiveCourse_BA_NewCatalog,
            'BA_OldCatalog': AreaElectiveCourse_BA_OldCatalog,
            'BE_Catalog': AreaElectiveCourse_BE_Catalog,
            'BAM_Catalog': AreaElectiveCourse_BAM_Catalog,
            'BFA_NewCatalog': AreaElectiveCourse_BFA_NewCatalog,
            'BFA_OldCatalog': AreaElectiveCourse_BFA_OldCatalog,
            'MDM_Catalog': AreaElectiveCourse_MDM_Catalog,
            'ECO_Catalog': AreaElectiveCourse_ECO_Catalog,
            'PSIR_NewCatalog': AreaElectiveCourse_PSIR_NewCatalog,
            'PSIR_OldCatalog': AreaElectiveCourse_PSIR_OldCatalog,
            'IFB_NewCatalog': AreaElectiveCourse_IFB_NewCatalog,
            'IFB_OldCatalog': AreaElectiveCourse_IFB_OldCatalog,
            'ITB_NewCatalog': AreaElectiveCourse_ITB_NewCatalog,
            'ITB_OldCatalog': AreaElectiveCourse_ITB_OldCatalog,
            'MIS_NewCatalog': AreaElectiveCourse_MIS_NewCatalog,
            'MIS_OldCatalog': AreaElectiveCourse_MIS_OldCatalog,
            'IntArch_NewCatalog': AreaElectiveCourse_IntArch_NewCatalog,
            'IntArch_OldCatalog': AreaElectiveCourse_IntArch_OldCatalog,
            'ARCHI_NewCatalog': AreaElectiveCourse_ARCHI_NewCatalog,
            'ARCHI_OldCatalog': AreaElectiveCourse_ARCHI_OldCatalog,
            'Nutrition_Catalog': AreaElectiveCourse_Nutrition_Catalog,
            'physio_engl_Catalog': AreaElectiveCourse_physio_engl_Catalog,
            'physio_TNewCatalog': AreaElectiveCourse_physio_TNewCatalog,
            'physio_TOldCatalog': AreaElectiveCourse_physio_TOldCatalog,
            'Nursing_Catalog': AreaElectiveCourse_Nursing_Catalog
        }

        # Get the correct model based on the selected faculty
        CourseModel = model_mapping.get(faculty)

        if CourseModel:
            for data in course_data:
                CourseModel.objects.create(**data)

        # Redirect to the faculties or any other page
        return redirect('faculties')  # Adjust as needed

    else:
        return render(request, 'add_area_elective_course.html')

#/////////////////////////////////ENGINEERING FACULTY//////////////////////////////////////#

#//////COMPUTER/////#

@login_required
def Comp_Catalog(request):
    return render(request, 'engeeningfac\comp\Comp_Catalog.html')

@login_required
def Comp_NewCatalog(request):
    new_courses = Computer_Newcatalog.objects.all()
    new_elective_courses = AreaElectiveCourse_Computer_Newcatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_Computer_Newcatalog.objects.all
    return render(request, 'engeeningfac\comp\Comp_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def Comp_OldCatalog(request):
    old_courses = Computer_OldCatalog.objects.all()
    old_elective_courses = AreaElectiveCourse_Computer_OldCatalog.objects.all()
    old_technical_courses = AreaTechnicalCourse_Computer_OldCatalog.objects.all
    return render(request, 'engeeningfac\comp\Comp_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#//////SOFTWARE/////#

login_required
def Soft_Catalog(request):
    return render(request, 'engeeningfac\soft\Soft_Catalog.html')

@login_required
def Soft_NewCatalog(request):
    new_courses = Software_Newcatalog.objects.all()
    new_elective_courses = AreaElectiveCourse_Software_Newcatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_Software_Newcatalog.objects.all
    return render(request, 'engeeningfac\soft\Soft_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def Soft_OldCatalog(request):
    old_courses = Software_Oldcatalog.objects.all()
    old_elective_courses = AreaElectiveCourse_Software_Oldcatalog.objects.all
    old_technical_courses = AreaTechnicalCourse_Software_Oldcatalog.objects.all
    return render(request, 'engeeningfac\soft\Soft_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#//////CIVIL/////#

login_required
def Civil_Catalog(request):
    return render(request, 'engeeningfac\civil\Civil_Catalog.html')

@login_required
def Civil_NewCatalog(request):
    new_courses = Civil_Newcatalog.objects.all()
    new_elective_courses = AreaElectiveCourse_Civil_Newcatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_Civil_Newcatalog.objects.all
    return render(request, 'engeeningfac\civil\Civil_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def Civil_OldCatalog(request):
    old_courses = civil_OldCatalog.objects.all()
    old_elective_courses = AreaElectiveCourse_civil_OldCatalog.objects.all
    old_technical_courses = AreaTechnicalCourse_civil_OldCatalog.objects.all
    return render(request, 'engeeningfac\civil\Civil_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#//////ARTIFICIAL INTELLIGENCE/////#

@login_required
def AI_catalog(request):
    return render(request, 'engeeningfac\\ai\AI_Main.html')

@login_required
def AI_Curriculum(request):
    courses = AI_Catalog.objects.all()
    elective_courses = AreaElectiveCourse_AI_Catalog.objects.all
    technical_courses = AreaTechnicalCourse_AI_Catalog.objects.all
    return render(request, 'engeeningfac\\ai\AI_Catalog.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

#//////ELECTRICAL AND ELECTRONICS/////#

@login_required
def EE_Catalog(request):
    return render(request, 'engeeningfac\elec\EE_Catalog.html')

@login_required
def EE_NewCatalog(request):
    new_courses = EE_Newcatalog.objects.all()
    new_elective_courses = AreaElectiveCourse_EE_Newcatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_EE_Newcatalog.objects.all
    return render(request, 'engeeningfac\elec\EE_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def EE_Oldcatalog(request):
    old_courses = EE_OldCatalog.objects.all()
    old_elective_courses = AreaElectiveCourse_EE_OldCatalog.objects.all
    old_technical_courses = AreaTechnicalCourse_EE_OldCatalog.objects.all
    return render(request, 'engeeningfac\elec\EE_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#/////////////////////////////////DENTISTRY FACULTY//////////////////////////////////////#

#////ENGLISH////#

@login_required
def DentistryE_Catalog(request):
    return render(request, 'dentistryfac\DentistryE_Main.html')

@login_required
def dentistryE_Catalog(request):
    courses = Dent_English_catalog.objects.all()
    elective_courses = AreaElectiveCourse_dentistryE_Catalog.objects.all
    technical_courses = AreaTechnicalCourse_dentistryE_Catalog.objects.all
    return render(request, 'dentistryfac\DentE.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

#////TURKISH////#

@login_required
def DentistryT_Catalog(request):
    return render(request, 'dentistryfac\DentistryT_Main.html')

def dentistryT_Catalog(request):
    courses = Dent_Turkish_catalog.objects.all()
    elective_courses = AreaElectiveCourse_dentistryT_Catalog.objects.all
    technical_courses = AreaTechnicalCourse_dentistryT_Catalog.objects.all
    return render(request, 'dentistryfac\DentT.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

#/////////////////////////////////PHARMACY FACULTY//////////////////////////////////////#

#////ENGLISH////#

@login_required
def PharmacyE_Catalog(request):
    return render(request, 'pharmacyfac\PharmacyE_Main.html')

@login_required
def PharmacyEP_Catalog(request):
    courses = Pharmay_English_PharmD_catalog.objects.all()
    elective_courses = AreaElectiveCourse_PharmacyEP_Catalog.objects.all
    technical_courses = AreaTechnicalCourse_PharmacyEP_Catalog.objects.all
    return render(request, 'pharmacyfac\PharmEP.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

@login_required
def PharmacyEM_Catalog(request):
    courses = Pharmay_English_Mpharm_catalog.objects.all()
    elective_courses = AreaElectiveCourse_PharmacyEM_Catalog.objects.all
    technical_courses = AreaTechnicalCourse_PharmacyEM_Catalog.objects.all
    return render(request, 'pharmacyfac\PharmEM.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

#////TURKISH////#

@login_required
def PharmacyTM_Catalog(request):
    return render(request, 'pharmacyfac\PharmacyTM_Main.html')

@login_required
def PharmacyT_Catalog(request):
    courses = Pharmay_Turkish_catalog.objects.all()
    elective_courses = AreaElectiveCourse_PharmacyT_Catalog.objects.all
    technical_courses = AreaTechnicalCourse_PharmacyT_Catalog.objects.all
    return render(request, 'pharmacyfac\PharmT.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

#/////////////////////////////////EDUCATIONAL SCIENCES FACULTY//////////////////////////////////////#

#////ENGLISH LANGUAGE TEACHING////#

@login_required
def ELT_Catalog(request):
    return render(request, 'educational_Scfac\ENGLISH LANGUANGE TEACHING\ELT_Catalog.html')

@login_required
def ELT_NewCatalog(request):
    new_courses = Edu_ELT2021_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_ELT_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_ELT_NewCatalog.objects.all
    return render(request, 'educational_Scfac\ENGLISH LANGUANGE TEACHING\ELT_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses,'new_technical_courses': new_technical_courses})

@login_required
def ELT_MidleCatalog(request):
    courses = Edu_ELT2018_catalog.objects.all()
    elective_courses = AreaElectiveCourse_ELT_MidleCatalog.objects.all
    technical_courses = AreaTechnicalCourse_ELT_MidleCatalog.objects.all
    return render(request, 'educational_Scfac\ENGLISH LANGUANGE TEACHING\ELT_MidleCatalog.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

@login_required
def ELT_OldCtalog(request):
    old_courses = Edu_ELT_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_ELT_OldCtalog.objects.all
    old_technical_courses = AreaTechnicalCourse_ELT_OldCtalog.objects.all
    return render(request, 'educational_Scfac\ENGLISH LANGUANGE TEACHING\ELT_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#////PRESCHOOL EDUCATION////#

@login_required
def PE_Catalog(request):
    return render(request, 'educational_Scfac\PRESCHOOL EDUCATION\PE_Catalog.html')

@login_required
def PE_NewCatalog(request):
    new_courses = Edu_PE2021_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_PE_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_PE_NewCatalog.objects.all
    return render(request, 'educational_Scfac\PRESCHOOL EDUCATION\PE_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def PE_MidleCatalog(request):
    courses = Edu_PE2018_catalog.objects.all()
    elective_courses = AreaElectiveCourse_PE_MidleCatalog.objects.all
    technical_courses = AreaTechnicalCourse_PE_MidleCatalog.objects.all
    return render(request, 'educational_Scfac\PRESCHOOL EDUCATION\PE_MidleCatalog.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

@login_required
def PE_OldCtalog(request):
    old_courses = Edu_PE_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_PE_OldCtalog.objects.all
    old_technical_courses = AreaTechnicalCourse_PE_OldCtalog.objects.all
    return render(request, 'educational_Scfac\PRESCHOOL EDUCATION\PE_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses })

#////SPECIAL EDUCATION TEACHING////#

@login_required
def SET_Catalog(request):
    return render(request, 'educational_Scfac\SPECIAL EDUCATION TEACHING\SET_Catalog.html')

@login_required
def SET_NewCatalog(request):
    new_courses = Edu_SET2021_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_SET_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_SET_NewCatalog.objects.all
    return render(request, 'educational_Scfac\SPECIAL EDUCATION TEACHING\SET_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def SET_OldCtalog(request):
    old_courses = Edu_SET2018_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_SET_OldCatalog.objects.all
    old_technical_courses = AreaTechnicalCourse_SET_OldCatalog.objects.all
    return render(request, 'educational_Scfac\SPECIAL EDUCATION TEACHING\SET_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#////GUIDANCE AND PSYCHOLOGICAL COUNSELING////#

@login_required
def GPC_Catalog(request):
    return render(request, 'educational_Scfac\GUIDANCE AND PSYCHOLOGICAL COUNSELING\GPC_Catalog.html')

@login_required
def GPC_NewCatalog(request):
    new_courses = Edu_GPC2021_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_GPC_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_GPC_NewCatalog.objects.all
    return render(request, 'educational_Scfac\GUIDANCE AND PSYCHOLOGICAL COUNSELING\GPC_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def GPC_MidleCatalog(request):
    courses = Edu_GPC2018_catalog.objects.all()
    elective_courses = AreaElectiveCourse_GPC_MidleCatalog.objects.all
    technical_courses = AreaTechnicalCourse_GPC_MidleCatalog.objects.all
    return render(request, 'educational_Scfac\GUIDANCE AND PSYCHOLOGICAL COUNSELING\GPC_MidleCatalog.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

@login_required
def GPC_OldCatalog(request):
    old_courses = Edu_GPC_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_GPC_OldCtalog.objects.all
    old_technical_courses = AreaTechnicalCourse_GPC_OldCtalog.objects.all
    return render(request, 'educational_Scfac\GUIDANCE AND PSYCHOLOGICAL COUNSELING\GPC_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#////TURKISH LANGUANGE TEACHING////#

@login_required
def TLT_Catalog(request):
    return render(request, 'educational_Scfac\TURKISH LANGUANGE TEACHING\TLT_Catalog.html')

@login_required
def TLT_NewCatalog(request):
    new_courses = Edu_TLT2021_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_TLT_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_TLT_NewCatalog.objects.all
    return render(request, 'educational_Scfac\TURKISH LANGUANGE TEACHING\TLT_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def TLT_MidleCatalog(request):
    courses = Edu_TLT2018_catalog.objects.all()
    elective_courses = AreaElectiveCourse_TLT_MidleCatalog.objects.all
    technical_courses = AreaTechnicalCourse_TLT_MidleCatalog.objects.all
    return render(request, 'educational_Scfac\TURKISH LANGUANGE TEACHING\TLT_MidleCatalog.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

@login_required
def TLT_OldCtalog(request):
    old_courses = Edu_TLT_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_TLT_OldCtalog.objects.all
    old_technical_courses = AreaTechnicalCourse_TLT_OldCtalog.objects.all
    return render(request, 'educational_Scfac\TURKISH LANGUANGE TEACHING\TLT_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#////PEDACOGICAL FORMATION CERTIFICATE PROGRAM////#

@login_required
def PFCP_Catalog(request):
    return render(request, 'educational_Scfac/PEDACOGICAL FORMATION CERTIFICATE PROGRAM/PFCP_Main.html')

@login_required
def PFCP_Curriculum(request):
    courses = Edu_PFCP_catalog.objects.all()
    elective_courses = AreaElectiveCourse_PFCP_Curriculum.objects.all
    technical_courses = AreaTechnicalCourse_PFCP_Curriculum.objects.all
    return render(request, 'educational_Scfac/PEDACOGICAL FORMATION CERTIFICATE PROGRAM/PFCP.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

#/////////////////////////////////ARTS AND SCIENCES FACULTY//////////////////////////////////////#

#////ENGLISH////#

@login_required
def PSYE_Catalog(request):
    return render(request, 'arts_and_Scfac\PSYE.html')

@login_required
def PSYE_NewCatalog(request):
    new_courses = Psycholoy_English_New_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_PSYE_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_PSYE_NewCatalog.objects.all
    return render(request, 'arts_and_Scfac\PSYE_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def PSYE_OldCatalog(request):
    old_courses = Psycholoy_English_Old_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_PSYE_OldCatalog.objects.all
    old_technical_courses = AreaTechnicalCourse_PSYE_OldCatalog.objects.all
    return render(request, 'arts_and_Scfac\PSYE_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#////TURKISH////#

@login_required
def PSYT_Catalog(request):
    return render(request, 'arts_and_Scfac\PSYT.html')

@login_required
def PSYT_NewCatalog(request):
    new_courses = Psychologyy_Turkish_New_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_PSYT_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_PSYT_NewCatalog.objects.all
    return render(request, 'arts_and_Scfac\PSYT_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def PSYT_OldCatalog(request):
    old_courses = Psychologyy_Turkish_Old_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_PSYT_OldCatalog.objects.all
    old_technical_courses = AreaTechnicalCourse_PSYT_OldCatalog.objects.all
    return render(request, 'arts_and_Scfac\PSYT_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#/////////////////////////////////LAW FACULTY//////////////////////////////////////#

#////LAW////#

@login_required
def Law_Catalog(request):
    return render(request, 'lawfac\LAW\Law_Main.html')

@login_required
def LAW_NewCatalog(request):
    new_courses = Law_New_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_LAW_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_LAW_NewCatalog.objects.all
    return render(request, 'lawfac\LAW\LAW_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def LAW_OldCatalog(request):
    old_courses = Law_Old_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_LAW_OldCatalog.objects.all()
    old_technical_courses = AreaTechnicalCourse_LAW_OldCatalog.objects.all()
    return render(request, 'lawfac\LAW\LAW_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#////INTERNATIONAL LAW////#

@login_required
def INTLaw_Catalog(request):
    return render(request, 'lawfac\INTERNATIONAL LAW\intLaw_Main.html')

@login_required
def INTLAW_NewCatalog(request):
    new_courses = Int_Law_New_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_INTLAW_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_INTLAW_NewCatalog.objects.all()
    return render(request, 'lawfac\INTERNATIONAL LAW\intLAW_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def INTLAW_OldCatalog(request):
    old_courses = Int_Law_Old_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_INTLAW_OldCatalog.objects.all()
    old_technical_courses = AreaTechnicalCourse_INTLAW_OldCatalog.objects.all()
    return render(request, 'lawfac\INTERNATIONAL LAW\intLAW_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#/////////////////////////////////ECONOMICS AND ADMINISTRATIVE SCIENCE FACULTY//////////////////////////////////////#

#////BUSINESS ADMISTRATION////#

@login_required
def BA_Catalog(request):
    return render(request, 'economicfac\BUSINESS ADMISTRATION\BA_Main.html')

@login_required
def BA_NewCatalog(request):
    new_courses = BA_New_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_BA_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_BA_NewCatalog.objects.all()
    return render(request, 'economicfac\BUSINESS ADMISTRATION\BA_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def BA_OldCatalog(request):
    old_courses = BA_Old_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_BA_OldCatalog.objects.all()
    old_technical_courses = AreaTechnicalCourse_BA_OldCatalog.objects.all()
    return render(request, 'economicfac\BUSINESS ADMISTRATION\BA_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#////BUSINESS ENTREPRENEURSHIP////#

@login_required
def BE_Main_Catalog(request):
    return render(request, 'economicfac\BUSINESS ENTREPRENEURSHIP\BE_Main.html')

@login_required
def BE_Catalog(request):
    courses = BE_catalog.objects.all()
    elective_courses = AreaElectiveCourse_BE_Catalog.objects.all
    technical_courses = AreaTechnicalCourse_BE_Catalog.objects.all
    return render(request, 'economicfac\BUSINESS ENTREPRENEURSHIP\BE_Catalog.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

#////BUSINESS ADMISTRATION Marketing////#

@login_required
def BAM_Main_Catalog(request):
    return render(request, 'economicfac\BUSINESS ADMISTRATION Marketing\BAM_Main.html')

@login_required
def BAM_Catalog(request):
    courses = BAM_catalog.objects.all()
    elective_courses = AreaElectiveCourse_BAM_Catalog.objects.all
    technical_courses = AreaTechnicalCourse_BAM_Catalog.objects.all
    return render(request, 'economicfac\BUSINESS ADMISTRATION Marketing\BAM_Catalog.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

#////BUSINESS FINANCE AND ACCOUNTING////#

@login_required
def BFA_Catalog(request):
    return render(request, 'economicfac\BUSINESS FINANCE AND ACCOUNTING\BFA_Main.html')

@login_required
def BFA_NewCatalog(request):
    new_courses = BFA_New_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_BFA_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_BFA_NewCatalog.objects.all
    return render(request, 'economicfac\BUSINESS FINANCE AND ACCOUNTING\BFA_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def BFA_OldCatalog(request):
    old_courses = BFA_Old_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_BFA_OldCatalog.objects.all()
    old_technical_courses = AreaTechnicalCourse_BFA_OldCatalog.objects.all
    return render(request, 'economicfac\BUSINESS FINANCE AND ACCOUNTING\BFA_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#////ECONOMICS////#

@login_required
def ECO_Main_Catalog(request):
    return render(request, 'economicfac\ECONOMICS\ECO_Main.html')

@login_required
def ECO_Catalog(request):
    courses = Econo_catalog.objects.all()
    elective_courses = AreaElectiveCourse_ECO_Catalog.objects.all
    technical_courses = AreaTechnicalCourse_ECO_Catalog.objects.all
    return render(request, 'economicfac\ECONOMICS\Eco_Catalog.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

#////MARKETING DIGITAL MEDIA////#

@login_required
def MDM_Main_Catalog(request):
    return render(request, 'economicfac\MARKETING DIGITAL MEDIA\MDM_Main.html')

@login_required
def MDM_Catalog(request):
    courses = MarkDigM_catalog.objects.all()
    elective_courses = AreaElectiveCourse_MDM_Catalog.objects.all
    technical_courses = AreaTechnicalCourse_MDM_Catalog.objects.all
    return render(request, 'economicfac\MARKETING DIGITAL MEDIA\MDM_Catalog.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

#////POLITICAL SCIENCE AND INTERNATIONAL RELATION////#

@login_required
def PSIR_Catalog(request):
    return render(request, 'economicfac\POLITICAL SCIENCE AND INTERNATIONAL RELATION\PSIR_Main.html')

@login_required
def PSIR_NewCatalog(request):
    new_courses = PSIR_New_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_PSIR_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_PSIR_NewCatalog.objects.all
    return render(request, 'economicfac\POLITICAL SCIENCE AND INTERNATIONAL RELATION\PSIR_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def PSIR_OldCatalog(request):
    old_courses = PSIR_Old_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_PSIR_OldCatalog.objects.all()
    old_technical_courses = AreaTechnicalCourse_PSIR_OldCatalog.objects.all
    return render(request, 'economicfac\POLITICAL SCIENCE AND INTERNATIONAL RELATION\PSIR_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#////INTERNATIONAL FINANCE AND BANKING////#

@login_required
def IFB_Catalog(request):
    return render(request, 'economicfac\INTERNATIONAL FINANCE AND BANKING\IFB_Main.html')

@login_required
def IFB_NewCatalog(request):
    new_courses = IFB_New_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_IFB_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_IFB_NewCatalog.objects.all
    return render(request, 'economicfac\INTERNATIONAL FINANCE AND BANKING\IFB_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def IFB_OldCatalog(request):
    old_courses = IFB_Old_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_IFB_OldCatalog.objects.all()
    old_technical_courses = AreaTechnicalCourse_IFB_OldCatalog.objects.all
    return render(request, 'economicfac\INTERNATIONAL FINANCE AND BANKING\IFB_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#////INTERNATIONAL TRADE AND BUSINESS////#

@login_required
def ITB_Catalog(request):
    return render(request, 'economicfac\INTERNATIONAL TRADE AND BUSINESS\ITB_Main.html')

@login_required
def ITB_NewCatalog(request):
    new_courses = ITB_New_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_ITB_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_ITB_NewCatalog.objects.all
    return render(request, 'economicfac\INTERNATIONAL TRADE AND BUSINESS\ITB_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def ITB_OldCatalog(request):
    old_courses = ITB_Old_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_ITB_OldCatalog.objects.all()
    old_technical_courses = AreaTechnicalCourse_ITB_OldCatalog.objects.all
    return render(request, 'economicfac\INTERNATIONAL TRADE AND BUSINESS\ITB_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#////MANAGEMENT INFORMATION SYSTEM////#

@login_required
def MIS_Catalog(request):
    return render(request, 'economicfac\MANAGEMENT INFORMATION SYSTEM\MIS_Main.html')

@login_required
def MIS_NewCatalog(request):
    new_courses = MIS_New_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_MIS_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_MIS_NewCatalog.objects.all
    return render(request, 'economicfac\MANAGEMENT INFORMATION SYSTEM\MIS_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def MIS_OldCatalog(request):
    old_courses = MIS_Old_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_MIS_OldCatalog.objects.all()
    old_technical_courses = AreaTechnicalCourse_MIS_OldCatalog.objects.all
    return render(request, 'economicfac\MANAGEMENT INFORMATION SYSTEM\MIS_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#/////////////////////////////////ARCHITECHTURE AND FINE ARTS FACULTY//////////////////////////////////////#

#////INTERIOR ARCHITECHTURE////#

@login_required
def IntArch_Catalog(request):
    return render(request, 'architecturefac\INTERIOR ARCHITECHTURE\IntArch_Main.html')

@login_required
def IntArch_NewCatalog(request):
    new_courses = interior_New_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_IntArch_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_IntArch_NewCatalog.objects.all
    return render(request, 'architecturefac\INTERIOR ARCHITECHTURE\IntArch_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def IntArch_OldCatalog(request):
    old_courses = interior_Old_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_IntArch_OldCatalog.objects.all()
    old_technical_courses = AreaTechnicalCourse_IntArch_OldCatalog.objects.all
    return render(request, 'architecturefac\INTERIOR ARCHITECHTURE\IntArch_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#////ARCHITECHTURE////#

@login_required
def ARCHI_MAIN_Catalog(request):
    return render(request, 'architecturefac\ARCHITECHTURE\\archi_Main.html')

@login_required
def ARCHI_NewCatalog(request):
    new_courses = archi_New_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_ARCHI_NewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_ARCHI_NewCatalog.objects.all()
    return render(request, 'architecturefac\ARCHITECHTURE\\archi_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def ARCHI_OldCatalog(request):
    old_courses = archi_Old_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_ARCHI_OldCatalog.objects.all() 
    old_technical_courses = AreaTechnicalCourse_ARCHI_OldCatalog.objects.all()
    return render(request, 'architecturefac\ARCHITECHTURE\\archi_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#/////////////////////////////////HEALTH SCIENCE FACULTY//////////////////////////////////////#

#////NUTRITION AND DIETETICS////#

@login_required
def Nutrition_Main_Catalog(request):
    return render(request, 'health_Scfac\\nUTRITION AND DIETETICS\\nutrition_Main.html')

@login_required
def Nutrition_Catalog(request):
    courses = nutrition_catalog.objects.all()
    elective_courses = AreaElectiveCourse_Nutrition_Catalog.objects.all()
    technical_courses = AreaTechnicalCourse_Nutrition_Catalog.objects.all()
    return render(request, 'health_Scfac\\nUTRITION AND DIETETICS\\nutrition_Catalog.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

#////PHYSIOTHERAPY AND REHABILITATION////#

@login_required
def physioE_Main_Catalog(request):
    return render(request, 'health_Scfac\PHYSIOTHERAPY AND REHABILITATION\physioE_Main.html')

@login_required
def physio_engl_Catalog(request):
    courses = physiotherapy_engl_catalog.objects.all()
    elective_courses = AreaElectiveCourse_physio_engl_Catalog.objects.all
    technical_courses = AreaTechnicalCourse_physio_engl_Catalog.objects.all()
    return render(request, 'health_Scfac\PHYSIOTHERAPY AND REHABILITATION\physio_engl_Catalog.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

@login_required
def physioT_Main_Catalog(request):
    return render(request, 'health_Scfac\PHYSIOTHERAPY AND REHABILITATION\physioT_Main.html')

@login_required
def physio_TNewCatalog(request):
    new_courses = physiotherapy_turk_new_catalog.objects.all()
    new_elective_courses = AreaElectiveCourse_physio_TNewCatalog.objects.all
    new_technical_courses = AreaTechnicalCourse_physio_TNewCatalog.objects.all()
    return render(request, 'health_Scfac\PHYSIOTHERAPY AND REHABILITATION\physio_TNew_Catalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def physio_TOldCatalog(request):
    old_courses = physiotherapy_turk_old_catalog.objects.all()
    old_elective_courses = AreaElectiveCourse_physio_TOldCatalog.objects.all
    old_technical_courses = AreaTechnicalCourse_physio_TOldCatalog.objects.all()
    return render(request, 'health_Scfac\PHYSIOTHERAPY AND REHABILITATION\physio_TOld_Catalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses, 'old_technical_courses': old_technical_courses})

#////NUrsing////#

@login_required
def Nursing_Main_Catalog(request):
    return render(request, 'health_Scfac\\NUrsing\\nursing_Main.html')

@login_required
def Nursing_Catalog(request):
    courses = nursing_catalog.objects.all()
    elective_courses = AreaElectiveCourse_Nursing_Catalog .objects.all
    technical_courses = AreaTechnicalCourse_Nursing_Catalog.objects.all()
    return render(request, 'health_Scfac\\NUrsing\\nursing_Catalog.html', {'courses': courses, 'elective_courses': elective_courses, 'technical_courses': technical_courses})

#///////////////////////////////////////////////////////////////////////////////////////////////////////////#

@login_required
@transaction.atomic
def upload_transcript(request):
    if request.method == 'POST':
        form = TranscriptUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            df = None

            # Process file based on its extension
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

            # Log DataFrame info
            if df is not None:
                print("DataFrame loaded successfully")
                #print(df.head())
            else:
                return render(request, 'upload_transcript.html', {
                    'form': form,
                    'error': 'Failed to process the file.'
                })

            catalogs = {
                'Computer_Newcatalog': Computer_Newcatalog,
                'Computer_OldCatalog': Computer_OldCatalog,
                'civil_OldCatalog': civil_OldCatalog,
                'Civil_Newcatalog': Civil_Newcatalog,
                'EE_OldCatalog': EE_OldCatalog,
                'EE_Newcatalog': EE_Newcatalog,
                'AI_Catalog': AI_Catalog,
                'Software_Newcatalog': Software_Newcatalog,
                'Software_Oldcatalog': Software_Oldcatalog,
                'Dent_English_catalog': Dent_English_catalog,
                'Dent_Turkish_catalog': Dent_Turkish_catalog,
                'Pharmay_English_Mpharm_catalog': Pharmay_English_Mpharm_catalog,
                'Pharmay_English_PharmD_catalog': Pharmay_English_PharmD_catalog,
                'Pharmay_Turkish_catalog': Pharmay_Turkish_catalog,
                'Pharmay_Turkish_English_PharmD_catalog': Pharmay_Turkish_English_PharmD_catalog,
                'Edu_ELT2021_catalog': Edu_ELT2021_catalog,
                'Edu_ELT2018_catalog': Edu_ELT2018_catalog,
                'Edu_ELT_catalog': Edu_ELT_catalog,
                'Edu_SET2021_catalog': Edu_SET2021_catalog,
                'Edu_SET2018_catalog': Edu_SET2018_catalog,
                'Edu_PE2021_catalog': Edu_PE2021_catalog,
                'Edu_PE2018_catalog': Edu_PE2018_catalog,
                'Edu_PE_catalog': Edu_PE_catalog,
                'Edu_GPC2021_catalog': Edu_GPC2021_catalog,
                'Edu_GPC2018_catalog': Edu_GPC2018_catalog,
                'Edu_GPC_catalog': Edu_GPC_catalog,
                'Edu_TLT2021_catalog': Edu_TLT2021_catalog,
                'Edu_TLT2018_catalog': Edu_TLT2018_catalog,
                'Edu_TLT_catalog': Edu_TLT_catalog,
                'Edu_PFCP_catalog': Edu_PFCP_catalog,
                'Psycholoy_English_New_catalog': Psycholoy_English_New_catalog,
                'Psycholoy_English_Old_catalog': Psycholoy_English_Old_catalog,
                'Psychologyy_Turkish_New_catalog': Psychologyy_Turkish_New_catalog,
                'Psychologyy_Turkish_Old_catalog': Psychologyy_Turkish_Old_catalog,
                'Law_New_catalog': Law_New_catalog,
                'Law_Old_catalog': Law_Old_catalog,
                'Int_Law_New_catalog': Int_Law_New_catalog,
                'Int_Law_Old_catalog': Int_Law_Old_catalog,
                'BA_New_catalog': BA_New_catalog,
                'BA_Old_catalog': BA_Old_catalog,
                'BE_catalog': BE_catalog,
                'BAM_catalog': BAM_catalog,
                'BFA_New_catalog': BFA_New_catalog,
                'BFA_Old_catalog': BFA_Old_catalog,
                'Econo_catalog': Econo_catalog,
                'MarkDigM_catalog': MarkDigM_catalog,
                'PSIR_New_catalog': PSIR_New_catalog,
                'PSIR_Old_catalog': PSIR_Old_catalog,
                'IFB_New_catalog': IFB_New_catalog,
                'IFB_Old_catalog': IFB_Old_catalog,
                'ITB_New_catalog': ITB_New_catalog,
                'ITB_Old_catalog': ITB_Old_catalog,
                'MIS_New_catalog': MIS_New_catalog,
                'MIS_Old_catalog': MIS_Old_catalog,
                'interior_New_catalog': interior_New_catalog,
                'interior_Old_catalog': interior_Old_catalog,
                'archi_New_catalog': archi_New_catalog,
                'archi_Old_catalog': archi_Old_catalog,
                'nutrition_catalog': nutrition_catalog,
                'physiotherapy_engl_catalog': physiotherapy_engl_catalog,
                'physiotherapy_turk_new_catalog': physiotherapy_turk_new_catalog,
                'physiotherapy_turk_old_catalog': physiotherapy_turk_old_catalog,
                'nursing_catalog': nursing_catalog,
            }

            for catalog_name, catalog_model in catalogs.items():
                # Determine parent model
                if issubclass(catalog_model, Health_Sciences_Course):
                    parent_model = Health_Sciences_Course
                elif issubclass(catalog_model, Arts_and_Sciences_Course):
                    parent_model = Arts_and_Sciences_Course
                elif issubclass(catalog_model, Economics_and_Administrative_Sciences_Course):
                    parent_model = Economics_and_Administrative_Sciences_Course
                elif issubclass(catalog_model, Law_Course):
                    parent_model = Law_Course
                elif issubclass(catalog_model, Engineering_Course):
                    parent_model = Engineering_Course
                elif issubclass(catalog_model, Architecture_and_Fine_Arts_Course):
                    parent_model = Architecture_and_Fine_Arts_Course
                elif issubclass(catalog_model, Dentistry_Course):
                    parent_model = Dentistry_Course
                elif issubclass(catalog_model, Educational_Sciences_Course):
                    parent_model = Educational_Sciences_Course
                elif issubclass(catalog_model, Phamarcy_Course):
                    parent_model = Phamarcy_Course
                else:
                    #print(f"Skipping {catalog_name} because it's not a subclass of a known parent model.")
                    continue
                # Get all course codes from the catalog model
                course_codes = set(catalog_model.objects.values_list('course_code', flat=True))

                # Filter DataFrame for courses that exist in the catalog model
                catalog_df = df[df['Code'].isin(course_codes)]

                if not catalog_df.empty:
                    #print(f"Processing DataFrame for {catalog_name}")
                    #print(catalog_df.head())
                
                # Ensure the DataFrame has the correct columns
                    columns = ['Code', 'Title of Course', 'ECTS Credits', 'Grade', 'Credits', 'Gr.Pts']
                    catalog_df = catalog_df.reindex(columns=columns)

                # Remove any extra columns
                    catalog_df = catalog_df[columns]

                # Update the grades in the respective catalog model
                for index, row in catalog_df.iterrows():
                        code = row['Code']
                        grade = row['Grade']
                        title = row['Title of Course']
                        ects_credit = row['ECTS Credits']
                        credit = row['Credits']

                        course, created = catalog_model.objects.get_or_create(course_code=code)
                        course.grade = grade
                        course.save()

                        transcript, created = Transcript.objects.update_or_create(code=code, defaults={'grades': grade},title=title,ects_credits=ects_credit,credits=credit)
                        if not created:
                            transcript.grades = grade
                            transcript.save()

            model_mapping = {
                'AreaElectiveCourse_Computer_OldCatalog': AreaElectiveCourse_Computer_OldCatalog,
                'AreaElectiveCourse_Computer_Newcatalog': AreaElectiveCourse_Computer_Newcatalog,
                'AreaElectiveCourse_Civil_Newcatalog': AreaElectiveCourse_Civil_Newcatalog,
                'AreaElectiveCourse_civil_OldCatalog': AreaElectiveCourse_civil_OldCatalog,
                'AreaElectiveCourse_EE_OldCatalog': AreaElectiveCourse_EE_OldCatalog,
                'AreaElectiveCourse_EE_Newcatalog': AreaElectiveCourse_EE_Newcatalog,
                'AreaElectiveCourse_AI_Catalog': AreaElectiveCourse_AI_Catalog,
                'AreaElectiveCourse_Software_Newcatalog': AreaElectiveCourse_Software_Newcatalog,
                'AreaElectiveCourse_Software_Oldcatalog': AreaElectiveCourse_Software_Oldcatalog,
                'AreaElectiveCourse_dentistryE_Catalog': AreaElectiveCourse_dentistryE_Catalog,
                'AreaElectiveCourse_dentistryT_Catalog': AreaElectiveCourse_dentistryT_Catalog,
                'AreaElectiveCourse_PharmacyEP_Catalog': AreaElectiveCourse_PharmacyEP_Catalog,
                'AreaElectiveCourse_PharmacyEM_Catalog': AreaElectiveCourse_PharmacyEM_Catalog,
                'AreaElectiveCourse_PharmacyT_Catalog': AreaElectiveCourse_PharmacyT_Catalog,
                'AreaElectiveCourse_ELT_NewCatalog': AreaElectiveCourse_ELT_NewCatalog,
                'AreaElectiveCourse_ELT_MidleCatalog': AreaElectiveCourse_ELT_MidleCatalog,
                'AreaElectiveCourse_ELT_OldCtalog': AreaElectiveCourse_ELT_OldCtalog,
                'AreaElectiveCourse_PE_NewCatalog': AreaElectiveCourse_PE_NewCatalog,
                'AreaElectiveCourse_PE_MidleCatalog': AreaElectiveCourse_PE_MidleCatalog,
                'AreaElectiveCourse_PE_OldCtalog': AreaElectiveCourse_PE_OldCtalog,
                'AreaElectiveCourse_SET_NewCatalog': AreaElectiveCourse_SET_NewCatalog,
                'AreaElectiveCourse_SET_OldCatalog': AreaElectiveCourse_SET_OldCatalog,
                'AreaElectiveCourse_GPC_NewCatalog': AreaElectiveCourse_GPC_NewCatalog,
                'AreaElectiveCourse_GPC_MidleCatalog': AreaElectiveCourse_GPC_MidleCatalog,
                'AreaElectiveCourse_GPC_OldCtalog': AreaElectiveCourse_GPC_OldCtalog,
                'AreaElectiveCourse_TLT_NewCatalog': AreaElectiveCourse_TLT_NewCatalog,
                'AreaElectiveCourse_TLT_MidleCatalog': AreaElectiveCourse_TLT_MidleCatalog,
                'AreaElectiveCourse_TLT_OldCtalog': AreaElectiveCourse_TLT_OldCtalog,
                'AreaElectiveCourse_PFCP_Curriculum': AreaElectiveCourse_PFCP_Curriculum,
                'AreaElectiveCourse_PSYE_NewCatalog': AreaElectiveCourse_PSYE_NewCatalog,
                'AreaElectiveCourse_PSYE_OldCatalog': AreaElectiveCourse_PSYE_OldCatalog,
                'AreaElectiveCourse_PSYT_NewCatalog': AreaElectiveCourse_PSYT_NewCatalog,
                'AreaElectiveCourse_PSYT_OldCatalog': AreaElectiveCourse_PSYT_OldCatalog,
                'AreaElectiveCourse_LAW_NewCatalog': AreaElectiveCourse_LAW_NewCatalog,
                'AreaElectiveCourse_LAW_OldCatalog': AreaElectiveCourse_LAW_OldCatalog,
                'AreaElectiveCourse_INTLAW_NewCatalog': AreaElectiveCourse_INTLAW_NewCatalog,
                'AreaElectiveCourse_INTLAW_OldCatalog': AreaElectiveCourse_INTLAW_OldCatalog,
                'AreaElectiveCourse_BA_NewCatalog': AreaElectiveCourse_BA_NewCatalog,
                'AreaElectiveCourse_BA_OldCatalog': AreaElectiveCourse_BA_OldCatalog,
                'AreaElectiveCourse_BE_Catalog': AreaElectiveCourse_BE_Catalog,
                'AreaElectiveCourse_BAM_Catalog': AreaElectiveCourse_BAM_Catalog,
                'AreaElectiveCourse_BFA_NewCatalog': AreaElectiveCourse_BFA_NewCatalog,
                'AreaElectiveCourse_BFA_OldCatalog': AreaElectiveCourse_BFA_OldCatalog,
                'AreaElectiveCourse_MDM_Catalog': AreaElectiveCourse_MDM_Catalog,
                'AreaElectiveCourse_ECO_Catalog': AreaElectiveCourse_ECO_Catalog,
                'AreaElectiveCourse_PSIR_NewCatalog': AreaElectiveCourse_PSIR_NewCatalog,
                'AreaElectiveCourse_PSIR_OldCatalog': AreaElectiveCourse_PSIR_OldCatalog,
                'AreaElectiveCourse_IFB_NewCatalog': AreaElectiveCourse_IFB_NewCatalog,
                'AreaElectiveCourse_IFB_OldCatalog': AreaElectiveCourse_IFB_OldCatalog,
                'AreaElectiveCourse_ITB_NewCatalog': AreaElectiveCourse_ITB_NewCatalog,
                'AreaElectiveCourse_ITB_OldCatalog': AreaElectiveCourse_ITB_OldCatalog,
                'AreaElectiveCourse_MIS_NewCatalog': AreaElectiveCourse_MIS_NewCatalog,
                'AreaElectiveCourse_MIS_OldCatalog': AreaElectiveCourse_MIS_OldCatalog,
                'AreaElectiveCourse_IntArch_NewCatalog': AreaElectiveCourse_IntArch_NewCatalog,
                'AreaElectiveCourse_IntArch_OldCatalog': AreaElectiveCourse_IntArch_OldCatalog,
                'AreaElectiveCourse_ARCHI_NewCatalog': AreaElectiveCourse_ARCHI_NewCatalog,
                'AreaElectiveCourse_ARCHI_OldCatalog': AreaElectiveCourse_ARCHI_OldCatalog,
                'AreaElectiveCourse_Nutrition_Catalog': AreaElectiveCourse_Nutrition_Catalog,
                'AreaElectiveCourse_physio_engl_Catalog': AreaElectiveCourse_physio_engl_Catalog,
                'AreaElectiveCourse_physio_TNewCatalog': AreaElectiveCourse_physio_TNewCatalog,
                'AreaElectiveCourse_physio_TOldCatalog': AreaElectiveCourse_physio_TOldCatalog,
                'AreaElectiveCourse_Nursing_Catalog': AreaElectiveCourse_Nursing_Catalog
        }
            
            # Ensure DataFrame is correct
            columns = ['Code', 'Title of Course', 'ECTS Credits', 'Grade', 'Credits']
            
            for catalog_name, elective_model in model_mapping.items():
                elective_model: Type[Model]  # Tell the editor that elective_model is a Django model class
                
                # Get all course codes from the current model
                course_codes = set(elective_model.objects.values_list('course_code', flat=True))

                # Filter the DataFrame for the current model's course codes
                catalog_df = df[df['Code'].isin(course_codes)]

                # If no matching courses in the DataFrame for the current model, skip it
                if catalog_df.empty:
                    continue

                # Filter the DataFrame for the current model's course codes
                catalog_df = df[df['Code'].isin(course_codes)].reindex(columns=columns)
                
                # Iterate through the filtered DataFrame and update the corresponding model
                for index, row in catalog_df.iterrows():
                    code = row['Code']
                    grade = row['Grade']
                    title = row['Title of Course']
                    ects_credit = row['ECTS Credits']
                    credit = row['Credits']

                elective, created = elective_model.objects.get_or_create(
                course_code=code)
                elective.grade = grade
                elective.save()
           
            technical_elective_mapping = {
                'AreaTechnicalCourse_Computer_OldCatalog': AreaTechnicalCourse_Computer_OldCatalog,
                'AreaTechnicalCourse_Computer_Newcatalog': AreaTechnicalCourse_Computer_Newcatalog,
                'AreaTechnicalCourse_Civil_Newcatalog': AreaTechnicalCourse_Civil_Newcatalog,
                'AreaTechnicalCourse_civil_Oldcatalog': AreaTechnicalCourse_civil_OldCatalog,
                'AreaTechnicalCourse_EE_OldCatalog': AreaTechnicalCourse_EE_OldCatalog,
                'AreaTechnicalCourse_EE_Newcatalog': AreaTechnicalCourse_EE_Newcatalog,
                'AreaTechnicalCourse_AI_Catalog': AreaTechnicalCourse_AI_Catalog,
                'AreaTechnicalCourse_Software_Newcatalog': AreaTechnicalCourse_Software_Newcatalog,
                'AreaTechnicalCourse_Software_Oldcatalog': AreaTechnicalCourse_Software_Oldcatalog,
                'AreaTechnicalCourse_dentistryE_Catalog': AreaTechnicalCourse_dentistryE_Catalog,
                'AreaTechnicalCourse_dentistryT_Catalog': AreaTechnicalCourse_dentistryT_Catalog,
                'AreaTechnicalCourse_PharmacyEP_Catalog': AreaTechnicalCourse_PharmacyEP_Catalog,
                'AreaTechnicalCourse_PharmacyEM_Catalog': AreaTechnicalCourse_PharmacyEM_Catalog,
                'AreaTechnicalCourse_PharmacyT_Catalog': AreaTechnicalCourse_PharmacyT_Catalog,
                'AreaTechnicalCourse_ELT_NewCatalog': AreaTechnicalCourse_ELT_NewCatalog,
                'AreaTechnicalCourse_ELT_MidleCatalog': AreaTechnicalCourse_ELT_MidleCatalog,
                'AreaTechnicalCourse_ELT_OldCtalog': AreaTechnicalCourse_ELT_OldCtalog,
                'AreaTechnicalCourse_PE_NewCatalog': AreaTechnicalCourse_PE_NewCatalog,
                'AreaTechnicalCourse_PE_MidleCatalog': AreaTechnicalCourse_PE_MidleCatalog,
                'AreaTechnicalCourse_PE_OldCtalog': AreaTechnicalCourse_PE_OldCtalog,
                'AreaTechnicalCourse_SET_NewCatalog': AreaTechnicalCourse_SET_NewCatalog,
                'AreaTechnicalCourse_SET_OldCatalog': AreaTechnicalCourse_SET_OldCatalog,
                'AreaTechnicalCourse_GPC_NewCatalog': AreaTechnicalCourse_GPC_NewCatalog,
                'AreaTechnicalCourse_GPC_MidleCatalog': AreaTechnicalCourse_GPC_MidleCatalog,
                'AreaTechnicalCourse_GPC_OldCtalog': AreaTechnicalCourse_GPC_OldCtalog,
                'AreaTechnicalCourse_TLT_NewCatalog': AreaTechnicalCourse_TLT_NewCatalog,
                'AreaTechnicalCourse_TLT_MidleCatalog': AreaTechnicalCourse_TLT_MidleCatalog,
                'AreaTechnicalCourse_TLT_OldCtalog': AreaTechnicalCourse_TLT_OldCtalog,
                'AreaTechnicalCourse_PFCP_Curriculum': AreaTechnicalCourse_PFCP_Curriculum,
                'AreaTechnicalCourse_PSYE_NewCatalog': AreaTechnicalCourse_PSYE_NewCatalog,
                'AreaTechnicalCourse_PSYE_OldCatalog': AreaTechnicalCourse_PSYE_OldCatalog,
                'AreaTechnicalCourse_PSYT_NewCatalog': AreaTechnicalCourse_PSYT_NewCatalog,
                'AreaTechnicalCourse_PSYT_OldCatalog': AreaTechnicalCourse_PSYT_OldCatalog,
                'AreaTechnicalCourse_LAW_NewCatalog': AreaTechnicalCourse_LAW_NewCatalog,
                'AreaTechnicalCourse_LAW_OldCatalog': AreaTechnicalCourse_LAW_OldCatalog,
                'AreaTechnicalCourse_INTLAW_NewCatalog': AreaTechnicalCourse_INTLAW_NewCatalog,
                'AreaTechnicalCourse_INTLAW_OldCatalog': AreaTechnicalCourse_INTLAW_OldCatalog,
                'AreaTechnicalCourse_BA_NewCatalog': AreaTechnicalCourse_BA_NewCatalog,
                'AreaTechnicalCourse_BA_OldCatalog': AreaTechnicalCourse_BA_OldCatalog,
                'AreaTechnicalCourse_BE_Catalog': AreaTechnicalCourse_BE_Catalog,
                'AreaTechnicalCourse_BAM_Catalog': AreaTechnicalCourse_BAM_Catalog,
                'AreaTechnicalCourse_BFA_NewCatalog': AreaTechnicalCourse_BFA_NewCatalog,
                'AreaTechnicalCourse_BFA_OldCatalog': AreaTechnicalCourse_BFA_OldCatalog,
                'AreaTechnicalCourse_MDM_Catalog': AreaTechnicalCourse_MDM_Catalog,
                'AreaTechnicalCourse_ECO_Catalog': AreaTechnicalCourse_ECO_Catalog,
                'AreaTechnicalCourse_PSIR_NewCatalog': AreaTechnicalCourse_PSIR_NewCatalog,
                'AreaTechnicalCourse_PSIR_OldCatalog': AreaTechnicalCourse_PSIR_OldCatalog,
                'AreaTechnicalCourse_IFB_NewCatalog': AreaTechnicalCourse_IFB_NewCatalog,
                'AreaTechnicalCourse_IFB_OldCatalog': AreaTechnicalCourse_IFB_OldCatalog,
                'AreaTechnicalCourse_ITB_NewCatalog': AreaTechnicalCourse_ITB_NewCatalog,
                'AreaTechnicalCourse_ITB_OldCatalog': AreaTechnicalCourse_ITB_OldCatalog,
                'AreaTechnicalCourse_MIS_NewCatalog': AreaTechnicalCourse_MIS_NewCatalog,
                'AreaTechnicalCourse_MIS_OldCatalog': AreaTechnicalCourse_MIS_OldCatalog,
                'AreaTechnicalCourse_IntArch_NewCatalog': AreaTechnicalCourse_IntArch_NewCatalog,
                'AreaTechnicalCourse_IntArch_OldCatalog': AreaTechnicalCourse_IntArch_OldCatalog,
                'AreaTechnicalCourse_ARCHI_NewCatalog': AreaTechnicalCourse_ARCHI_NewCatalog,
                'AreaTechnicalCourse_ARCHI_OldCatalog': AreaTechnicalCourse_ARCHI_OldCatalog,
                'AreaTechnicalCourse_Nutrition_Catalog': AreaTechnicalCourse_Nutrition_Catalog,
                'AreaTechnicalCourse_physio_engl_Catalog': AreaTechnicalCourse_physio_engl_Catalog,
                'AreaTechnicalCourse_physio_TNewCatalog': AreaTechnicalCourse_physio_TNewCatalog,
                'AreaTechnicalCourse_physio_TOldCatalog': AreaTechnicalCourse_physio_TOldCatalog,
                'AreaTechnicalCourse_Nursing_Catalog': AreaTechnicalCourse_Nursing_Catalog
            }

            # Ensure DataFrame is correct
            columns = ['Code', 'Title of Course', 'ECTS Credits', 'Grade', 'Credits']
            
            for catalog_name, technical_model in technical_elective_mapping.items():
                technical_model: Type[Model]  # Tell the editor that elective_model is a Django model class
                
                # Get all course codes from the current model
                course_codes = set(technical_model.objects.values_list('course_code', flat=True))

                # Filter the DataFrame for the current model's course codes
                catalog_df = df[df['Code'].isin(course_codes)]

                # If no matching courses in the DataFrame for the current model, skip it
                if catalog_df.empty:
                    continue

                # Filter the DataFrame for the current model's course codes
                catalog_df = df[df['Code'].isin(course_codes)].reindex(columns=columns)
                
                # Iterate through the filtered DataFrame and update the corresponding model
                for index, row in catalog_df.iterrows():
                    code = row['Code']
                    grade = row['Grade']
                    title = row['Title of Course']
                    ects_credit = row['ECTS Credits']
                    credit = row['Credits']

                technical, created = technical_model.objects.get_or_create(
                course_code=code)
                technical.grade = grade
                technical.save()
           
            return redirect('faculties')

    else:
        form = TranscriptUploadForm()
    return render(request, 'upload_transcript.html', {'form': form})

def process_csv(file: io.BufferedReader) -> pd.DataFrame:
    df = pd.read_csv(file)
    return df

#def process_csv(file: io.BufferedReader) -> pd.DataFrame:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file)
    
    # Convert DataFrame to a string to mimic the text structure from the PDF function
    text = df.to_string(index=False, header=False)
    
    # Clean the text by removing unwanted characters like (rst) and *
    clean_text = re.sub(r'\s*\(rst\)|\*', '', text)
    
    # Process the cleaned text to extract course data and return a DataFrame
    return process_text_data(clean_text)

#def process_excel(file: io.BufferedReader) -> pd.DataFrame:
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file)

    # Convert DataFrame to a string to mimic the text structure from the PDF function
    text = df.to_string(index=False, header=False)

    # Clean the text by removing unwanted characters like (rst) and *
    clean_text = re.sub(r'\s*\(rst\)|\*', '', text)

    # Process the cleaned text to extract course data and return a DataFrame
    
    return process_text_data(clean_text)

def process_excel(file: io.BufferedReader) -> pd.DataFrame:

    df = pd.read_excel(file)
    return df

def process_pdf(file: io.BufferedReader) -> pd.DataFrame:
    # Read the PDF file using PyPDF2
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''

    # Extract text from each page
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Clean the extracted text by removing unwanted characters like (rst) and *
    clean_text = re.sub(r'\s*\(rst\)|\*', '', text)

    # Process the cleaned text to extract course data and return a DataFrame
    return process_text_data(clean_text)

def process_docx(file: io.BufferedReader) -> pd.DataFrame:
    doc = docx.Document(file)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return process_text_data(text)

def process_txt(file: io.BufferedReader) -> pd.DataFrame:
    text = file.read().decode('utf-8')
    return process_text_data(text)

#def process_txt(file):
#return pd.read_csv(file, delimiter="\t")

#def process_text_data(text: str) -> pd.DataFrame:
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
                data['Title of Course'].append(' '.join(fields[0:-5]))
                data['ECTS Credits'].append(fields[-3])
                data['Grade'].append(fields[-4])
                data['Credits'].append(fields[-2])
                data['Gr.Pts'].append(fields[-1])          
    
    df = pd.DataFrame(data)
    print("Processed DataFrame from text data:", df)
    return df

def process_text_data(text: str) -> pd.DataFrame:
    # Initialize data structure to store extracted information
    data = {
        'Code': [],
        'Title of Course': [],
        'ECTS Credits': [],
        'Grade': [],
        'Credits': [],
        'Gr.Pts': []
    }
    
    # Clean up the text by removing unwanted characters like (rst) and *
    clean_text = re.sub(r'\s*\(rst\)|\*', '', text)
    
    # Split the text by lines
    lines = clean_text.split('\n')
    
    # Define the expected columns and flag for when the header is found
    columns = ['Code', 'Title of Course', 'ECTS Credits', 'Grade', 'Credits', 'Gr.Pts']
    header_found = False

    for line in lines:
        # Skip lines until we find the header
        if not header_found:
            if all(col in line for col in columns):
                header_found = True
            continue
        
        # After header is found, process each line to extract data
        if header_found:
            fields = line.split()
            
            # Check if there are at least 6 fields, adjust accordingly if not
            if len(fields) >= 6:
                # Extract course code, title, credits, grade, and points
                data['Code'].append(fields[-5])
                data['Title of Course'].append(' '.join(fields[0:-5]))  # All before the last 5 fields is the title
                data['ECTS Credits'].append(fields[-3])
                data['Grade'].append(fields[-4])
                data['Credits'].append(fields[-2])
                data['Gr.Pts'].append(fields[-1])

    # Convert to DataFrame
    df = pd.DataFrame(data)
    print("Processed DataFrame from text data:", df)
    
    return df