from django.shortcuts import render
from web.models import Ciudad

# Create your views here.
def home(request):
    ciudades = Ciudad.objects.all()
    return render(request,'home.html',{'ciudades':ciudades})

