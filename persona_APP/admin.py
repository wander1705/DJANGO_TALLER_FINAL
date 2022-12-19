from django.contrib import admin
from persona_APP.models import Institucion, Proyecto

# Register your models here.

class Institucionadmin(admin.ModelAdmin):
    list_display = ['institucion']

admin.site.register(Institucion, Institucionadmin)