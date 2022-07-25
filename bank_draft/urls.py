from django.urls import path
from . import views

urlpatterns = [
    path('', views.BankView.as_view()),
    path('<int:pk>/', views.BankDetailView.as_view()),
    path('bank_draft/', views.BankDraftView.as_view()),
    path('bank_draft/<int:pk>/', views.BankDraftDetailView.as_view())
]
