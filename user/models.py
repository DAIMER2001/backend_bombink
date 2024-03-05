
from django.contrib.auth.models import AbstractUser
from mixins.models import ListItem, BaseModel
from django.db import models
from mixins.models import BaseModel
from safedelete.models import SafeDeleteModel
from django.contrib.auth.models import UnicodeUsernameValidator

class Role(SafeDeleteModel):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    identificador = models.CharField(max_length=4, blank=True)
    published = models.BooleanField(default=False, verbose_name = 'Activo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['id', 'name', 'id']

class RolesProjects(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    identificador = models.CharField(max_length=3, unique=True, blank=True)
    # project = models.ForeignKey(project,  verbose_name="proyecto", on_delete=models.CASCADE)
    role = models.OneToOneField(Role, related_name='role', on_delete=models.CASCADE, null=True)

class CustomUser(AbstractUser):
    roles = models.ManyToManyField(RolesProjects, blank=True)
    document_number = models.BigIntegerField(blank=True, null=True, verbose_name='Número  de documento de indentifiación')
    document_type = models.ForeignKey('mixins.ListItem', on_delete=models.PROTECT, null=True, blank=True)
    reset_token = models.CharField(max_length=100, null=False, blank=True)
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        ('username'),
        max_length=150,
        unique=True,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
        null=True,
        blank=True,
    )
    embedding = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=150, unique=True, null=False, blank= False)
    city = models.ForeignKey(ListItem, blank=True, null=True, on_delete=models.CASCADE, related_name='city_id')
    country = models.ForeignKey(ListItem, blank=True, null=True, on_delete=models.CASCADE, related_name='country_id')

    class Meta:
        ordering = ['-id']
