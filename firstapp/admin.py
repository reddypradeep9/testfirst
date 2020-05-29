from django.contrib import admin
from firstapp.models import studentmodel

class studentadmin(admin.ModelAdmin):
    list_display=['name','email']
admin.site.register(studentmodel,studentadmin)
