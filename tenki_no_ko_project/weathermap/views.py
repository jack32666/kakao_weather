import urllib.request
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpRequest

# Create your views here.

TOKEN = '8efabdb7c4a00c765d7816f3ae2310ad'

def request(url) :
    response = urllib.request.urlopen(url)
    byte_data = response.read()
    text_data = byte_data.decode('utf-8')
    return text_data

def build_url(city) :
    return f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={TOKEN}'

def request_to_weather(req) :
    url = build_url(req)
    response = request(url)
    return json.loads(response)

def keyboard(request):
 
        return JsonResponse({
                'type' : 'buttons',
                'buttons' : ['1','2']
                })

@csrf_exempt
def message(request):
        message = ((request.body).decode('utf-8'))
        return_json_str = json.loads(message)
        return_str = return_json_str['content']
 
        return JsonResponse({
                'message': {
                        'text': "you type "+return_str+"!"
                },
                'keyboard': {
                        'type': 'buttons',
                        'buttons': ['1','2']
                }
        })
