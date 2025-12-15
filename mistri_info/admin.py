from django.contrib import admin
from .models import Mistri

<<<<<<< HEAD
# Register your models here.
=======
# # Register your models here.


# @admin.register(Mistri)
# class MistriAdmin(admin.ModelAdmin):
#     list_display = ('image', 'name', 'skill', 'location', 'contact' )
>>>>>>> 6736dab (second commit)

# admin.site.register(Mistri)

@admin.register(Mistri)
class MistriAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('image', 'name', 'skill', 'location', 'contact' )
=======
    list_display = ('image', 'name', 'skill', 'location', 'contact')
    search_fields = ('name', 'skill', 'location')
>>>>>>> 6736dab (second commit)
