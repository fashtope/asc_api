from student.models import Student
from .models import Fees

def student_total_fees(student_id):
    student = Student.objects.get(student_id)
    fees = Fees.objects.filter(student=student)
    
    print(fees.values_list())