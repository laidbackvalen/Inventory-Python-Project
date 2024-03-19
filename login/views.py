from django.shortcuts import render, redirect
from login.forms import ProfileForm
from signup.models import Employee
from adminprofile.models import useradmin
from django.http import Http404
# Create your views here.
def login(request):
    form = ProfileForm(request.POST)
    #print(form.errors)
    if form.is_valid():
        eid = form["emp_id"].value()
        pas = form["emp_pas"].value()
        for p in useradmin.objects.raw('select * from useradmin'):
            if p.Employee_Id==eid and p.password==pas:
                user_list = [eid]
                request.session['user_list'] = user_list
                return redirect('adminprofile/')
        for p in Employee.objects.raw('select * from Employee'):
            if p.Employee_Id==eid and p.password==pas:
                user_list = [eid]
                request.session['user_list'] = user_list
                return redirect('profile/')
    return render(request,'login/home.html',{'form':form})