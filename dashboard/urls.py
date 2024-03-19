from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('query/',views.query),
    path('query1/',views.query1),
    path('query1/xyz/',views.xyz),
]