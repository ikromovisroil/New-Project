from django.db import models

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
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'analysis'