from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Engineering_Course(models.Model):
    semester = models.CharField(max_length=255,null=True, blank=True)
    course_code = models.CharField(max_length=255,null=True, blank=True)
    title = models.CharField(max_length=255,null=True, blank=True)
    category = models.CharField(max_length=255,null=True, blank=True)
    hours_lecture = models.IntegerField(null=True, blank=True)
    hours_tutorial = models.IntegerField(null=True, blank=True)
    hours_lab = models.IntegerField(null=True, blank=True)
    pre_requisite = models.TextField(null=True, blank=True)
    ects_credit = models.CharField(max_length=255,null=True, blank=True)
    total_credits = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.course_code
    
class Computer_OldCatalog(Engineering_Course):
    pass
class Computer_Newcatalog(Engineering_Course):
    pass
class civil_OldCatalog(Engineering_Course):
    pass
class Civil_Newcatalog(Engineering_Course):
    pass
class EE_OldCatalog(Engineering_Course):
    pass
class EE_Newcatalog(Engineering_Course):
    pass
class AI_Catalog(Engineering_Course):
    pass
class Software_Newcatalog(Engineering_Course):
    pass
class Software_Oldcatalog(Engineering_Course):
    pass

class Dentistry_Course(models.Model):
    semester = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    hours_lecture = models.IntegerField(null=True, blank=True)
    hours_tutorial = models.IntegerField(null=True, blank=True)
    hours_lab = models.IntegerField(null=True, blank=True)
    pre_requisite = models.TextField(null=True, blank=True)
    ects_credit = models.CharField(max_length=255,null=True, blank=True)
    total_credits = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.course_code
class Dent_English_catalog(Dentistry_Course):
    pass
class Dent_Turkish_catalog(Dentistry_Course):
    pass

class Phamarcy_Course(models.Model):
    semester = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    hours_lecture = models.IntegerField(null=True, blank=True)
    hours_tutorial = models.IntegerField(null=True, blank=True)
    hours_lab = models.IntegerField(null=True, blank=True)
    pre_requisite = models.TextField(null=True, blank=True)
    ects_credit = models.CharField(max_length=255,null=True, blank=True)
    total_credits = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=255)

    def __str__(self):
        return self.course_code
class Pharmay_English_Mpharm_catalog(Phamarcy_Course):
    pass
class Pharmay_English_PharmD_catalog(Phamarcy_Course):
    pass
class Pharmay_Turkish_catalog(Phamarcy_Course):
    pass
class Pharmay_Turkish_English_PharmD_catalog(Phamarcy_Course):
    pass

class Educational_Sciences_Course(models.Model):
    semester = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    hours_lecture = models.IntegerField(null=True, blank=True)
    hours_tutorial = models.IntegerField(null=True, blank=True)
    hours_lab = models.IntegerField(null=True, blank=True)
    pre_requisite = models.TextField(null=True, blank=True)
    ects_credit = models.CharField(max_length=255,null=True, blank=True)
    total_credits = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.course_code
class Edu_ELT2021_catalog(Educational_Sciences_Course):
    pass
class Edu_ELT2018_catalog(Educational_Sciences_Course):
    pass
class Edu_ELT_catalog(Educational_Sciences_Course):
    pass
class Edu_SET2021_catalog(Educational_Sciences_Course):
    pass
class Edu_SET2018_catalog(Educational_Sciences_Course):
    pass
class Edu_PE2021_catalog(Educational_Sciences_Course):
    pass
class Edu_PE2018_catalog(Educational_Sciences_Course):
    pass
class Edu_PE_catalog(Educational_Sciences_Course):
    pass
class Edu_GPC2021_catalog(Educational_Sciences_Course):
    pass
class Edu_GPC2018_catalog(Educational_Sciences_Course):
    pass
class Edu_GPC_catalog(Educational_Sciences_Course):
    pass
class Edu_TLT2021_catalog(Educational_Sciences_Course):
    pass
class Edu_TLT2018_catalog(Educational_Sciences_Course):
    pass
class Edu_TLT_catalog(Educational_Sciences_Course):
    pass
class Edu_PFCP_catalog(Educational_Sciences_Course):
    pass

class Arts_and_Sciences_Course(models.Model):
    semester = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    hours_lecture = models.IntegerField(null=True, blank=True)
    hours_tutorial = models.IntegerField(null=True, blank=True)
    hours_lab = models.IntegerField(null=True, blank=True)
    pre_requisite = models.TextField(null=True, blank=True)
    ects_credit = models.CharField(max_length=255,null=True, blank=True)
    total_credits = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.course_code
class Psycholoy_English_New_catalog(Arts_and_Sciences_Course):
    pass
class Psycholoy_English_Old_catalog(Arts_and_Sciences_Course):
    pass
class Psychologyy_Turkish_New_catalog(Arts_and_Sciences_Course):
    pass
class Psychologyy_Turkish_Old_catalog(Arts_and_Sciences_Course):
    pass

class Law_Course(models.Model):
    semester = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    hours_lecture = models.IntegerField(null=True, blank=True)
    hours_tutorial = models.IntegerField(null=True, blank=True)
    hours_lab = models.IntegerField(null=True, blank=True)
    pre_requisite = models.TextField(null=True, blank=True)
    ects_credit = models.CharField(max_length=255,null=True, blank=True)
    total_credits = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.course_code
class Law_New_catalog(Law_Course):
    pass
class Law_Old_catalog(Law_Course):
    pass
class Int_Law_New_catalog(Law_Course):
    pass
class Int_Law_Old_catalog(Law_Course):
    pass

class Economics_and_Administrative_Sciences_Course(models.Model):
    semester = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    hours_lecture = models.IntegerField(null=True, blank=True)
    hours_tutorial = models.IntegerField(null=True, blank=True)
    hours_lab = models.IntegerField(null=True, blank=True)
    pre_requisite = models.TextField(null=True, blank=True)
    ects_credit = models.CharField(max_length=255,null=True, blank=True)
    total_credits = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.course_code
class BA_New_catalog(Economics_and_Administrative_Sciences_Course):
    pass
class BA_Old_catalog(Economics_and_Administrative_Sciences_Course):
    pass
class BE_catalog(Economics_and_Administrative_Sciences_Course):
    pass
class BAM_catalog(Economics_and_Administrative_Sciences_Course):
    pass
class BFA_New_catalog(Economics_and_Administrative_Sciences_Course):
    pass
class BFA_Old_catalog(Economics_and_Administrative_Sciences_Course):
    pass
class Econo_catalog(Economics_and_Administrative_Sciences_Course):
    pass
class MarkDigM_catalog(Economics_and_Administrative_Sciences_Course):
    pass
class PSIR_New_catalog(Economics_and_Administrative_Sciences_Course):
    pass
class PSIR_Old_catalog(Economics_and_Administrative_Sciences_Course):
    pass
class IFB_New_catalog(Economics_and_Administrative_Sciences_Course):
    pass
class IFB_Old_catalog(Economics_and_Administrative_Sciences_Course):
    pass
class ITB_New_catalog(Economics_and_Administrative_Sciences_Course):
    pass
class ITB_Old_catalog(Economics_and_Administrative_Sciences_Course):
    pass
class MIS_New_catalog(Economics_and_Administrative_Sciences_Course):
    pass
class MIS_Old_catalog(Economics_and_Administrative_Sciences_Course):
    pass

class Architecture_and_Fine_Arts_Course(models.Model):
    semester = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    hours_lecture = models.IntegerField(null=True, blank=True)
    hours_tutorial = models.IntegerField(null=True, blank=True)
    hours_lab = models.IntegerField(null=True, blank=True)
    pre_requisite = models.TextField(null=True, blank=True)
    ects_credit = models.CharField(max_length=255,null=True, blank=True)
    total_credits = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.course_code
class interior_New_catalog(Architecture_and_Fine_Arts_Course):
    pass
class interior_Old_catalog(Architecture_and_Fine_Arts_Course):
    pass
class archi_New_catalog(Architecture_and_Fine_Arts_Course):
    pass
class archi_Old_catalog(Architecture_and_Fine_Arts_Course):
    pass

class Health_Sciences_Course(models.Model):
    semester = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    hours_lecture = models.IntegerField(null=True, blank=True)
    hours_tutorial = models.IntegerField(null=True, blank=True)
    hours_lab = models.IntegerField(null=True, blank=True)
    pre_requisite = models.TextField(null=True, blank=True)
    ects_credit = models.CharField(max_length=255,null=True, blank=True)
    total_credits = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.course_code
class nutrition_catalog(Health_Sciences_Course):
    pass
class physiotherapy_engl_catalog(Health_Sciences_Course):
    pass
class physiotherapy_turk_new_catalog(Health_Sciences_Course):
    pass
class physiotherapy_turk_old_catalog(Health_Sciences_Course):
    pass
class nursing_catalog(Health_Sciences_Course):
    pass   

class AreaTechnicalElectiveCourse(models.Model):
    course_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    hours_lecture = models.IntegerField(null=True, blank=True)
    hours_tutorial = models.IntegerField(null=True, blank=True)
    hours_lab = models.IntegerField(null=True, blank=True)
    pre_requisite = models.TextField(null=True, blank=True)
    ects_credit = models.CharField(max_length=255,null=True, blank=True)
    total_credits = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.course_code

class Transcript(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    ects_credits = models.CharField(max_length=255, blank=True, null=True)
    grades = models.CharField(max_length=255, blank=True, null=True)
    credits = models.CharField(max_length=255, blank=True, null=True)
    grade_points = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.grades}"
    