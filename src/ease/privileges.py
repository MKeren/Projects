from django.contrib.auth.models import Permission

#Different permissions for differents users according to their roles
supervisor_permissions = [
    Permission.objects.get(codename='add_student'),
    Permission.objects.get(codename='update_student'),
    Permission.objects.get(codename='delete_student'),
    Permission.objects.get(codename='add_course'),
    Permission.objects.get(codename='update_course'),
    Permission.objects.get(codename='delete_course'),
    Permission.objects.get(codename='add_transcript'),
    Permission.objects.get(codename='update_transcript'),
    Permission.objects.get(codename='delete_transcript'),
]

professor_permissions = [
    Permission.objects.get(codename='add_student'),
    Permission.objects.get(codename='update_student'),
    Permission.objects.get(codename='view_transcript'),
    Permission.objects.get(codename='update_transcript'),
]
