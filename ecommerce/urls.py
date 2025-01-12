"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin
import os
from django.conf import settings
from django.conf.urls.static import static

from django.urls import include, path, re_path
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Productos API",
      default_version='v1',
      description="Test de apis para listar y crear productos, listar historial y listar top de productos más buscados",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="daimercuellar@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),                                       # admin site
    path('api/', include('mixins.urls')),                                       # Urls del módulo de autenticacion y usuarios
    path('api/', include('products.urls')),                    # Urls del módulo de administración de archivos
    path('api/', include('user.urls')),                    # Urls del módulo de administración de archivos
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
