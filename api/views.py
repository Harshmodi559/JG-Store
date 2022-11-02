from django.shortcuts import render

# Create your views here.
from pickle import NONE
from matplotlib.cbook import report_memory

from rest_framework.decorators import api_view
from django.shortcuts import render
from yaml import serialize
from .serializers import CustomerSerializer
from .models import Customer
from django.contrib import messages
from rest_framework.response import Response

@api_view(['GET','POST','DELETE','PUT','PATCH'])   ## be defalult ->get 
def api(request,id=NONE):
    
    
    if(request.method=='POST'): 
        body=request.data

        serializer=CustomerSerializer(data=body)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    if request.method=='GET':
        if id is not NONE:
            obj=Customer.objects.get(id=id)
            serializer=CustomerSerializer(obj)
            if(obj is not None):
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        obj=Customer.objects.all()
        serializer=CustomerSerializer(obj,many=True)
        return Response(serializer.data)
    

    # if(request.method=='PUT'): 
    if(request.method=='DELETE'): 
        if id is not None:
            obj=Customer.objects.get(id=id)
            if(obj is not None):
                obj.delete()
                return Response("Data Deleted")
            return Response('not found')
    # if(request.method=='PATCH'): 




