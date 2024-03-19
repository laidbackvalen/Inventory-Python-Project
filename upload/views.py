from django.shortcuts import render
import openpyxl
# Create your views here.
from .forms import ItemForm
def home(request):
    form = ItemForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        form = ItemForm()
    return render(request,'upload/home.html',{'form' : form})