from django.shortcuts import render

def index(request):
    appid = '8561ee4246a907b4d7596a1a456c1095'
    url = 'api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid


    city = 'Tomsk'


    return render(request, 'weather/index.html')