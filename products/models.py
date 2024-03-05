import os
import random
import hashlib
from django.db import models
from mixins.models import BaseModel, ListItem
from mixins.validators import FileMimeValidator
from datetime import datetime


def temp_name(instance, filename):
    timestamp = datetime.timestamp(datetime.now())
    basefilename, file_extension= os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    randomstr = hashlib.md5(randomstr.encode() + str(timestamp).encode()).hexdigest()
    return 'filemanager/temp/{randomstring}{ext}'.format(basename=basefilename, randomstring=randomstr, ext=file_extension)


class File(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to=temp_name, blank=True, null=True, 
        validators=[
            FileMimeValidator()
        ])

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Product(BaseModel):

    name =          models.CharField(max_length=100, blank=False, null= False)
    description =   models.TextField(blank=False, null= False)
    price =         models.IntegerField(blank=False, null=False)
    discount =      models.IntegerField(blank=True, null=True)
    country =       models.ForeignKey(ListItem, blank=True, null=True, on_delete=models.SET_NULL)
    images =        models.ManyToManyField(File)

    class Meta:
        ordering = ['-id']
    

class HistorySearchProduct(BaseModel):

    id_product = models.ForeignKey(Product, blank=False, null=False, on_delete=models.DO_NOTHING)
    count_search = models.IntegerField(blank=False, null= False)
    
    class Meta:
        ordering = ['-id']

