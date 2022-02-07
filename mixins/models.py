
from django.db import models
from django.conf import settings
from safedelete.models import SafeDeleteModel
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE, SOFT_DELETE

class ListType(SafeDeleteModel):
    parent              = models.ForeignKey('mixins.ListType', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Tipo de lista padre')
    code                = models.CharField(max_length=15, verbose_name='Código', blank=True,)
    name                = models.CharField(max_length=150, verbose_name='Nombre')
    description         = models.TextField(verbose_name='Descripción')
    meta                = models.TextField(verbose_name='Metadata')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de lista'
        verbose_name_plural = 'Tipos de listas'
        ordering = ['id']


class ListItem(SafeDeleteModel):
    parent              = models.ForeignKey('mixins.ListItem', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Elemento padre')
    list_type           = models.ForeignKey(ListType, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Elemento de la lista')
    code                = models.CharField(max_length=15, verbose_name='Código', blank=True,)
    name                = models.CharField(max_length=150, verbose_name='Nombre')
    description         = models.TextField(verbose_name='Descripción')
    meta                = models.TextField(verbose_name='Metadata')

    def __str__(self):
        return self.list_type.name + ' - ' + self.name

    class Meta:
        verbose_name = 'Elemento de la lista'
        verbose_name_plural = 'Elementos de la lista'
        ordering = ['id']



# Create your models here.
class BaseModel(SafeDeleteModel):
    _safedelete_policy  = SOFT_DELETE
    published           = models.BooleanField(default=False, verbose_name = 'Activo')
    created             = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')
    updated             = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de actualización', null=True)
    created_by          = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', blank=True, null=True, verbose_name="Creado por", on_delete=models.PROTECT)
    updated_by          = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', blank=True, null=True, verbose_name="Modificado por", on_delete=models.PROTECT)

    class Meta:
        abstract = True

    def publish(self):
        self.published = True
        self.save()

    def unpublish(self):
        self.published = False
        self.save()

