
from . import views
from django.urls import path, include


urlpatterns = [
    # path('students', views.students, name='students'),
    # path('create_student', views.create_student,),
    path("department/", include('department.urls')),
    path('student/', include('student.urls')),
    path('fees/', include('fees.urls')),
    path('bank/', include('bank_draft.urls'))
]
