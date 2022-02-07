import json
from django.shortcuts import render
from rest_framework import filters as filterRest
from django_filters.rest_framework import DjangoFilterBackend 
import django_filters.rest_framework
from products.forms import UploadFileForm
from products.models import HistorySearchProduct, Product, File
from rest_framework import viewsets, filters, mixins, status
from rest_framework import generics
from products.serializers import HistorySerializer, ImagesSerializer, ProductFilter, ProductSerializer
from rest_framework.pagination import PageNumberPagination 
from rest_framework.response import Response  # new
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import action

class ExtendedPagination(PageNumberPagination):
    page_size = 8

    def get_paginated_response(self, data):
        print(data)
        return Response({
            'count': self.page.paginator.count,
            'num_pages': self.page.paginator.num_pages,
            'page_number': self.page.number,
            'page_size': self.page_size,
            'next_link': self.get_next_link(),
            'previous_link': self.get_previous_link(),
            'results': data
        })

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filterRest.SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['^name',]


class ProductsSearchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ExtendedPagination
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend, filterRest.SearchFilter]
    search_fields = ['^name',]

    def dispatch(self, request, *args, **kwargs):
        try:
            queryset = Product.objects.all()
            filter_product = ProductFilter(self.request.GET, queryset=queryset)
            if filter_product.qs is not None:
                for product in filter_product.qs:
                    productHistory = HistorySearchProduct.objects.filter(id_product = product.id).first()
                    count = 1
                    if productHistory is not None:
                        dataHistory = HistorySerializer(productHistory, many = False).data
                        count = dataHistory['count_search'] + 1
                    HistorySearchProduct.objects.update_or_create(
                        id_product=product,
                        defaults={'count_search': count},
                    )
        except Product.DoesNotExist:
            self.property = None
        return super().dispatch(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     queryset = Product.objects.all()
    #     filter_product = ProductFilter(self.request.GET, queryset=queryset)
    #     if filter_product.qs is not None:
    #         for product in filter_product.qs:
    #             productHistory = HistorySearchProduct.objects.filter(id_product = product.id).first()
    #             count = 1
    #             if productHistory is not None:
    #                 dataHistory = HistorySerializer(productHistory, many = False).data
    #                 count = dataHistory['count_search'] + 1
    #             HistorySearchProduct.objects.update_or_create(
    #                 id_product=product,
    #                 defaults={'count_search': count},
    #             )
    #     return data

    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     filter_product = ProductFilter(self.request.GET, queryset=queryset)
    #     if filter_product.qs is not None:
    #         for product in filter_product.qs:
    #             productHistory = HistorySearchProduct.objects.filter(id_product = product.id).first()
    #             count = 1
    #             if productHistory is not None:
    #                 dataHistory = HistorySerializer(productHistory, many = False).data
    #                 count = dataHistory['count_search'] + 1
    #             HistorySearchProduct.objects.update_or_create(
    #                 id_product=product,
    #                 defaults={'count_search': count},
    #             )

    #     return queryset


class HistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HistorySearchProduct.objects.all()
    serializer_class = HistorySerializer

    
    def productsTop(self, request):
        queryset = HistorySearchProduct.objects.all().order_by('-count_search')[0:5]
        serializer = HistorySerializer(queryset, many = True).data
        productosTop = []
        for history_product in serializer:
            product = Product.objects.get(pk = history_product['id_product'])
            expand=["plan_de_aula"]
            product_srl = ProductSerializer(product, many = False, expand = ['images',])
            price = product_srl['price'].value
            discountApply = price - (price * (product_srl['discount'].value / 100))
            data = {}
            data['name'] = product_srl['name'].value
            data['price'] = product_srl['price'].value
            data['discountPrice'] = discountApply
            data['discount'] = '{}%'.format(str(product_srl['discount'].value))
            data['images'] = product_srl['images'].value
            history_product['product'] = data
            productosTop.append(data)
        return Response(productosTop)


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = ImagesSerializer

    def create(self, request, *args, **kwargs):
        if request.data["file"] is not None:
            # request.data["title"] = str(request.data["file"])
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'message': 'file not sent'})
