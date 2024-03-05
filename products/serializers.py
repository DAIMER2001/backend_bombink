
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
    images = ImagesSerializer(many=True, required=False)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'discount', 'images', 'country',)
        expandable_fields = {
            'images': (ImagesSerializer, {'many': True}),
        }
    
    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        product = Product.objects.create(**validated_data)
        self._create_images(product, images_data)
        return product

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', [])
        instance = super().update(instance, validated_data)
        instance.images.all().delete()
        self._create_images(instance, images_data)
        return instance

    def _create_images(self, product, images_data):
        for image_data in images_data:
            File.objects.create(product=product, **image_data)



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
