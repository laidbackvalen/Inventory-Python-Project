from django.shortcuts import render
from adminrequest.models import approval
from newrequest.models import NewRequest
# Create your views here.
def home(request):
    user_list = request.session.get('user_list', None)
    eid = user_list[0]
    req = []
    for p in approval.objects.raw('select * from approval'):
        if p.emp_id == eid:
            req.append(p)
    return render(request,'myreturn/home.html',{'req':req})