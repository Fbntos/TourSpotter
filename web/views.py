from django.shortcuts import render, get_object_or_404, redirect
from web.models import Ciudad
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .weather_api import get_clima, get_geo 


# Create your views here.
def home(request):
    # METODO ALL -> Me retorna un QuerySet con todos los registros.
    # ciudades = Ciudad.objects.all() # -> QuerySet -> Objeto Empaquetado 
    # for city in ciudades:     
    #     print(f'{city.name}')  # -> Desempaquetando el QuerySet


    # METODO GET -> Me retorna un OBJETO que coincida.
    # ciudad = Ciudad.objects.get(id = 1)


    # METODO FILTER(where) -> Me retorna un QuerySet con los registros que coincidan
    ciudades = Ciudad.objects.filter(is_active = True)
    #ciudades = Ciudad.objects.filter(is_active = True, name = 'Valdivia') # -> Filter con doble condición
    

    # METODO UPDATE -> Se puede aplicar el metodo update a un QuerySet, el filter funciona como where.
    # ciudad = Ciudad.objects.filter(id=4).update(id=14)

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

def registro(request):
    if request.method == "POST":
        user = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf_password']

        if password == conf_password:
            try:
                User.objects.create_user(
                    username=user,
                    password=password,
                    email=email)
                return redirect('/login')
            except IntegrityError:
                error_message = "El nombre de usuario o correo electrónico ya está en uso."
                return render(request, 'registration/registro.html', {'error_message': error_message})
        else:
            error_message = "Las contraseñas no coinciden."
            return render(request, 'registration/registro.html', {'error_message': error_message})
    else: 
        return render(request, 'registration/registro.html')
    
