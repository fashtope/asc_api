from django.urls import path

from . import views

urlpatterns = [
    path('', views.FeesView.as_view())
]
