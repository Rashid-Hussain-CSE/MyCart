from django.shortcuts import render
from .models import Product
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
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def productView(request):
    return render(request,'shop/productView.html')

def checkout(request):
    return render(request,'shop/checkout.html')
 