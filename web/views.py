from django.shortcuts import render, get_object_or_404
from web.models import Ciudad
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    ciudades = Ciudad.objects.all()
    return render(request,'home.html',{'ciudades':ciudades})

@login_required
def ciudad_detail(request,ciudad_id):
    ciudad = get_object_or_404(Ciudad, id=ciudad_id)
    return render(request,'ciudad_detail.html', {'ciudad':ciudad})

def chile(request):
    return render(request,'chile.html')

def about(request):
    return render(request,'about.html')

def ciudades(request):
    ciudades = Ciudad.objects.all()
    return render(request,'ciudades.html',{'ciudades':ciudades})