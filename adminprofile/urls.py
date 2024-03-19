from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('upload/',include('upload.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('adminrequest/',include('adminrequest.urls')),
    path('return/',views.adminreturn),
]