from django.db import models
from django.contrib.auth.models import User

class Area(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(null=True, blank=True)
    date_creat = models.DateField(auto_now_add=True)
    date_edit = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'area'



class Category(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(null=True, blank=True)
    date_creat = models.DateField(auto_now_add=True)
    date_edit = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'category'
    
    
    
class Analysis(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    demo = models.BooleanField(default=False)
    date_creat = models.DateField(auto_now_add=True)
    date_edit = models.DateField(auto_now=True)
    area = models.CharField(max_length=500,null=True, blank=True)
    eksports = models.ForeignKey(Area, related_name='eksports', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    imports = models.ForeignKey(Area, related_name='imports', on_delete=models.SET_NULL, null=True)
    body = models.TextField(null=True, blank=True)
    volume = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'analysis'
        
class Pest(models.Model):
    analysis = models.ForeignKey(Analysis, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    damage = models.CharField(max_length=200, blank=True, null=True)
    protection = models.CharField(max_length=200, blank=True, null=True)
    date_creat = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'pest'


class Opros(models.Model):
    title = models.CharField(max_length=200)
    date_creat = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'opros'


class Opros_body(models.Model):
    opros = models.ForeignKey(Opros, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    date_creat = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'opros_body'


class Summary_rating(models.Model):
    title = models.CharField(max_length=100)
    date_creat = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'summary_rating'


class Confidence_level(models.Model):
    title = models.CharField(max_length=100)
    date_creat = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'confidence_level'


class Opros_answer(models.Model):
    opros_body = models.ForeignKey(Opros_body, on_delete=models.SET_NULL, null=True)
    pest = models.ForeignKey(Pest, on_delete=models.SET_NULL, null=True)
    body = models.TextField(null=True, blank=True)
    summary_rating = models.ForeignKey(Summary_rating, on_delete=models.SET_NULL, null=True)
    confidence_level = models.ForeignKey(Confidence_level, on_delete=models.SET_NULL, null=True)
    date_creat = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.body
    
    class Meta:
        db_table = 'opros_answer'
