import csv
from account.models import User

from student.models import Student, StudentAddition


def run():
    fhand = open('student/student.csv')  #open document
    reader = csv.reader(fhand) #Read document
    next(reader) # Don't read the first line
    
    for row in reader:
        student_obj = Student.objects.filter(username=row[3]).exists()
        
        if student_obj is False:
            student = User.objects.create_user(
                    first_name=row[0],
                    last_name=row[1],
                    username=row[3],
                    email=row[-1],
                    password=row[0],
                    other_name=row[2],
                    address=row[5],
                    dob=row[4],
                    phone_number=row[6],
                    gender=row[7],
                    type=User.Types.STUDENT
                )
            
            student_addition = StudentAddition(
                    user=student,
                    index_number=row[3],
                )
            
            student_addition.save()
    
    
    