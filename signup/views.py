from django.shortcuts import render,redirect
from signup.forms import EmployeeForm
from signup.models import Employee

# Create your views here.
def signup(request):
    form = EmployeeForm(request.POST)
    if form.is_valid():
       # print(form["Employee_Id"])
        form.save()
        return redirect('../')
    return render(request,'signup/home.html',{'form':form})