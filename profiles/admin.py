from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Person

admin.site.register(Person)
class ListAdmin(admin.ModelAdmin):
    list_display = ("lastName", "firstName")
    search_fields = ("lastName__startswith", )
   

admin.site.unregister(User)
admin.site.unregister(Group) 


admin.site.site_header = 'Administration App (HomeWork2)'

# Register your models here.
