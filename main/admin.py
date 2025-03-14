from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Area)
class AftomabilAdmin(admin.ModelAdmin):
    list_display = ('title','date_creat','date_edit',)
    list_filter = ('date_creat',)
    search_fields = ('title',)


@admin.register(Category)
class AftomabilAdmin(admin.ModelAdmin):
    list_display = ('title','date_creat','date_edit',)
    list_filter = ('date_creat',)
    search_fields = ('title',)


@admin.register(Analysis)
class AftomabilAdmin(admin.ModelAdmin):
    list_display = ('title','demo','date_creat','date_edit','eksports','imports','name','volume','category',)
    list_filter = ('demo','date_creat','eksports','imports','category',)
    search_fields = ('title','name','volume',)