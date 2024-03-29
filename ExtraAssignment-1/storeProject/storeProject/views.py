from django.shortcuts import render, redirect
from myStore.models import *

def storePage(request):
    store=storeModel.objects.all()
    storedict={
        'store':store
    }
    return render(request, 'storePage.html',storedict)

def addStore(request):
    if request.method =='POST':
        sname=request.POST.get('storename')
        oname=request.POST.get('ownername')
        slocation=request.POST.get('location')

        addstore=storeModel(
            StoreName=sname,
            OwnerName=oname,
            StoreLocation=slocation,
        )
        addstore.save()
        
        return redirect('storePage')
        
    return render(request,'addStore.html')

def deleteStore(request,myid):
    deletestore=storeModel.objects.get(id=myid)
    deletestore.delete()
    return redirect('storePage')    

def editStore(request,myid):
    editstore=storeModel.objects.filter(id=myid)
    storedict={
        'store':editstore
    }
    return render(request,'editStore.html',storedict)

def updateStore(request):
    if request.method=='POST':
        sid=request.POST.get('storeid')
        sname=request.POST.get('storename')
        oname=request.POST.get('ownername')
        slocation=request.POST.get('location')
        
        updatestore=storeModel(
            id=sid,
            StoreName=sname,
            OwnerName=oname,
            StoreLocation=slocation,
        )
        updatestore.save()
        
        return redirect('storePage')
        
        
