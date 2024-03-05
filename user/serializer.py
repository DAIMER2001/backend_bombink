
from mixins.models import ListItem
from mixins.serializers import BaseSerializer
from user.models import CustomUser
from django_filters import rest_framework as filters
import django_filters


class CustomUserSerializer(BaseSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')
        read_only_fields = ('date_joined',)

class UserFilter(filters.FilterSet):
    first_name = filters.CharFilter(lookup_expr='iexact')
    last_name = filters.CharFilter(lookup_expr='iexact')
    email = filters.CharFilter(lookup_expr='iexact')
    is_staff = filters.BooleanFilter()
    is_active = filters.BooleanFilter()

    # country__id = django_filters.NumberFilter()

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')
