from django.db import models

# Create your models here.
class info(models.Model) :
    teamno = models.IntegerField
    teamname = models.CharField(max_length='200')
    pagetitle = models.CharField(max_length='200')
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    explanation = models.TextField() #140자 제한
    pagelink = models.TextField()