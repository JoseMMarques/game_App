from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Teacher, Student, Employee
from .forms import UserAdminCreationForm, UserAdminForm


class UserAdmin(BaseUserAdmin):
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('type', 'name', 'email', 'sex', 'phone_number', 'address',
                       'is_admin', 'is_staff', 'is_active', 'is_superadmin', 'is_game',
                       'password1', 'password2',)
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('email', 'password', 'type', )
        }),
        ('Informações Básicas', {
            'fields': ('name', 'birth_date', 'sex', 'phone_number', 'address', )
        }),
        (
            'Permissões', {
                'fields': (
                    'is_active', 'is_staff', 'is_admin', 'is_superadmin', 'is_game',
                    'user_permissions'
                )
            }
        )
    )
    list_display = [
        'type', 'name', 'get_first_name', 'get_last_name', 'get_age', 'birth_date', 'sex', 'phone_number',
        'address', 'is_game'
    ]

    list_filter = [
        'type', 'name', 'birth_date', 'sex', 'phone_number', 'address', 'is_game',
        'created', 'modified', 'is_game'
    ]

    search_fields = [
        'type', 'name', 'birth_date', 'sex', 'phone_number', 'address', 'is_game',
        'created', 'modified', 'is_game'
    ]

    ordering = ('name', 'email',)


admin.site.register(User, UserAdmin)


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)


# Register your models here.
