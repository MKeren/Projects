from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Role)

#admin.site.register(CustomUser)
#admin.site.register(Role)