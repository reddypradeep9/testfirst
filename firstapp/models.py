from django.db import models

class studentmodel(models.Model):
    name=models.CharField(max_length=40)
    rollno=models.IntegerField()
    email=models.EmailField()
    releasedate=models.DateField()
    
