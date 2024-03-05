
from django.forms import ClearableFileInput
from mixins.serializers import BaseSerializer
from products.models import HistorySearchProduct, Product, File
import django_filters
from django_filters import rest_framework as filters
from rest_framework import fields, serializers



class TattoFileSerialier(serializers.ModelSerializer):
        class Meta:
        model = File
        fields = ('id', 'title', 'file',)

