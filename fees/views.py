from rest_framework import generics

from fees.models import Fees
from fees.serializers import FeesSerializer
from student.models import Student



class FeesView(generics.ListCreateAPIView):
    queryset = Fees.objects.all()
    serializer_class = FeesSerializer
    
    # def perform_create(self, serializer):
    #     if serializer.is_valid():
    #         student_id = serializer.validated_data.get('student_id')
    #         amount = serializer.validated_data.get('amount')
    #         reference = serializer.validated_data.get('reference')
            
    #         student = Student.objects.get(id=student_id)
    #         if student is not None:
    #             fees = Fees(student=student, amount=amount, reference=reference)
                
    #             fees.save()



            