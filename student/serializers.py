from .models import Student, StudentAddition
from rest_framework import serializers


class StudentAdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAddition
        fields = ['id', 'index_number']

class StudentSerializer(serializers.ModelSerializer):
    more = StudentAdditionSerializer(read_only=True)
    if more is None:
        more=None
    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'last_name',
            'other_name',
            'dob',
            'email',
            'gender',
            'phone_number',
            'address',
            'more'
            ]


class StudentCreateSerializer(serializers.ModelSerializer):
    more = StudentAdditionSerializer(read_only=True)
    index_number = serializers.CharField(write_only=True)
    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'last_name',
            'other_name',
            'index_number',
            'username',
            'dob',
            'email',
            'gender',
            'phone_number',
            'address',
            'more'
            ]

class StudentFeesSerializer(serializers.ModelSerializer):
    more = StudentAdditionSerializer(read_only=True)
    class Meta:
        model = Student
        fields = [
            'id',
            'more'
        ]