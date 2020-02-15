from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

TOKEN = '8efabdb7c4a00c765d7816f3ae2310ad'

def request(url) :
    response = urllib.request.urlopen(url)
    byte_data = response.read()
    text_data = byte_data.decode('utf-8')
    return text_data

def build_url(city) :
    return f'api.openweathermap.org/data/2.5/weather?q={city}&appid={TOKEN}'

@csrf_exempt
def request_to_weather(request) :
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    userMessage = received_json_data['content'] 

    url = build_url(userMessage)
    response = request(url)
    return json.loads(response)
