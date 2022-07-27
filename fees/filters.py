from django_filters import rest_framework as filters

from .models import Fees


class FeesFilter(filters.FilterSet):
    index_number = filters.CharFilter(field_name='student__studentaddition__index_number', lookup_expr='icontains')
    
    class Meta:
        model=Fees
        fields = ['index_number']