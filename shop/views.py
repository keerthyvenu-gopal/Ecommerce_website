from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

def home(request,c_slug=None):
    c_page=None
    prod=None
    if c_slug!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        prod=product.objects.filter(categ=c_page,available=True)
    else:
        prod=product.objects.all().filter(available=True)
    cat=category.objects.all()
    paginator=Paginator(prod,3)
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request,'home.html',{'pr':prod,'ct':cat,'pg':pro})

def prodview(request,c_slug,prod_slug):
    try:
        prodt=product.objects.get(categ__slug=c_slug,slug=prod_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'pr':prodt})

def searching(request):
    prodt=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prodt=product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    else:
        messages.info(request, "Invalid data")
    return render(request,'search.html',{'qr':query,'pr':prodt})