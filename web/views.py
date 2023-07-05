from django.shortcuts import render, get_object_or_404
from web.models import Ciudad
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    ciudades = Ciudad.objects.all()
    return render(request,'home.html',{'ciudades':ciudades})


def ciudad(request):
    # ciudad = get_object_or_404(Ciudad, id=ciudad_id)
    return render(request,'ciudad.html')

def chile(request):
    return render(request,'chile.html')