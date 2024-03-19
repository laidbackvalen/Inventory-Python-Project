from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('delete/<int:id>/',views.delete),
    path('approve/<int:id>/',views.approve),
]