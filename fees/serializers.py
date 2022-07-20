from rest_framework import serializers

from student.serializers import StudentFeesSerializer

from .models import Fees


class FeesSerializer(serializers.ModelSerializer):
    # student = StudentFeesSerializer(read_only=True)
    # student_id = serializers.CharField(write_only=True)
    # date = serializers.DateField(source=, read_only=True)
    class Meta:
        model = Fees
        fields = [
            'id',
            'student',
            'amount',
            'reference',
            'date'
        ]
        read_only_fields = ['date']