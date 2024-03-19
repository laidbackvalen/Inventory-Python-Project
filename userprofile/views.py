from django.shortcuts import render
from signup.models import Employee
# Create your views here.
def profile(request):
    user_list = request.session.get('user_list',None)
    eid = user_list[0]
    context = Employee.objects.get(pk = eid)
    args = {
        'eid' : eid,
        'name' : context.name,
        'email' : context.emailaddress
    }
    return render(request,'userprofile/home.html',args)