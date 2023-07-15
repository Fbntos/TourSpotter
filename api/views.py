'''
Creación de mini API de prueba para consumo e inserción de algunas ciudades en la bd de la web.
'''

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from web.models import Ciudad

# Para excluir una vista o una función de la protección CSRF (Cross-Site Request Forgery) proporcionada por Django. (CSRF TOKEN)
@csrf_exempt
def get_all(request):
    """
    Vista que retorna o ingresa una ciudad en la base de datos, dependiendo si el metodo es GET o POST.

    IN GET:
        Retorna un JSON con la información de todas las personas de la base de datos.
    IN POST: 
        Agrega una persona a la base de datos. 
    """
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        img_url = request.POST['img_url']
        is_active = request.POST['is_active']
        ciudad = Ciudad.objects.create(
            name = name, 
            desc = desc,
            img_url = img_url,
            is_active = is_active
        )
        return HttpResponse('Ciudad ingresada!')
    else:
        ciudades = Ciudad.objects.all()
        json = {}
        for x,c in enumerate(ciudades):
            json[c.id] = {'name':c.name,
                          'desc':c.desc,
                          'img_url':c.img_url,
                          'is_active':c.is_active}
        return JsonResponse({'ciudades':json})


def filter(request, name):
    """ 
    Vista que recibe el nombre de una ciudad en la url para buscarla en la BD.

    Args:
        name (str): nombre de la ciudad.
    
    Returns: 
        Json con la información de la ciudad.
    """
    if request.method == 'GET':
        ciudad = Ciudad.objects.get(name = name.capitalize())
        json = {
            'name':ciudad.name,
            'desc':ciudad.desc,
            'img_url':ciudad.img_url,
            'is_active':ciudad.is_active
        }
        return JsonResponse(json)
    # Pendiente la respuesta si no se encuentra la ciudad
    else:
        return HttpResponse('Metodo POST no permitido')
