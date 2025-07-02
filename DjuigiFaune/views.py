from django.shortcuts import render
from . models import*
# Create your views here.

def index(request):
    animaux=Animaux.objects.all().order_by("?")
    return render(request,"index.html",{"animaux":animaux})

def contact(request):
    
    return render(request,"contact.html",{})