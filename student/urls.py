from django.urls import path

from . import views

urlpatterns = [
    path('', views.StudentListCreateAPIView.as_view()),
    # path('<int:pk>', views.StudentDetailAPIView.as_view()),
    path('<int:pk>', views.StudentUpdateAPIView.as_view()),
    path('<int:pk>/delete', views.StudentDestroyView.as_view()),
]
