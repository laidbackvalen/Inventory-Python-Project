from django.shortcuts import render, redirect
from .models import useradmin, returnmodel, items
from adminrequest.models import approval
from .forms import returnform
# Create your views here.
def home(request):
    user_list = request.session.get('user_list', None)
    eid = user_list[0]
    context = useradmin.objects.get(pk=eid)
    args = {
        'eid': eid,
        'name': context.name,
        'email': context.emailaddress
    }
    return render(request,'adminprofile/home.html',args)

def adminreturn(request):
    form = returnform(request.POST)
    if form.is_valid():
        if not approval.objects.filter(item_no = form.cleaned_data['item_no']).exists():
            return redirect('./')
        i = form.cleaned_data['item_no']
        appr = approval.objects.get(item_no = i)
        appr.delete()
        ite = items.objects.get(id= i)
        ite.Condition = form.cleaned_data['Condition']
        ite.Loaned = 0
        ite.In_use = 0
        ite.save()
        return redirect('./')
    return render(request,'adminreturn/home.html',{'form':form})