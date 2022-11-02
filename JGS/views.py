import json
from pickle import NONE
import re
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib import messages
import requests
# Create your views here.

from api.models import Customer
import json

URL = "http://127.0.0.1:8000/api/"

def splash(request):
    return render(request,'splash.html')

def home(request):
    obj=Customer.objects.all()
    due_amount=0
    for i in obj:
        due_amount=due_amount+i.amount

    return render(request,'dashboard.html',{'total_due_amount':due_amount})

def insert_data(request):
    if(request.method=='POST'):
        name=request.POST['name']
        mobile=request.POST['mobile']
        note=request.POST['note']
        amount=request.POST['amount']

        if ( len(name)==0 ):
            messages.info(request, "Name is required")
            return redirect('insert')
        if ( len(mobile)==0 ):
            messages.info(request, "Mobile Number is required")
            return redirect('insert')
        if ( len(note)==0 ):
            messages.info(request, "Note is required")
            return redirect('insert')
        if ( len(amount)==0 ):
            messages.info(request, "Due Amount is required")
            return redirect('insert')

        if(len(mobile)!=10):
            messages.info(request, "Enter Valid Phone Number")
            return redirect('insert')


        data={'name':name,'mobile_number':mobile,'note':note,'amount':amount}
        json_data=json.dumps(data)
        
        headers={'content-Type':'application/json'}
        r=requests.post(URL,headers=headers,data=json_data)
        messages.info(request, "Data Added Successfully")
        return redirect("dashboard")
    return render(request,'insert_data.html')

def fetch(request,pk=None):
    data={}
    json_data=json.dumps(data)
    url=URL
    headers={'content-Type':'application/json'}
    if pk is not None:
        url=URL+str(pk)
        r=requests.get(url,headers=headers,data=json_data)
        data=[r.json()]

    else:    
        r=requests.get(URL,headers=headers,data=json_data)
        data=r.json()
   
    return render(request,'fulldata.html',{'context':data})



# jagdamba - 4277