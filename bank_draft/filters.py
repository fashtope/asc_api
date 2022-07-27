from django_filters import rest_framework as filters

from .models import BankDraft


class BankDraftFilter(filters.FilterSet):
    draft_number = filters.CharFilter(field_name='draft_number', lookup_expr='iexact')
    
    class Meta:
        model=BankDraft
        fields = ['draft_number']