from django.shortcuts import render, get_object_or_404, redirect
from web.models import Ciudad
from django.contrib.auth.decorators import login_required
import requests
from .weather_api import get_clima, get_geo

# Create your views here.
def home(request):
    ciudades = Ciudad.objects.all()
    return render(request,'home.html',{'ciudades':ciudades})

@login_required
def ciudad_detail(request,ciudad_id):
    if request.method == 'GET':
        ciudad = get_object_or_404(Ciudad, id=ciudad_id)
        geo = get_geo(ciudad.name)
        clima = get_clima(geo['lon'],geo['lat'])
        info = geo | clima
        return render(request,'ciudad_detail.html', {'ciudad':ciudad,'info':info})
    else: 
        return redirect('index.html')
    

def chile(request):
    return render(request,'chile.html')

def about(request):
    return render(request,'about.html')

def ciudades(request):
    ciudades = Ciudad.objects.all()
    return render(request,'ciudades.html',{'ciudades':ciudades})
