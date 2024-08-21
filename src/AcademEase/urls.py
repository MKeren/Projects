"""
URL configuration for AcademEase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from ease import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('', views.user_login, name='login'),
    path('home/', views.Home, name='home'), 
    path('transcript/', views.StudentTranscriptView, name='transcript'),
    path('upload_transcript/', views.upload_transcript, name='upload_transcript'),
    path('logout/', views.user_logout, name='logout'),
    path('faculties/', views.Faculties, name='faculties'),
    path('switch_language/', views.switch_language, name='switch_language'),
    path('i18n/', include('django.conf.urls.i18n')),
    

    path('computer_catalog/', views.Comp_Catalog, name='computer_catalog'),
    path('comp_old_catalog/', views.Comp_OldCatalog, name='comp_old_catalog'),
    path('comp_new_catalog/', views.Comp_NewCatalog, name='comp_new_catalog'),

    path('software_catalog/', views.Soft_Catalog, name='software_catalog'),
    path('soft_old_catalog/', views.Soft_OldCatalog, name='soft_old_catalog'),
    path('soft_new_catalog/', views.Soft_NewCatalog, name='soft_new_catalog'),

    path('electrical_catalog/', views.EE_Catalog, name='electrical_catalog'),
    path('elec_old_catalog/', views.EE_Oldcatalog, name='elec_old_catalog'),
    path('elec_new_catalog/', views.EE_NewCatalog, name='elec_new_catalog'),

    path('civil_catalog/', views.Civil_Catalog, name='civil_catalog'),
    path('civil_old_catalog/', views.Civil_OldCatalog, name='civil_old_catalog'),
    path('civil_new_catalog/', views.Civil_NewCatalog, name='civil_new_catalog'),

    path('AI_catalog/', views.AI_catalog, name='AI_catalog'),
    path('ai_catalog/', views.AI_Curriculum, name='ai_catalog'),

    path('dentistryE_catalog/', views.DentistryE_Catalog, name='dentistryE_catalog'),
    path('dentE_catalog/', views.dentistryE_Catalog, name='dentE_catalog'),
    path('dentistryT_catalog/', views.DentistryT_Catalog, name='dentistryT_catalog'),
    path('dentT_catalog/', views.dentistryT_Catalog, name='dentT_catalog'),

    path('pharmacyE_catalog/', views.PharmacyE_Catalog, name='pharmacyE_catalog'),
    path('pharmacyEM_catalog/', views.PharmacyEM_Catalog, name='pharmacyEM_catalog'),
    path('pharmacyEP_catalog/', views.PharmacyEP_Catalog, name='pharmacyEP_catalog'),

    path('pharmacyTM_catalog/', views.PharmacyTM_Catalog, name='pharmacyTM_catalog'),
    path('pharmacyT_catalog/', views.PharmacyT_Catalog, name='pharmacyT_catalog'),
    

    path('ELT_catalog/', views.ELT_Catalog, name='ELT_catalog'),
    path('ELTN_catalog/', views.ELT_NewCatalog, name='ELTN_catalog'),
    path('ELTM_catalog/', views.ELT_MidleCatalog, name='ELTM_catalog'),
    path('ELTO_catalog/', views.ELT_OldCtalog, name='ELTO_catalog'),

    path('PE_catalog/', views.PE_Catalog, name='PE_catalog'),
    path('PEN_catalog/', views.PE_NewCatalog, name='PEN_catalog'),
    path('PEM_catalog/', views.PE_MidleCatalog, name='PEM_catalog'),
    path('PEO_catalog/', views.PE_OldCtalog, name='PEO_catalog'),

    path('SET_catalog/', views.SET_Catalog, name='SET_catalog'),
    path('SETN_catalog/', views.SET_NewCatalog, name='SETN_catalog'),
    path('SETO_catalog/', views.SET_OldCtalog, name='SETO_catalog'),

    path('GPC_catalog/', views.GPC_Catalog, name='GPC_catalog'),
    path('GPCN_catalog/', views.GPC_NewCatalog, name='GPCN_catalog'),
    path('GPCM_catalog/', views.GPC_MidleCatalog, name='GPCM_catalog'),
    path('GPCO_catalog/', views.GPC_OldCatalog, name='GPCO_catalog'),

    path('TLT_catalog/', views.TLT_Catalog, name='TLT_catalog'),
    path('TLTN_catalog/', views.TLT_NewCatalog, name='TLTN_catalog'),
    path('TLTM_catalog/', views.TLT_MidleCatalog, name='TLTM_catalog'),
    path('TLTO_catalog/', views.TLT_OldCtalog, name='TLTO_catalog'),

    path('PFCP_main_catalog/', views.PFCP_Catalog, name='PFCP_main_catalog'),
    path('PFCP_catalog/', views.PFCP_Curriculum, name='PFCP_catalog'),

    path('PSYE_catalog/', views.PSYE_Catalog, name='PSYE_catalog'),
    path('PSYEN_catalog/', views.PSYE_NewCatalog, name='PSYEN_catalog'),
    path('PSYEO_catalog/', views.PSYE_OldCatalog, name='PSYEO_catalog'),
    
    path('PSYT_catalog/', views.PSYT_Catalog, name='PSYT_catalog'),
    path('PSYTN_catalog/', views.PSYT_NewCatalog, name='PSYTN_catalog'),
    path('PSYTO_catalog/', views.PSYT_OldCatalog, name='PSYTO_catalog'),

    path('LAW_catalog/', views.Law_Catalog, name='LAW_catalog'),
    path('LAWN_catalog/', views.LAW_NewCatalog, name='LAWN_catalog'),
    path('LAWO_catalog/', views.LAW_OldCatalog, name='LAWO_catalog'),

    path('INTLAW_catalog/', views.INTLaw_Catalog, name='INTLAW_catalog'),
    path('INTLAWN_catalog/', views.INTLAW_NewCatalog, name='INTLAWN_catalog'),
    path('INTLAWO_catalog/', views.INTLAW_OldCatalog, name='INTLAWO_catalog'),

    path('BA_catalog/', views.BA_Catalog, name='BA_catalog'),
    path('BAN_catalog/', views.BA_NewCatalog, name='BAN_catalog'),
    path('BAO_catalog/', views.BA_OldCatalog, name='BAO_catalog'),

    path('BE_catalog/', views.BE_Main_Catalog, name='BE_catalog'),
    path('be_catalog/', views.BE_Catalog, name='be_catalog'),

    path('BAM_catalog/', views.BAM_Main_Catalog, name='BAM_catalog'),
    path('bam_catalog/', views.BAM_Catalog, name='bam_catalog'),

    path('BFA_catalog/', views.BFA_Catalog, name='BFA_catalog'),
    path('BFAN_catalog/', views.BFA_NewCatalog, name='BFAN_catalog'),
    path('BFAO_catalog/', views.BFA_OldCatalog, name='BFAO_catalog'),

    path('ECO_catalog/', views.ECO_Main_Catalog, name='ECO_catalog'),
    path('eco_catalog/', views.ECO_Catalog, name='eco_catalog'),

    path('MDM_catalog/', views.MDM_Main_Catalog, name='MDM_catalog'),
    path('mdm_catalog/', views.MDM_Catalog, name='mdm_catalog'),

    path('PSIR_catalog/', views.PSIR_Catalog, name='PSIR_catalog'),
    path('PSIRN_catalog/', views.PSIR_NewCatalog, name='PSIRN_catalog'),
    path('PSIRO_catalog/', views.PSIR_OldCatalog, name='PSIRO_catalog'),

    path('IFB_catalog/', views.IFB_Catalog, name='IFB_catalog'),
    path('IFBN_catalog/', views.IFB_NewCatalog, name='IFBN_catalog'),
    path('IFBO_catalog/', views.IFB_OldCatalog, name='IFBO_catalog'),

    path('ITB_catalog/', views.ITB_Catalog, name='ITB_catalog'),
    path('ITBN_catalog/', views.ITB_NewCatalog, name='ITBN_catalog'),
    path('ITBO_catalog/', views.ITB_OldCatalog, name='ITBO_catalog'),

    path('MIS_catalog/', views.MIS_Catalog, name='MIS_catalog'),
    path('MISN_catalog/', views.MIS_NewCatalog, name='MISN_catalog'),
    path('MISO_catalog/', views.MIS_OldCatalog, name='MISO_catalog'),

    path('IA_catalog/', views.IntArch_Catalog, name='IA_catalog'),
    path('IAN_catalog/', views.IntArch_NewCatalog, name='IAN_catalog'),
    path('IAO_catalog/', views.IntArch_OldCatalog, name='IAO_catalog'),

    path('ARCH_catalog/', views.ARCHI_MAIN_Catalog, name='ARCH_catalog'),
    path('ARCHN_catalog/', views.ARCHI_NewCatalog, name='ARCHN_catalog'),
    path('ARCHO_catalog/', views.ARCHI_OldCatalog, name='ARCHO_catalog'),

    path('NUTRI_catalog/', views.Nutrition_Main_Catalog, name='NUTRI_catalog'),
    path('nutri_catalog/', views.Nutrition_Catalog, name='nutri_catalog'),
    
    path('PHYSIOE_catalog/', views.physioE_Main_Catalog, name='PHYSIOE_catalog'),
    path('physioe_catalog/', views.physio_engl_Catalog, name='physioe_catalog'),
    path('PHYSIOT_catalog/', views.physioT_Main_Catalog, name='PHYSIOT_catalog'),
    path('PHYSIOTN_catalog/', views.physio_TNewCatalog, name='PHYSIOTN_catalog'),
    path('PHYSIOTO_catalog/', views.physio_TOldCatalog, name='PHYSIOTO_catalog'),

    path('NURSE_catalog/', views.Nursing_Main_Catalog, name='NURSE_catalog'),
    path('nurse_catalog/', views.Nursing_Catalog, name='nurse_catalog'),

]
