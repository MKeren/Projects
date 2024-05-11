from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser, Role

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email')
    list_filter = ()
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ('user_permissions', 'groups')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.role != 'supervisor':
            qs = qs.filter(role='teacher')
        return qs

    def has_change_permission(self, request, obj=None):
        if obj and obj.role == 'supervisor' and request.user.role != 'supervisor':
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.role == 'supervisor' and request.user.role != 'supervisor':
            return False
        return super().has_delete_permission(request, obj)

    def save_model(self, request, obj, form, change):
        if not change and obj.role == 'supervisor' and request.user.role != 'supervisor':
            obj.role = 'teacher'
        super().save_model(request, obj, form, change)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role)