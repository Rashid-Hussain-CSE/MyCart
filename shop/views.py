from django.shortcuts import render
from .models import Product, Contact
from django.http import HttpResponse
from math import ceil

def index(request):
    products = Product.objects.all()
    print(products)
    params = {'product' : products}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=="POST":
        _name = request.POST.get('name','')
        _email = request.POST.get('email','')
        _phone = request.POST.get('phone','')
        _desc = request.POST.get('desc','')
        contact = Contact(name=_name, email=_email, phone=_phone, desc=_desc)
        contact.save()
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def productView(request,_id):
    # fetch the product using id
    product = Product.objects.filter(id=_id)
    return render(request,'shop/productView.html',{'product':product[0]})

def checkout(request):
    return render(request,'shop/checkout.html')
 