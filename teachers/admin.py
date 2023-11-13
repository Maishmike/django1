from django.contrib import admin
from . models import Students, Sliders
from django.contrib.auth.admin import UserAdmin
from teachers.form import CustomUserCreationForm, CustomUserChangeForm
from teachers.models import CustomUser

# Register your models here.

admin.site.register(Students)
admin.site.register(Sliders)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm


admin.site.register(CustomUser, CustomUserAdmin)