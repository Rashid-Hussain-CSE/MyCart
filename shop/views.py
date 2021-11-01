from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from math import ceil

def index(request):
    products = Product.objects.all()
    n=len(products)
    print(products)
    params = {'range':range(n),'product' : products}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at Search")

def productView(request):
    return HttpResponse("We are at productView")

def checkout(request):
    return HttpResponse("We are at request")
 