from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('title','date_creat','date_edit',)
    list_filter = ('date_creat',)
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','date_creat','date_edit',)
    list_filter = ('date_creat',)
    search_fields = ('title',)


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('title','demo','date_creat','date_edit','eksports','imports','name','volume','category',)
    list_filter = ('demo','date_creat','eksports','imports','category',)
    search_fields = ('title','name','volume',)


@admin.register(Pest)
class PestAdmin(admin.ModelAdmin):
    list_display = ('analysis','title','date_creat',)
    list_filter = ('analysis','date_creat',)
    search_fields = ('title',)


@admin.register(Opros)
class OprosAdmin(admin.ModelAdmin):
    list_display = ('title','date_creat',)
    list_filter = ('date_creat',)
    search_fields = ('title',)


@admin.register(Opros_body)
class Opros_bodyAdmin(admin.ModelAdmin):
    list_display = ('opros','title','date_creat',)
    list_filter = ('opros','date_creat',)
    search_fields = ('title',)


@admin.register(Summary_rating)
class Summary_ratingAdmin(admin.ModelAdmin):
    list_display = ('title','date_creat',)
    list_filter = ('date_creat',)
    search_fields = ('title',)


@admin.register(Confidence_level)
class Confidence_levelAdmin(admin.ModelAdmin):
    list_display = ('title','date_creat',)
    list_filter = ('date_creat',)
    search_fields = ('title',)


@admin.register(Opros_answer)
class Opros_answerAdmin(admin.ModelAdmin):
    list_display = ('pest','opros_body','summary_rating','confidence_level','body','date_creat','author')
    list_filter = ('author','pest','date_creat',)
    search_fields = ('author','pest','date_creat',)

