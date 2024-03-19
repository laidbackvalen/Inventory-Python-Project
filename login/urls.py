from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login),
    path('signup/',include('signup.urls')),
    path('profile/',include('userprofile.urls')),
    path('adminprofile/',include('adminprofile.urls')),
]