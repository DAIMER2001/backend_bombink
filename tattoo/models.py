import os
from django.db import models
from mixins.validators import FileMimeValidator
from datetime import datetime

def temp_name(instance, filename):
    timestamp = datetime.timestamp(datetime.now())
    basefilename, file_extension= os.path.splitext(filename)
    randomstr = str(timestamp).encode()
    return 'filemanager/temp/{randomstring}{ext}'.format(basename=basefilename, randomstring=randomstr, ext=file_extension)



class TattooCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField
    
    
class TattooFiles(models.Model):
    sketch = models.FileField(upload_to=temp_name, blank=True, null=True, 
        validators=[
            FileMimeValidator()
        ])
# Create your models here.
