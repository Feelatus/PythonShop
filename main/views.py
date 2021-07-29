from django.shortcuts import render
from .models import Category, Product, SliderAdd, SliderHome


def home (request):
    slideradd = SliderAdd.objects.order_by('name')
    sliderhome = SliderHome.objects.order_by('name') 
    context = {'slideradd': slideradd, 'sliderhome': sliderhome}
    return render(request, 'home/home.html', context)


def catalog_list (request):
    category = Category.objects.order_by('name')
    product = Product.objects.order_by('name')
    context = {'product': product, 'category': category}
    return render(request, 'catalog/catalog.html', context )



