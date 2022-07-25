from django_filters import rest_framework as filters

from student.models import Student


class StudentFilter(filters.FilterSet):
    index_number = filters.CharFilter(field_name='studentaddition__index_number', lookup_expr='icontains')
    department = filters.CharFilter(field_name='department__name', lookup_expr='icontains')
    
    class Meta:
        model=Student
        fields = ['studentaddition__index_number', 'department', 'first_name', 'last_name', 'other_name']