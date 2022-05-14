from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class File_Upload(models.Model):
    user_specific = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    ids = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=30)
    my_file = models.FileField(upload_to="F")
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self): 
        return f"{self.file_name}"
    
class Updates(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    upload = models.CharField(max_length=200,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}"
    
    
        