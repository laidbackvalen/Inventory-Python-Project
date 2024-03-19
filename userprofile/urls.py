from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profile),
    path('newrequest/',include('newrequest.urls')),
    path('myrequest/',include('myrequest.urls')),
    path('myreturn/',include('myreturn.urls')),
]