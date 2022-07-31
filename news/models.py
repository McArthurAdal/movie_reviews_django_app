from distutils.command.upload import upload
from email.mime import image
from operator import mod
from django.db import models

# Create your models here.
class News(models.Model):

    def __str__(self):
        return self.headline

    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField() 
    image = models.ImageField(upload_to='news/images/')
    url = models.URLField(blank=True)