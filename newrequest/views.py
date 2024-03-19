from django.shortcuts import render
from adminprofile.models import items
from .forms import NewRequestForm
from django.db import connection
import datetime
# Create your views here.
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns,row))
        for row in cursor.fetchall()
    ]
def home(request):
    user_list = request.session.get('user_list', None)
    eid = user_list[0]
    req_id = request.session.get('req_id')
    if not req_id:
        req_id = 1;
    form = NewRequestForm(request.POST)
    if form.is_valid():
        req_id = req_id+1;
        request.session['req_id'] = req_id
        form.save()
    cursor = connection.cursor()
    cursor.execute('select distinct Name from items')
    itemss = dictfetchall(cursor)
    args = {
        'form' : form,
        'itemss':itemss,
        'eid' : eid,
        'requestid' : req_id
    }
    return render(request,'newrequest/home.html',args)