from django.shortcuts import render
from .forms import queryform, queryform2
from adminprofile.models import items
from adminrequest.models import approval
from signup.models import Employee
from newrequest.models import NewRequest
from django.db import connection
from datetime import date
import datetime

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns,row))
        for row in cursor.fetchall()
    ]
def addYears(d,years):
    try:
        return d.replace(year = d.year + years)
    except:
        return d + (date(d.year+years,1,1) - date(d.year,1,1))
# Create your views here.
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns,row))
        for row in cursor.fetchall()
    ]
def home(request):
    penreq = NewRequest.objects.count()
    util = items.objects.filter(In_use = "True").count() / items.objects.count()
    util = util*100
    util = round(util,2)
    cond = items.objects.filter(Condition = "Good").count() / items.objects.count()
    cond = cond*100
    cond = round(cond,2)
    rep = items.objects.filter(Replacement_Required="True").count() / items.objects.count()
    rep = rep * 100
    rep = round(rep, 2)
    disc = items.objects.filter(To_be_Discarded="True").count() / items.objects.count()
    disc = disc * 100
    disc = round(disc, 2)
    loan = items.objects.filter(Loaned="True").count() / items.objects.count()
    loan = loan * 100
    loan = round(loan, 2)
    cursor = connection.cursor()
    cursor.execute('select distinct Type from items')
    itemss = dictfetchall(cursor)
    ite = []
    for p in itemss:
        cou = items.objects.filter(Type = p['Type']).count()
        dicti = {'name':p, 'cout':cou}
        ite.append(dicti)
    return render(request,'dashboard/index.html',{'penreq':penreq, 'util':util, 'ite':ite, 'cond':cond, 'rep':rep, 'disc':disc, 'loan':loan})

def query(request):
    form = queryform(request.POST)
    if form.is_valid():
        item_no = form.cleaned_data['item_no']
        item = items.objects.get(id = item_no)
        if item.Loaned == 1:
            appr = approval.objects.get(item_no = item_no)
            ename = Employee.objects.get(Employee_Id = appr.emp_id)
            return render(request,'dashboard/info1.html',{'item':item, 'appr':appr, 'ename':ename})
        return render(request,'dashboard/info.html',{'item':item})
    return render(request,'dashboard/query.html',{'form':form})



def query1(request):
    cursor = connection.cursor()
    cursor.execute('select distinct Name from items')
    names = dictfetchall(cursor)
    cursor.execute('select distinct Type from items')
    types = dictfetchall(cursor)
    cursor.execute('select distinct id from items')
    ids = dictfetchall(cursor)
    cursor.execute('select distinct Bond_Id from items')
    bonds = dictfetchall(cursor)
    dicti = {'name1': "*", "type1": "*", "id1": "*","bond1":"*"}
    form = queryform2(request.POST)
    if form.is_valid():
        dicti['name1'] = form.cleaned_data['name2']
        dicti['type1'] = form.cleaned_data['type2']
        dicti['id1'] = form.cleaned_data['id2']
        dicti['bond1'] = form.cleaned_data['bond2']
    itemss = items.objects.filter()
    print(dicti['name1'],dicti['name1'])
    print(dicti['type1'])
    print(dicti['bond1'],dicti['bond1'])
    if(dicti['name1'] != "*"):
        itemss = itemss.filter(Name = dicti['name1'])
    if (dicti['id1'] != "*"):
        itemss = itemss.filter(id = dicti['id1'])
    if (dicti['bond1'] != "*"):
        itemss = itemss.filter(Bond_Id = dicti['bond1'])
    if (dicti['type1'] != "*"):
        itemss = itemss.filter(Type = dicti['type1'])
    return render(request,'dashboard/home.html',{'form':form, 'dicti':dicti, 'names':names, 'types':types, 'ids':ids, 'bonds':bonds, 'itemss':itemss})

def xyz(request):
    cursor = connection.cursor()
    cursor.execute('select distinct id from items')
    ids = dictfetchall(cursor)
    return render(request,'dashboard/xyz.html',{'ids':ids})