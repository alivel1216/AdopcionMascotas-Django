"""Adopcion Mascotas Views"""
#Django
from django.http import HttpResponse
#Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting"""
    now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hola joven, el tiempo del servidor es {now}'.format(now=str(now)))

def sorted_int(request):
    """Hi"""
    numbers =[int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data={
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorteed successfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say(request, name, age):
    """Say Hi """
    if age < 12:
        message ='Sorry {}, you not allowed'.format(name)
    else:
        message ='Hello {}, Wellcome!! '.format(name)
    
    return HttpResponse(message)