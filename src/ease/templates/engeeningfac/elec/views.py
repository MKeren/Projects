import io
import PyPDF2
import docx
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from AcademEase.settings import LANGUAGE_QUERY_PARAMETER
from ease.forms import TranscriptUploadForm
from ease.models import AI_Catalog, Architecture_and_Fine_Arts_Course, AreaTechnicalElectiveCourse, Arts_and_Sciences_Course, BA_New_catalog, BA_Old_catalog, BAM_catalog, BE_catalog, BFA_New_catalog, BFA_Old_catalog, Civil_Newcatalog, Dent_English_catalog, Dent_Turkish_catalog, EE_Newcatalog, EE_OldCatalog, Econo_catalog, Economics_and_Administrative_Sciences_Course, Edu_ELT2018_catalog, Edu_ELT2021_catalog, Edu_ELT_catalog, Edu_GPC2018_catalog, Edu_GPC2021_catalog, Edu_GPC_catalog, Edu_PE2018_catalog, Edu_PE2021_catalog, Edu_PE_catalog, Edu_PFCP_catalog, Edu_SET2018_catalog, Edu_SET2021_catalog, Edu_TLT2018_catalog, Edu_TLT2021_catalog, Edu_TLT_catalog, Educational_Sciences_Course, Engineering_Course, Computer_Newcatalog,Computer_OldCatalog, Faculty, Health_Sciences_Course, IFB_New_catalog, IFB_Old_catalog, ITB_New_catalog, ITB_Old_catalog, Int_Law_New_catalog, Int_Law_Old_catalog, Law_Course, Law_New_catalog, Law_Old_catalog, MIS_New_catalog, MIS_Old_catalog, MarkDigM_catalog, PSIR_New_catalog, PSIR_Old_catalog,Phamarcy_Course,Dentistry_Course, Pharmay_English_Mpharm_catalog, Pharmay_English_PharmD_catalog, Pharmay_Turkish_English_PharmD_catalog, Pharmay_Turkish_catalog, Psychologyy_Turkish_New_catalog, Psychologyy_Turkish_Old_catalog, Psycholoy_English_New_catalog, Psycholoy_English_Old_catalog, Software_Newcatalog, Software_Oldcatalog,Transcript, archi_New_catalog, archi_Old_catalog, civil_OldCatalog, interior_New_catalog, interior_Old_catalog, nursing_catalog, nutrition_catalog, physiotherapy_engl_catalog, physiotherapy_turk_new_catalog, physiotherapy_turk_old_catalog
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import translate_url
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.translation import check_for_language

def set_language(request):
    next_url = request.POST.get("next", request.GET.get("next"))
    if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
        next_url = "/"
    lang_code = request.POST.get(LANGUAGE_QUERY_PARAMETER)
    if lang_code and check_for_language(lang_code):
        if next_url:
            next_trans = translate_url(next_url, lang_code)
            if next_trans != next_url:
                response = HttpResponseRedirect(next_trans)
        response.set_cookie(
            settings.LANGUAGE_COOKIE_NAME,
            lang_code,
            max_age=settings.LANGUAGE_COOKIE_AGE,
            path=settings.LANGUAGE_COOKIE_PATH,
            domain=settings.LANGUAGE_COOKIE_DOMAIN,
            secure=settings.LANGUAGE_COOKIE_SECURE,
            httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
            samesite=settings.LANGUAGE_COOKIE_SAMESITE,
        )
    return response

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
def Faculties(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculties.html', {'faculties': faculties})

@login_required
def old_catalog(request):
    computer_old_catalog = Computer_OldCatalog.objects.all()
    civil_old_catalog = civil_OldCatalog.objects.all()
    ee_old_catalog = EE_OldCatalog.objects.all()
    ai_old_catalog = AI_Catalog.objects.all()
    software_old_catalog = Software_Oldcatalog.objects.all()
    dent_english_old_catalog = Dent_English_catalog.objects.all()
    dent_turkish_old_catalog = Dent_Turkish_catalog.objects.all()
    phamacy_english_old_catalog = Pharmay_English_PharmD_catalog.objects.all()
    phamacy_turkish_old_catalog = Pharmay_Turkish_catalog.objects.all()
    educational_sciences_old_catalog = Edu_ELT2018_catalog.objects.all()
    arts_and_sciences_old_catalog = Psycholoy_English_Old_catalog.objects.all()
    law_old_catalog = Law_Old_catalog.objects.all()
    economics_and_administrative_sciences_old_catalog = BA_Old_catalog.objects.all()
    architecture_and_fine_arts_old_catalog = interior_Old_catalog.objects.all()
    health_sciences_old_catalog = nutrition_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'old_catalog.html',{
        'computer_old_catalog': computer_old_catalog,
        'civil_old_catalog': civil_old_catalog,
        'ee_old_catalog': ee_old_catalog,
        'ai_old_catalog': ai_old_catalog,
        'software_old_catalog': software_old_catalog,
        'dent_english_old_catalog': dent_english_old_catalog,
        'dent_turkish_old_catalog': dent_turkish_old_catalog,
        'phamacy_english_old_catalog': phamacy_english_old_catalog,
        'phamacy_turkish_old_catalog': phamacy_turkish_old_catalog,
        'educational_sciences_old_catalog': educational_sciences_old_catalog,
        'arts_and_sciences_old_catalog': arts_and_sciences_old_catalog,
        'law_old_catalog': law_old_catalog,
        'economics_and_administrative_sciences_old_catalog': economics_and_administrative_sciences_old_catalog,
        'architecture_and_fine_arts_old_catalog': architecture_and_fine_arts_old_catalog,
        'health_sciences_old_catalog': health_sciences_old_catalog,
        'old_elective_courses': old_elective_courses,
    })


#/////////////////////////////////ENGINEERING FACULTY//////////////////////////////////////#

#//////COMPUTER/////#

@login_required
def Comp_Catalog(request):
    return render(request, 'Comp_Catalog.html')

@login_required
def Comp_NewCatalog(request):
    new_courses = Computer_Newcatalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'Comp_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def Comp_OldCatalog(request):
    old_courses = Computer_OldCatalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'Comp_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#//////SOFTWARE/////#

login_required
def Soft_Catalog(request):
    return render(request, 'Soft_Catalog.html')

@login_required
def Soft_NewCatalog(request):
    new_courses = Software_Newcatalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'Soft_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def Soft_OldCatalog(request):
    old_courses = Software_Oldcatalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'Soft_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#//////CIVIL/////#

login_required
def Civil_Catalog(request):
    return render(request, 'Civil_Catalog.html')

@login_required
def Civil_NewCatalog(request):
    new_courses = Civil_Newcatalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'Civil_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def Civil_OldCatalog(request):
    old_courses = civil_OldCatalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'Civil_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#//////ARTIFICIAL INTELLIGENCE/////#

@login_required
def AI_catalog(request):
    return render(request, 'AI_Main.html')

@login_required
def AI_Curriculum(request):
    courses = AI_Catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'AI_Catalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#//////ELECTRICAL AND ELECTRONICS/////#

@login_required
def EE_Catalog(request):
    return render(request, 'EE_Catalog.html')

@login_required
def EE_NewCatalog(request):
    new_courses = EE_Newcatalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'EE_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def EE_Oldcatalog(request):
    old_courses = EE_OldCatalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'EE_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#/////////////////////////////////DENTISTRY FACULTY//////////////////////////////////////#

@login_required
def Dentistry_Catalog(request):
    return render(request, 'Dentistry_Main.html')

#////ENGLISH////#

@login_required
def DentistryE_Catalog(request):
    courses = Dent_English_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'DentE.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#////TURKISH////#

def DentistryT_Catalog(request):
    courses = Dent_Turkish_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'DentT.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#/////////////////////////////////PHARMACY FACULTY//////////////////////////////////////#

@login_required
def Pharmacy_Catalog(request):
    return render(request, 'Pharmacy_Main.html')

@login_required
def PharmacyEP_Catalog(request):
    courses = Pharmay_English_PharmD_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'PharmEP.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def PharmacyEM_Catalog(request):
    courses = Pharmay_English_Mpharm_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'PharmEM.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def PharmacyT_Catalog(request):
    courses = Pharmay_Turkish_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'PharmT.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def PharmacyTE_Catalog(request):
    courses = Pharmay_Turkish_English_PharmD_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'PharmTE.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#/////////////////////////////////EDUCATIONAL SCIENCES FACULTY//////////////////////////////////////#

#////ENGLISH LANGUAGE TEACHING////#

@login_required
def ELT_Catalog(request):
    return render(request, 'ELT_Catalog.html')

@login_required
def ELT_NewCatalog(request):
    courses = Edu_ELT2021_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'ELT_NewCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def ELT_MidleCatalog(request):
    courses = Edu_ELT2018_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'ELT_MidleCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def ELT_OldCtalog(request):
    courses = Edu_ELT_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'ELT_OldCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#////PRESCHOOL EDUCATION////#

@login_required
def PE_Catalog(request):
    return render(request, 'PE_Catalog.html')

@login_required
def PE_NewCatalog(request):
    courses = Edu_PE2021_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'PE_NewCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def PE_MidleCatalog(request):
    courses = Edu_PE2018_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'PE_MidleCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def PE_OldCtalog(request):
    courses = Edu_PE_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'PE_OldCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#////SPECIAL EDUCATION TEACHING////#

@login_required
def SET_Catalog(request):
    return render(request, 'SET_Catalog.html')

@login_required
def SET_NewCatalog(request):
    courses = Edu_SET2021_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'SET_NewCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def SET_OldCtalog(request):
    courses = Edu_SET2018_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'SET_OldCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#////GUIDANCE AND PSYCHOLOGICAL COUNSELING////#

@login_required
def GPC_Catalog(request):
    return render(request, 'GPC_Catalog.html')

@login_required
def GPC_NewCatalog(request):
    courses = Edu_GPC2021_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'GPC_NewCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def GPC_MidleCatalog(request):
    courses = Edu_GPC2018_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'GPC_MidleCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def GPC_OldCtalog(request):
    courses = Edu_GPC_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'GPC_OldCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#////TURKISH LANGUANGE TEACHING////#

@login_required
def TLT_Catalog(request):
    return render(request, 'TLT_Catalog.html')

@login_required
def TLT_NewCatalog(request):
    courses = Edu_TLT2021_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'TLT_NewCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def TLT_MidleCatalog(request):
    courses = Edu_TLT2018_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'TLT_MidleCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def TLT_OldCtalog(request):
    courses = Edu_TLT_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'TLT_OldCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#////PEDACOGICAL FORMATION CERTIFICATE PROGRAM////#

@login_required
def PFCP_Catalog(request):
    return render(request, 'PCFP_Main.html')

@login_required
def PharmacyEP_Catalog(request):
    courses = Edu_PFCP_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'PCFP.html', {'courses': courses, 'elective_courses': elective_courses})

#/////////////////////////////////ARTS AND SCIENCES FACULTY//////////////////////////////////////#

@login_required
def Arts_and_Science_Catalog(request):
    return render(request, 'Arts_and_Science_Main.html')

#////ENGLISH////#

@login_required
def PSYE_NewCatalog(request):
    courses = Psycholoy_English_New_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'PSYE_NewCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def PSYE_OldCtalog(request):
    courses = Psycholoy_English_Old_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'PSYE_OldCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#////TURKISH////#

@login_required
def PSYT_NewCatalog(request):
    courses = Psychologyy_Turkish_New_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'PSYT_NewCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def PSYT_OldCtalog(request):
    courses = Psychologyy_Turkish_Old_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'PSYT_OldCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#/////////////////////////////////LAW FACULTY//////////////////////////////////////#

@login_required
def Law_Catalog(request):
    return render(request, 'Law_Main.html')

#////LAW////#

@login_required
def LAW_NewCatalog(request):
    new_courses = Law_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'LAW_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def LAW_OldCatalog(request):
    old_courses = Law_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'LAW_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#////INTERNATIONAL LAW////#

@login_required
def INT_Law_Catalog(request):
    return render(request, 'Law_Main.html')


@login_required
def INTLAW_NewCatalog(request):
    new_courses = Int_Law_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'LAW_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def INTLAW_OldCatalog(request):
    old_courses = Int_Law_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'LAW_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#/////////////////////////////////ECONOMICS AND ADMINISTRATIVE SCIENCE FACULTY//////////////////////////////////////#

#////BUSINESS ADMISTRATION////#

@login_required
def BA_Catalog(request):
    return render(request, 'BA_Main.html')

@login_required
def BA_NewCatalog(request):
    new_courses = BA_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'BA_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def BA_OldCatalog(request):
    old_courses = BA_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'BA_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#////BUSINESS ENTREPRENEURSHIP////#

@login_required
def BE_Main_Catalog(request):
    return render(request, 'BE_Main.html')

@login_required
def BE_Catalog(request):
    courses = BE_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'BA_Catalog.html', {'new_courses': courses, 'new_elective_courses': elective_courses})

#////BUSINESS ADMISTRATION Marketing////#

@login_required
def BAM_Main_Catalog(request):
    return render(request, 'BAM_Main.html')

@login_required
def BAM_Catalog(request):
    courses = BAM_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'BAM_Catalog.html', {'new_courses': courses, 'new_elective_courses': elective_courses})

#////BUSINESS FINANCE AND ACCOUNTING////#

@login_required
def BFA_Catalog(request):
    return render(request, 'BFA_Main.html')

@login_required
def BFA_NewCatalog(request):
    new_courses = BFA_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'BFA_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def BFA_OldCatalog(request):
    old_courses = BFA_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'BFA_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#////ECONOMICS////#

@login_required
def ECO_Main_Catalog(request):
    return render(request, 'ECO_Main.html')

@login_required
def ECO_Catalog(request):
    courses = Econo_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'Eco_Catalog.html', {'courses': courses, 'elective_courses': elective_courses})

#////MARKETING DIGITAL MEDIA////#

@login_required
def MDM_Main_Catalog(request):
    return render(request, 'MDM_Main.html')

@login_required
def MDM_Catalog(request):
    courses = MarkDigM_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'MDM_Catalog.html', {'courses': courses, 'elective_courses': elective_courses})

#////POLITICAL SCIENCE AND INTERNATIONAL RELATION////#

@login_required
def PSIR_Catalog(request):
    return render(request, 'PSIR_Main.html')

@login_required
def PSIR_NewCatalog(request):
    new_courses = PSIR_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'PSIR_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def PSIR_OldCatalog(request):
    old_courses = PSIR_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'PSIR_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#////INTERNATIONAL FINANCE AND BANKING////#

@login_required
def IFB_Catalog(request):
    return render(request, 'IFB_Main.html')

@login_required
def IFB_NewCatalog(request):
    new_courses = IFB_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'IFB_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def IFB_OldCatalog(request):
    old_courses = IFB_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'IFB_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#////INTERNATIONAL TRADE AND BUSINESS////#

@login_required
def ITB_Catalog(request):
    return render(request, 'ITB_Main.html')

@login_required
def ITB_NewCatalog(request):
    new_courses = ITB_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'ITB_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def ITB_OldCatalog(request):
    old_courses = ITB_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'ITB_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#////MANAGEMENT INFORMATION SYSTEM////#

@login_required
def MIS_Catalog(request):
    return render(request, 'MIS_Main.html')

@login_required
def MIS_NewCatalog(request):
    new_courses = MIS_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'MIS_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def MIS_OldCatalog(request):
    old_courses = MIS_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'MIS_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#/////////////////////////////////ARCHITECHTURE AND FINE ARTS FACULTY//////////////////////////////////////#

#////INTERIOR ARCHITECHTURE////#

@login_required
def IntArch_Catalog(request):
    return render(request, 'IntArch_Main.html')

@login_required
def IntArch_NewCatalog(request):
    new_courses = interior_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'IntArch_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def IntArch_OldCatalog(request):
    old_courses = interior_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'IntArch_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#////ARCHITECHTURE////#

@login_required
def ARCHI_MAIN_Catalog(request):
    return render(request, 'archi_Main.html')

@login_required
def ARCHI_NewCatalog(request):
    new_courses = archi_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'archi_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def ARCHi_OldCatalog(request):
    old_courses = archi_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'archi_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#/////////////////////////////////HEALTH SCIENCE FACULTY//////////////////////////////////////#

#////NUTRITION AND DIETETICS////#

@login_required
def nutrition_Main_Catalog(request):
    return render(request, 'nutrition_Main.html')

@login_required
def Nutrition_Catalog(request):
    courses = nutrition_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'nutrition_Catalog.html', {'courses': courses, 'elective_courses': elective_courses})

#////PHYSIOTHERAPY AND REHABILITATION////#

@login_required
def physio_Main_Catalog(request):
    return render(request, 'physio_Main.html')

@login_required
def physio_engl_Catalog(request):
    courses = physiotherapy_engl_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'physio_engl_Catalog.html', {'courses': courses, 'elective_courses': elective_courses})

@login_required
def physio_TNewCatalog(request):
    courses = physiotherapy_turk_new_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'physio_TNew_Catalog.html', {'courses': courses, 'elective_courses': elective_courses})

@login_required
def physio_TOldCatalog(request):
    courses = physiotherapy_turk_old_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'physio_TOld_Catalog.html', {'courses': courses, 'elective_courses': elective_courses})

#////NUrsing////#

@login_required
def Nursing_Main_Catalog(request):
    return render(request, 'nursing_Main.html')

@login_required
def Nursing_Catalog(request):
    courses = nursing_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'nursing_Catalog.html', {'courses': courses, 'elective_courses': elective_courses})


@login_required
@transaction.atomic
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

            course_codes = set(Engineering_Course.objects.values_list('course_code', flat=True) |
                              Dentistry_Course.objects.values_list('course_code', flat=True) |
                              Phamarcy_Course.objects.values_list('course_code', flat=True) |
                              Educational_Sciences_Course.objects.values_list('course_code', flat=True) |
                              Arts_and_Sciences_Course.objects.values_list('course_code', flat=True) |
                              Law_Course.objects.values_list('course_code', flat=True) |
                              Economics_and_Administrative_Sciences_Course.objects.values_list('course_code', flat=True) |
                              Architecture_and_Fine_Arts_Course.objects.values_list('course_code', flat=True) |
                              Health_Sciences_Course.objects.values_list('course_code', flat=True))
            df = df[df['Code'].isin(course_codes)]
                

            # Ensure the DataFrame has the correct columns
            columns = ['Code', 'Title of Course', 'ECTS Credits', 'Grade', 'Credits', 'Gr.Pts']
            df = df.reindex(columns=columns,fill_value='')

            # remove any extra columns
            df = df[columns]
        
            # Update the grades in the Course model      
            for index, row in df.iterrows():
                    code = row['Code']
                    grades = row['Grade']
                    title = row['Title of Course']

                    if Engineering_Course.objects.filter(course_code=code).exists():
                        course, created = Engineering_Course.objects.get_or_create(course_code=code)
                    elif Dentistry_Course.objects.filter(course_code=code).exists():
                        course, created = Dentistry_Course.objects.get_or_create(course_code=code)
                    elif Phamarcy_Course.objects.filter(course_code=code).exists():
                        course, created = Phamarcy_Course.objects.get_or_create(course_code=code)
                    elif Educational_Sciences_Course.objects.filter(course_code=code).exists():
                        course, created = Educational_Sciences_Course.objects.get_or_create(course_code=code)
                    elif Arts_and_Sciences_Course.objects.filter(course_code=code).exists():
                        course, created = Arts_and_Sciences_Course.objects.get_or_create(course_code=code)
                    elif Law_Course.objects.filter(course_code=code).exists():
                        course, created = Law_Course.objects.get_or_create(course_code=code)
                    elif Economics_and_Administrative_Sciences_Course.objects.filter(course_code=code).exists():
                        course, created = Economics_and_Administrative_Sciences_Course.objects.get_or_create(course_code=code)
                    elif Architecture_and_Fine_Arts_Course.objects.filter(course_code=code).exists():
                        course, created = Architecture_and_Fine_Arts_Course.objects.get_or_create(course_code=code)
                    elif Health_Sciences_Course.objects.filter(course_code=code).exists():
                        course, created = Health_Sciences_Course.objects.get_or_create(course_code=code)
                    else:
                        continue

                    print(f"Updating course {course.course_code} with grade {grades}")
                    course.grade = grades
                    course.save()            

                    transcript, created = Transcript.objects.update_or_create(code=code)
                    transcript.grades = grades
                    transcript.save()
            
            return redirect('faculties')
        return df
        
    else:
        form = TranscriptUploadForm()
    return render(request, 'upload_transcript.html', {'form': form})

def process_csv(file: io.BufferedReader) -> pd.DataFrame:
    df = pd.read_csv(file)
    return df

def process_excel(file: io.BufferedReader) -> pd.DataFrame:

    df = pd.read_excel(file)
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