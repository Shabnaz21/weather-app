from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup as bs

def get_weather_data(city):
    city = city.replace(' ', '+')
    url = f'https://www.google.com/search?q=weather+of+{city}'
    USER_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    LANGUAGE = 'en-US,en;q=0.9'
    encoding = 'accept-encoding'
    cookie = 'OTZ=6868175_32_32__32_; SID=TghLc9H-ClgkJP1fGGPh204rwj6z6YI28rIVc3cbhOwGhp5z5sozcPpZ1a8nEh6fqIIONQ.; __Secure-1PSID=TghLc9H-ClgkJP1fGGPh204rwj6z6YI28rIVc3cbhOwGhp5zBJeCfSWOkEc32QZ_SqDffQ.; __Secure-3PSID=TghLc9H-ClgkJP1fGGPh204rwj6z6YI28rIVc3cbhOwGhp5zDNJleDuideCHDA8pd5rgiQ.; HSID=AqLw3fsn13LhegaUp; SSID=A2yWyj-FfCkwV0WjA; APISID=RdJtZnQ_7pp8Brd_/Asw5Pct80egSc_R84; SAPISID=nWD20k6jmERNV5FV/ADtqpNXuCubiu7XGB; __Secure-1PAPISID=nWD20k6jmERNV5FV/ADtqpNXuCubiu7XGB; __Secure-3PAPISID=nWD20k6jmERNV5FV/ADtqpNXuCubiu7XGB; GOOGLE_ABUSE_EXEMPTION=ID=93be5965e3f0fe4b:TM=1676116452:C=c:IP=43.245.140.166-:S=K5HSQZm6VmW2q4xWPQtFaA; OGPC=19033690-2:; OGP=-19033690:; SEARCH_SAMESITE=CgQIz5cB; NID=511=mNKJ1ZO75tCWprVTUwp9w0UYha25feivEsLYRAV7NVO1LuhrHCOcN21e39ykpST3zSzYtrRzDROg2y3Yr435Fc8M7uH469pTTmVvqCsB8RxrUbL1Jdh-4Bt5IhY3T-b7ndKKR4GYiU6AhVngLN8pZ5E4H45vBgYc5rxpSYjHgzFiGe8wb3Cb4OF_glQv9oOsUgx1J7Py5Ti-IqbZs7YByItGhAYsMwzUFfcnvTG6dOnjCVq9gCxAdXG9Ga1Xc7L84mevzKFVKZhwt6w-DahdDaQYCbfeaAa1wlnX_dlGY0P_xP7rKbOtk161V2YJ6Q3Z4BvnVhnPiTUVYwyLTt2slCC4Ws5T-JhcmpsJEHfMxw; AEC=ARSKqsKejkeRc9NVNU0D8E6HaPYcFCR05hr9JsVCpciqy6uCxmKs16bBdA; 1P_JAR=2023-02-19-07; SIDCC=AFvIBn_kO65MBFy_rR3wt5mTs3v8SbYE8tJTeqckaKJM_Far0_qK4VCd6GaNcohwzcEf2rjpTWqN; __Secure-1PSIDCC=AFvIBn_h_ETk2vtkUcZAs1VYJcfwZFP2RW-J367wpDDdbUWaO8hEA5TWKzxCn7LHABAzMIBkeX4i; __Secure-3PSIDCC=AFvIBn_E83Go0irB6xZwJibD50ci-Cy1duX5f7fSVzI5r2W_QwZaFXwAPfTUsSD5KZceMjV8kV1W'
    session = requests.session()
    session.headers['user-agent'] = USER_Agent
    session.headers['accept-language'] = LANGUAGE
    session.headers['accept-encoding'] = encoding
    session.headers['cookie'] = cookie
    response = session.get(url)
    soup = bs(response.text, 'html.parser')
    result = {}
    result['region'] = soup.find('span', attrs={'class': 'BBwThe'}).text
    result['datetime'] = soup.find('div', attrs={'id': 'wob_dts'}).text
    result['weather'] = soup.find('span', attrs={'id': 'wob_dc'}).text
    result['temp'] = soup.find('span', attrs={'id': 'wob_tm'}).text

    print(result)
    return result

# Create your views here.

def show(request):
    if request.method == 'GET' and 'city' in request.GET:
        city = request.GET.get('city')
        results = get_weather_data(city)
        context ={'results': results}
    else:
        context= {}
    return render(request, 'home.html', context)

