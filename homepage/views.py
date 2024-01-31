from django.contrib import auth
from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import signUpForm
# Create your views here.

def index(request):
    items=Item.objects.order_by('-created_at').filter(is_sold=False)[0:8]
    categories=Category.objects.all()
    return render(request,'homepage/index.html',{'categories':categories,
                                                 'items':items})

def contact(request):
    return render(request,'homepage/contact.html')

def signup(request):
    if request.method=='POST':
        form=signUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = signUpForm()

    return render(request,'homepage/signup.html',{
        'form':form
    })

def logout(request):
    auth.logout(request)
    return redirect('homepage:index')