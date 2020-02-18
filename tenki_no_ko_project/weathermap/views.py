import urllib.request
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

# Create your views here.

TOKEN = '8efabdb7c4a00c765d7816f3ae2310ad'

def request_data(url) :
    response = urllib.request.urlopen(url)
    byte_data = response.read()
    text_data = byte_data.decode('utf-8')
    return text_data

def build_url(city) :
    return f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={TOKEN}'

@csrf_exempt
def message(request):                                         # POST 형식이었을 때의 반환
    if request.method == "POST" :
        json_str = ((request.body).decode('utf-8'))
        received_json_data = json.loads(json_str)
        datacontent = received_json_data['userRequest']['utterance'].split()[0]
        par = received_json_data['action']['params']
        
        try : 
            city_name = par['custom_city'].split()[0]
            current_weather = json.loads(request_data(build_url(city_name)))['weather'][0]['main']                                # 현재기후
            current_temperature = str(round(int(json.loads(request_data(build_url(city_name)))['main']['temp']) - 273.15,1))      # 현재기온
            feel_temperature = str(round(int(json.loads(request_data(build_url(city_name)))['main']['feels_like']) - 273.15,1))   # 체감기온
            response_body= {
            'version': '2.0',
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': "현재 " + datacontent + "의 날씨는 " + current_weather + "이며 기온은 " + current_temperature + "°C입니다! " + "체감기온은 " + feel_temperature + "°C입니다!"
                        }
                    }
                ]
            }
        }
        except KeyError :         # city_name = par['custom_city'].split()[0] 값이 없어서 에러가 뜬 경우 실행
            response_body= {
            'version': '2.0',
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': datacontent + "?"
                        }
                    }
                ]
            }
        }
        return JsonResponse(response_body)
    
    else : return HttpResponse("Success")                      # GET 형식이었을 때의 반환   