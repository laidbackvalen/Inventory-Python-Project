from django.shortcuts import render, redirect
from newrequest.models import NewRequest
from .forms import approvalform
from adminprofile.models import items
from django.db import connection
# Create your views here.
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns,row))
        for row in cursor.fetchall()
    ]

def home(request):
    req = NewRequest.objects.raw('select * from NewRequest')
    ite = []
    for p in req:
        cou = items.objects.filter(Name = p.item_name)
        cou = cou.filter(In_use = False).count()
        dicti = {'cou' : cou , 'req':p}
        ite.append(dicti)
    return render(request,'adminrequest/home.html',{'ite':ite})

def delete(request,id):
    req = NewRequest.objects.get(request_id = id)
    req.delete()
    req = NewRequest.objects.raw('select * from NewRequest')
    return redirect('/adminprofile/adminrequest/')

def approve(request,id):
    req = NewRequest.objects.get(request_id=id)
    eid = req.emp_id
    form = approvalform(request.POST)
    if form.is_valid():
        if not items.objects.filter(id = form.cleaned_data['item_no']).exists():
            return redirect('./')
        print("Yes")
        item = items.objects.get(id = form.cleaned_data['item_no'])
        item.Loaned = 1;
        item.In_use = 1;
        item.save()
        if req.qty == 1:
            req.delete()
        else:
            req.qty = req.qty - 1;
            req.save()
        form.save()
        return redirect('/adminprofile/adminrequest/')
    return render(request,'adminrequest/approval.html',{'form':form, 'id':id, 'eid':eid})

