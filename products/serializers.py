
from django.forms import ClearableFileInput
from mixins.serializers import BaseSerializer
from products.models import HistorySearchProduct, Product, File
import django_filters
from django_filters import rest_framework as filters
from rest_framework import fields, serializers



class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'title', 'file',)


class ProductSerializer(BaseSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'discount', 'images', 'country',)
        expandable_fields = {
            'images': (ImagesSerializer, {'many': True}),
        }



class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='iexact')
    price = filters.NumberFilter()
    price__gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    discount = filters.NumberFilter()
    discount__gt = filters.NumberFilter(field_name='discount', lookup_expr='gt')
    discount__lt = filters.NumberFilter(field_name='discount', lookup_expr='lt')


    country__id = django_filters.NumberFilter()

    # def __init__(self, *args, author=None, **kwargs):
    #     print('filtersss')
    #     super().__init__(*args, **kwargs)
        # do something w/ author

    class Meta:
        model = Product
        fields =  ('id', 'name', 'description', 'price', 'discount', 'images', 'country',)


class HistorySerializer(BaseSerializer):
    class Meta:
        model = HistorySearchProduct
        fields = ('id', 'id_product', 'count_search',)
        expandable_fields = {
            'id_product': (ProductSerializer, { 'many' : False }),
        }
