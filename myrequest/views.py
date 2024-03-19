from django.shortcuts import render
from newrequest.models import NewRequest
# Create your views here.
from django.db import connection
def home(request):
    user_list = request.session.get('user_list', None)
    eid = user_list[0]
    req = []
    for p in NewRequest.objects.raw('select * from NewRequest'):
        if p.emp_id == eid:
            req.append(p)
    return render(request,'myrequest/home.html',{'req':req})