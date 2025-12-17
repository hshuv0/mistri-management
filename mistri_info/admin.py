from django.contrib import admin
from .models import Mistri

# # Register your models here.


# admin.site.register(Mistri)

@admin.register(Mistri)
class MistriAdmin(admin.ModelAdmin):
    list_display = ('image', 'name', 'skill', 'location', 'contact')
    search_fields = ('name', 'skill', 'location')

