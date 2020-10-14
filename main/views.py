from django.shortcuts import render,redirect,get_object_or_404
from .models import *

# Create your views here.

def show_about_page(request):
    return render(request,'main/about.html')

def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data = {
        'images':images,
        'cats':cats,
    }


    return render(request,'main/home.html',data)

def show_category_page(request,id):
    cats = Category.objects.all()
    category = Category.objects.get(pk=id)
    images = Image.objects.filter(cat=category)


    data = {
        'images':images,
        'cats':cats,
        
    }


    return render(request,'main/home.html',data)

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
      
        images = Image.objects.filter(title__icontains=q)
        
        context = {'query':q,'images':images}
        template = 'main/home.html'
    else:
        template = 'main/home.html'
        context = {}
    return render(request,template,context)



                    