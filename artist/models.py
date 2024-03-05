from django.db import models





class Artist(models.Model):
    nickname = models.CharField(max_length=200)
    


# Create your models here.
