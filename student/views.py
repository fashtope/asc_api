from django.shortcuts import render

from rest_framework import generics, mixins

from account.models import User
from fees.fees_func import student_total_fees

from .models import Student, StudentAddition
from .serializers import StudentCreateSerializer, StudentSerializer


class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # lookup_field =


class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            first_name = serializer.validated_data.get('first_name')
            last_name = serializer.validated_data.get('last_name')
            other_name = serializer.validated_data.get('other_name')
            dob = serializer.validated_data.get('dob')
            email = serializer.validated_data.get('email')
            gender = serializer.validated_data.get('gender')
            phone_number = serializer.validated_data.get('phone_number')
            address = serializer.validated_data.get('address')
            index_number = serializer.validated_data.pop('index_number')

            student = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                other_name=other_name,
                dob=dob,
                email=email,
                gender=gender,
                phone_number=phone_number,
                address=address,
                username=index_number,
                type=User.Types.STUDENT
            )

            student_addition = StudentAddition(
                user=student, index_number=index_number)

            student_addition.save()


class StudentUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if serializer.is_valid():
            first_name = serializer.validated_data.get('first_name')
            last_name = serializer.validated_data.get('last_name')
            other_name = serializer.validated_data.get('other_name')
            dob = serializer.validated_data.get('dob')
            email = serializer.validated_data.get('email')
            gender = serializer.validated_data.get('gender')
            phone_number = serializer.validated_data.get('phone_number')
            address = serializer.validated_data.get('address')
            index_number = serializer.validated_data.pop('index_number')
            
            student = Student.objects.get(id=pk)
            student.first_name=first_name
            student.last_name=last_name
            student.other_name=other_name
            student.dob=dob
            student.email=email
            student.gender=gender
            student.phone_number=phone_number
            student.address=address,
            student.username=index_number,
            
            student.save()

            student_addition = StudentAddition.objects.get(user=student)
            student_addition.index_number=index_number

            student_addition.save()


class StudentDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    lookup_field = 'pk'

# class StudentView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentCreateSerializer
#     lookup_field = 'pk'

#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
#     def put(self, request,*args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def perform_create(self, serializer):
#         if serializer.is_valid():
#             first_name = serializer.validated_data.get('first_name')
#             last_name = serializer.validated_data.get('last_name')
#             other_name = serializer.validated_data.get('other_name')
#             dob = serializer.validated_data.get('dob')
#             email = serializer.validated_data.get('email')
#             gender = serializer.validated_data.get('gender')
#             phone_number = serializer.validated_data.get('phone_number')
#             address = serializer.validated_data.get('address')
#             index_number = serializer.validated_data.pop('index_number')

#             student = User.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 other_name=other_name,
#                 dob=dob,
#                 email=email,
#                 gender=gender,
#                 phone_number=phone_number,
#                 address=address,
#                 username=index_number,
#                 type=User.Types.STUDENT
#             )

#             student_addition = StudentAddition(
#                 user=student, index_number=index_number)

#             student_addition.save()
