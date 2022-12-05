from django.db import models

# Create your models here.


class Family(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, null=True)
    age = models.IntegerField()
    born_date = models.DateField(null= True)
   

   
    