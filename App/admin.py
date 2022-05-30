from re import A
from django.contrib import admin
from .models import App

# Register your models here.
@admin.register(App)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name' ,'address', 'num']


