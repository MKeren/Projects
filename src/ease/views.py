import io
import PyPDF2
import docx
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from AcademEase import settings
from ease.forms import TranscriptUploadForm
from ease.models import AI_Catalog, Architecture_and_Fine_Arts_Course, AreaTechnicalElectiveCourse, Arts_and_Sciences_Course, BA_New_catalog, BA_Old_catalog, BAM_catalog, BE_catalog, BFA_New_catalog, BFA_Old_catalog, Civil_Newcatalog, Dent_English_catalog, Dent_Turkish_catalog, EE_Newcatalog, EE_OldCatalog, Econo_catalog, Economics_and_Administrative_Sciences_Course, Edu_ELT2018_catalog, Edu_ELT2021_catalog, Edu_ELT_catalog, Edu_GPC2018_catalog, Edu_GPC2021_catalog, Edu_GPC_catalog, Edu_PE2018_catalog, Edu_PE2021_catalog, Edu_PE_catalog, Edu_PFCP_catalog, Edu_SET2018_catalog, Edu_SET2021_catalog, Edu_TLT2018_catalog, Edu_TLT2021_catalog, Edu_TLT_catalog, Educational_Sciences_Course, Engineering_Course, Computer_Newcatalog,Computer_OldCatalog, Faculty, Health_Sciences_Course, IFB_New_catalog, IFB_Old_catalog, ITB_New_catalog, ITB_Old_catalog, Int_Law_New_catalog, Int_Law_Old_catalog, Law_Course, Law_New_catalog, Law_Old_catalog, MIS_New_catalog, MIS_Old_catalog, MarkDigM_catalog, PSIR_New_catalog, PSIR_Old_catalog,Phamarcy_Course,Dentistry_Course, Pharmay_English_Mpharm_catalog, Pharmay_English_PharmD_catalog, Pharmay_Turkish_English_PharmD_catalog, Pharmay_Turkish_catalog, Psychologyy_Turkish_New_catalog, Psychologyy_Turkish_Old_catalog, Psycholoy_English_New_catalog, Psycholoy_English_Old_catalog, Software_Newcatalog, Software_Oldcatalog,Transcript, archi_New_catalog, archi_Old_catalog, civil_OldCatalog, interior_New_catalog, interior_Old_catalog, nursing_catalog, nutrition_catalog, physiotherapy_engl_catalog, physiotherapy_turk_new_catalog, physiotherapy_turk_old_catalog
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.utils.translation import gettext as _
from django.utils.translation import activate

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
    AreaTechnicalElectiveCourse.objects.all().update(grade=None)
    Transcript.objects.all().delete()
    

    logout(request)
    return redirect('login')

@login_required
def Home(request):
    return render(request, 'home.html')

def switch_language(request):
    print(request.GET) 
    lang = request.GET.get('lang','')
    next_url = request.GET.get('next','/')
    activate(lang)
    response = redirect(next_url)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    return response

@login_required
def StudentTranscriptView(request):
    transcripts = Transcript.objects.all()  
    return render(request, 'transcript.html',{'transcripts': transcripts})

@login_required
def Faculties(request):
    return render(request, 'faculties.html')

#/////////////////////////////////ENGINEERING FACULTY//////////////////////////////////////#

#//////COMPUTER/////#

@login_required
def Comp_Catalog(request):
    return render(request, 'engeeningfac\comp\Comp_Catalog.html')

@login_required
def Comp_NewCatalog(request):
    new_courses = Computer_Newcatalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    new_technical_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'engeeningfac\comp\Comp_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses, 'new_technical_courses': new_technical_courses})

@login_required
def Comp_OldCatalog(request):
    old_courses = Computer_OldCatalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'engeeningfac\comp\Comp_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#//////SOFTWARE/////#

login_required
def Soft_Catalog(request):
    return render(request, 'engeeningfac\soft\Soft_Catalog.html')

@login_required
def Soft_NewCatalog(request):
    new_courses = Software_Newcatalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'engeeningfac\soft\Soft_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def Soft_OldCatalog(request):
    old_courses = Software_Oldcatalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'engeeningfac\soft\Soft_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#//////CIVIL/////#

login_required
def Civil_Catalog(request):
    return render(request, 'engeeningfac\civil\Civil_Catalog.html')

@login_required
def Civil_NewCatalog(request):
    new_courses = Civil_Newcatalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'engeeningfac\civil\Civil_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def Civil_OldCatalog(request):
    old_courses = civil_OldCatalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'engeeningfac\civil\Civil_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#//////ARTIFICIAL INTELLIGENCE/////#

@login_required
def AI_catalog(request):
    return render(request, 'engeeningfac\\ai\AI_Main.html')

@login_required
def AI_Curriculum(request):
    courses = AI_Catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'engeeningfac\\ai\AI_Catalog.html', {'courses': courses, 'elective_courses': elective_courses})

#//////ELECTRICAL AND ELECTRONICS/////#

@login_required
def EE_Catalog(request):
    return render(request, 'engeeningfac\elec\EE_Catalog.html')

@login_required
def EE_NewCatalog(request):
    new_courses = EE_Newcatalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'engeeningfac\elec\EE_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def EE_Oldcatalog(request):
    old_courses = EE_OldCatalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'engeeningfac\elec\EE_OldCatalog.html', {'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#/////////////////////////////////DENTISTRY FACULTY//////////////////////////////////////#

#////ENGLISH////#

@login_required
def DentistryE_Catalog(request):
    return render(request, 'dentistryfac\DentistryE_Main.html')

@login_required
def dentistryE_Catalog(request):
    courses = Dent_English_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'dentistryfac\DentE.html', {'courses': courses, 'elective_courses': elective_courses})

#////TURKISH////#

@login_required
def DentistryT_Catalog(request):
    return render(request, 'dentistryfac\DentistryT_Main.html')


def dentistryT_Catalog(request):
    courses = Dent_Turkish_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'dentistryfac\DentT.html', {'courses': courses, 'elective_courses': elective_courses})

#/////////////////////////////////PHARMACY FACULTY//////////////////////////////////////#

#////ENGLISH////#

@login_required
def PharmacyE_Catalog(request):
    return render(request, 'pharmacyfac\PharmacyE_Main.html')

@login_required
def PharmacyEP_Catalog(request):
    courses = Pharmay_English_PharmD_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'pharmacyfac\PharmEP.html', {'courses': courses, 'elective_courses': elective_courses})

@login_required
def PharmacyEM_Catalog(request):
    courses = Pharmay_English_Mpharm_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'pharmacyfac\PharmEM.html', {'courses': courses, 'elective_courses': elective_courses})

#////TURKISH////#

@login_required
def PharmacyTM_Catalog(request):
    return render(request, 'pharmacyfac\PharmacyTM_Main.html')

@login_required
def PharmacyT_Catalog(request):
    courses = Pharmay_Turkish_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'pharmacyfac\PharmT.html', {'courses': courses, 'elective_courses': elective_courses})

#/////////////////////////////////EDUCATIONAL SCIENCES FACULTY//////////////////////////////////////#

#////ENGLISH LANGUAGE TEACHING////#

@login_required
def ELT_Catalog(request):
    return render(request, 'educational_Scfac\ENGLISH LANGUANGE TEACHING\ELT_Catalog.html')

@login_required
def ELT_NewCatalog(request):
    courses = Edu_ELT2021_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'educational_Scfac\ENGLISH LANGUANGE TEACHING\ELT_NewCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def ELT_MidleCatalog(request):
    courses = Edu_ELT2018_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'educational_Scfac\ENGLISH LANGUANGE TEACHING\ELT_MidleCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def ELT_OldCtalog(request):
    courses = Edu_ELT_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'educational_Scfac\ENGLISH LANGUANGE TEACHING\ELT_OldCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#////PRESCHOOL EDUCATION////#

@login_required
def PE_Catalog(request):
    return render(request, 'educational_Scfac\PRESCHOOL EDUCATION\PE_Catalog.html')

@login_required
def PE_NewCatalog(request):
    courses = Edu_PE2021_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'educational_Scfac\PRESCHOOL EDUCATION\PE_NewCatalog.html', {'new_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def PE_MidleCatalog(request):
    courses = Edu_PE2018_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'educational_Scfac\PRESCHOOL EDUCATION\PE_MidleCatalog.html', {'midle_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def PE_OldCtalog(request):
    courses = Edu_PE_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'educational_Scfac\PRESCHOOL EDUCATION\PE_OldCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#////SPECIAL EDUCATION TEACHING////#

@login_required
def SET_Catalog(request):
    return render(request, 'educational_Scfac\SPECIAL EDUCATION TEACHING\SET_Catalog.html')

@login_required
def SET_NewCatalog(request):
    courses = Edu_SET2021_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'educational_Scfac\SPECIAL EDUCATION TEACHING\SET_NewCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def SET_OldCtalog(request):
    courses = Edu_SET2018_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'educational_Scfac\SPECIAL EDUCATION TEACHING\SET_OldCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#////GUIDANCE AND PSYCHOLOGICAL COUNSELING////#

@login_required
def GPC_Catalog(request):
    return render(request, 'educational_Scfac\GUIDANCE AND PSYCHOLOGICAL COUNSELING\GPC_Catalog.html')

@login_required
def GPC_NewCatalog(request):
    courses = Edu_GPC2021_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'educational_Scfac\GUIDANCE AND PSYCHOLOGICAL COUNSELING\GPC_NewCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def GPC_MidleCatalog(request):
    courses = Edu_GPC2018_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'educational_Scfac\GUIDANCE AND PSYCHOLOGICAL COUNSELING\GPC_MidleCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def GPC_OldCatalog(request):
    courses = Edu_GPC_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'educational_Scfac\GUIDANCE AND PSYCHOLOGICAL COUNSELING\GPC_OldCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#////TURKISH LANGUANGE TEACHING////#

@login_required
def TLT_Catalog(request):
    return render(request, 'educational_Scfac\TURKISH LANGUANGE TEACHING\TLT_Catalog.html')

@login_required
def TLT_NewCatalog(request):
    courses = Edu_TLT2021_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'educational_Scfac\TURKISH LANGUANGE TEACHING\TLT_NewCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def TLT_MidleCatalog(request):
    courses = Edu_TLT2018_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'educational_Scfac\TURKISH LANGUANGE TEACHING\TLT_MidleCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def TLT_OldCtalog(request):
    courses = Edu_TLT_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'educational_Scfac\TURKISH LANGUANGE TEACHING\TLT_OldCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#////PEDACOGICAL FORMATION CERTIFICATE PROGRAM////#

@login_required
def PFCP_Catalog(request):
    return render(request, 'educational_Scfac/PEDACOGICAL FORMATION CERTIFICATE PROGRAM/PFCP_Main.html')

@login_required
def PFCP_Curriculum(request):
    courses = Edu_PFCP_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'educational_Scfac/PEDACOGICAL FORMATION CERTIFICATE PROGRAM/PFCP.html', {'courses': courses, 'elective_courses': elective_courses})

#/////////////////////////////////ARTS AND SCIENCES FACULTY//////////////////////////////////////#

#////ENGLISH////#

@login_required
def PSYE_Catalog(request):
    return render(request, 'arts_and_Scfac\PSYE.html')

@login_required
def PSYE_NewCatalog(request):
    courses = Psycholoy_English_New_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'arts_and_Scfac\PSYE_NewCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def PSYE_OldCatalog(request):
    courses = Psycholoy_English_Old_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'arts_and_Scfac\PSYE_OldCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#////TURKISH////#

@login_required
def PSYT_Catalog(request):
    return render(request, 'arts_and_Scfac\PSYT.html')

@login_required
def PSYT_NewCatalog(request):
    courses = Psychologyy_Turkish_New_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'arts_and_Scfac\PSYT_NewCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

@login_required
def PSYT_OldCatalog(request):
    courses = Psychologyy_Turkish_Old_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'arts_and_Scfac\PSYT_OldCatalog.html', {'old_courses': courses, 'old_elective_courses': elective_courses})

#/////////////////////////////////LAW FACULTY//////////////////////////////////////#

#////LAW////#

@login_required
def Law_Catalog(request):
    return render(request, 'lawfac\LAW\Law_Main.html')

@login_required
def LAW_NewCatalog(request):
    new_courses = Law_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'lawfac\LAW\LAW_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def LAW_OldCatalog(request):
    old_courses = Law_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'lawfac\LAW\LAW_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#////INTERNATIONAL LAW////#

@login_required
def INTLaw_Catalog(request):
    return render(request, 'lawfac\INTERNATIONAL LAW\intLaw_Main.html')

@login_required
def INTLAW_NewCatalog(request):
    new_courses = Int_Law_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'lawfac\INTERNATIONAL LAW\intLAW_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def INTLAW_OldCatalog(request):
    old_courses = Int_Law_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'lawfac\INTERNATIONAL LAW\intLAW_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#/////////////////////////////////ECONOMICS AND ADMINISTRATIVE SCIENCE FACULTY//////////////////////////////////////#

#////BUSINESS ADMISTRATION////#

@login_required
def BA_Catalog(request):
    return render(request, 'economicfac\BUSINESS ADMISTRATION\BA_Main.html')

@login_required
def BA_NewCatalog(request):
    new_courses = BA_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'economicfac\BUSINESS ADMISTRATION\BA_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def BA_OldCatalog(request):
    old_courses = BA_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'economicfac\BUSINESS ADMISTRATION\BA_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#////BUSINESS ENTREPRENEURSHIP////#

@login_required
def BE_Main_Catalog(request):
    return render(request, 'economicfac\BUSINESS ENTREPRENEURSHIP\BE_Main.html')

@login_required
def BE_Catalog(request):
    courses = BE_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'economicfac\BUSINESS ENTREPRENEURSHIP\BE_Catalog.html', {'new_courses': courses, 'new_elective_courses': elective_courses})

#////BUSINESS ADMISTRATION Marketing////#

@login_required
def BAM_Main_Catalog(request):
    return render(request, 'economicfac\BUSINESS ADMISTRATION Marketing\BAM_Main.html')

@login_required
def BAM_Catalog(request):
    courses = BAM_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'economicfac\BUSINESS ADMISTRATION Marketing\BAM_Catalog.html', {'new_courses': courses, 'new_elective_courses': elective_courses})

#////BUSINESS FINANCE AND ACCOUNTING////#

@login_required
def BFA_Catalog(request):
    return render(request, 'economicfac\BUSINESS FINANCE AND ACCOUNTING\BFA_Main.html')

@login_required
def BFA_NewCatalog(request):
    new_courses = BFA_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'economicfac\BUSINESS FINANCE AND ACCOUNTING\BFA_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def BFA_OldCatalog(request):
    old_courses = BFA_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'economicfac\BUSINESS FINANCE AND ACCOUNTING\BFA_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#////ECONOMICS////#

@login_required
def ECO_Main_Catalog(request):
    return render(request, 'economicfac\ECONOMICS\ECO_Main.html')

@login_required
def ECO_Catalog(request):
    courses = Econo_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'economicfac\ECONOMICS\Eco_Catalog.html', {'courses': courses, 'elective_courses': elective_courses})

#////MARKETING DIGITAL MEDIA////#

@login_required
def MDM_Main_Catalog(request):
    return render(request, 'economicfac\MARKETING DIGITAL MEDIA\MDM_Main.html')

@login_required
def MDM_Catalog(request):
    courses = MarkDigM_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'economicfac\MARKETING DIGITAL MEDIA\MDM_Catalog.html', {'courses': courses, 'elective_courses': elective_courses})

#////POLITICAL SCIENCE AND INTERNATIONAL RELATION////#

@login_required
def PSIR_Catalog(request):
    return render(request, 'economicfac\POLITICAL SCIENCE AND INTERNATIONAL RELATION\PSIR_Main.html')

@login_required
def PSIR_NewCatalog(request):
    new_courses = PSIR_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'economicfac\POLITICAL SCIENCE AND INTERNATIONAL RELATION\PSIR_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def PSIR_OldCatalog(request):
    old_courses = PSIR_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'economicfac\POLITICAL SCIENCE AND INTERNATIONAL RELATION\PSIR_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#////INTERNATIONAL FINANCE AND BANKING////#

@login_required
def IFB_Catalog(request):
    return render(request, 'economicfac\INTERNATIONAL FINANCE AND BANKING\IFB_Main.html')

@login_required
def IFB_NewCatalog(request):
    new_courses = IFB_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'economicfac\INTERNATIONAL FINANCE AND BANKING\IFB_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def IFB_OldCatalog(request):
    old_courses = IFB_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'economicfac\INTERNATIONAL FINANCE AND BANKING\IFB_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#////INTERNATIONAL TRADE AND BUSINESS////#

@login_required
def ITB_Catalog(request):
    return render(request, 'economicfac\INTERNATIONAL TRADE AND BUSINESS\ITB_Main.html')

@login_required
def ITB_NewCatalog(request):
    new_courses = ITB_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'economicfac\INTERNATIONAL TRADE AND BUSINESS\ITB_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def ITB_OldCatalog(request):
    old_courses = ITB_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'economicfac\INTERNATIONAL TRADE AND BUSINESS\ITB_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#////MANAGEMENT INFORMATION SYSTEM////#

@login_required
def MIS_Catalog(request):
    return render(request, 'economicfac\MANAGEMENT INFORMATION SYSTEM\MIS_Main.html')

@login_required
def MIS_NewCatalog(request):
    new_courses = MIS_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'economicfac\MANAGEMENT INFORMATION SYSTEM\MIS_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def MIS_OldCatalog(request):
    old_courses = MIS_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'economicfac\MANAGEMENT INFORMATION SYSTEM\MIS_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#/////////////////////////////////ARCHITECHTURE AND FINE ARTS FACULTY//////////////////////////////////////#

#////INTERIOR ARCHITECHTURE////#

@login_required
def IntArch_Catalog(request):
    return render(request, 'architecturefac\INTERIOR ARCHITECHTURE\IntArch_Main.html')

@login_required
def IntArch_NewCatalog(request):
    new_courses = interior_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'architecturefac\INTERIOR ARCHITECHTURE\IntArch_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def IntArch_OldCatalog(request):
    old_courses = interior_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'architecturefac\INTERIOR ARCHITECHTURE\IntArch_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#////ARCHITECHTURE////#

@login_required
def ARCHI_MAIN_Catalog(request):
    return render(request, 'architecturefac\ARCHITECHTURE\\archi_Main.html')

@login_required
def ARCHI_NewCatalog(request):
    new_courses = archi_New_catalog.objects.all()
    new_elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'architecturefac\ARCHITECHTURE\\archi_NewCatalog.html', {'new_courses': new_courses, 'new_elective_courses': new_elective_courses})

@login_required
def ARCHI_OldCatalog(request):
    old_courses = archi_Old_catalog.objects.all()
    old_elective_courses = AreaTechnicalElectiveCourse.objects.all()
    return render(request, 'architecturefac\ARCHITECHTURE\\archi_OldCatalog.html',{'old_courses': old_courses, 'old_elective_courses': old_elective_courses})

#/////////////////////////////////HEALTH SCIENCE FACULTY//////////////////////////////////////#

#////NUTRITION AND DIETETICS////#

@login_required
def Nutrition_Main_Catalog(request):
    return render(request, 'health_Scfac\\nUTRITION AND DIETETICS\\nutrition_Main.html')

@login_required
def Nutrition_Catalog(request):
    courses = nutrition_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'health_Scfac\\nUTRITION AND DIETETICS\\nutrition_Catalog.html', {'courses': courses, 'elective_courses': elective_courses})

#////PHYSIOTHERAPY AND REHABILITATION////#

@login_required
def physioE_Main_Catalog(request):
    return render(request, 'health_Scfac\PHYSIOTHERAPY AND REHABILITATION\physioE_Main.html')

@login_required
def physio_engl_Catalog(request):
    courses = physiotherapy_engl_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'health_Scfac\PHYSIOTHERAPY AND REHABILITATION\physio_engl_Catalog.html', {'courses': courses, 'elective_courses': elective_courses})

@login_required
def physioT_Main_Catalog(request):
    return render(request, 'health_Scfac\PHYSIOTHERAPY AND REHABILITATION\physioT_Main.html')

@login_required
def physio_TNewCatalog(request):
    courses = physiotherapy_turk_new_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'health_Scfac\PHYSIOTHERAPY AND REHABILITATION\physio_TNew_Catalog.html', {'courses': courses, 'elective_courses': elective_courses})

@login_required
def physio_TOldCatalog(request):
    courses = physiotherapy_turk_old_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'health_Scfac\PHYSIOTHERAPY AND REHABILITATION\physio_TOld_Catalog.html', {'courses': courses, 'elective_courses': elective_courses})

#////NUrsing////#

@login_required
def Nursing_Main_Catalog(request):
    return render(request, 'health_Scfac\\NUrsing\\nursing_Main.html')

@login_required
def Nursing_Catalog(request):
    courses = nursing_catalog.objects.all()
    elective_courses = AreaTechnicalElectiveCourse.objects.all
    return render(request, 'health_Scfac\\NUrsing\\nursing_Catalog.html', {'courses': courses, 'elective_courses': elective_courses})

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
                        
                        elective, created = AreaTechnicalElectiveCourse.objects.update_or_create(course_code=code, defaults={'grade': grade},title=title,ects_credit=ects_credit)
                        if not created:
                            elective.grade = grade
                            elective.save()
                
     
            return redirect('faculties')

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

    #def process_txt(file):
    #return pd.read_csv(file, delimiter="\t")

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
                data['Title of Course'].append(' '.join(fields[0:-5]))
                data['ECTS Credits'].append(fields[-3])
                data['Grade'].append(fields[-4])
                data['Credits'].append(fields[-2])
                data['Gr.Pts'].append(fields[-1])          
    
    df = pd.DataFrame(data)
    print("Processed DataFrame from text data:", df)
    return df
