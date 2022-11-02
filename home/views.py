from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_lastfm(request):
    url = 'http://ws.audioscrobbler.com/2.0/?'
    params = {
        'method': 'user.getweeklyartistchart',
        'user': 'matairak',
        'api_key': settings.API_KEY_LASTFM,
        'format': 'json'
    }
    response = requests.get(url, params)
    
    if response.status_code == 200:
        #print("sucessfully fetched the data")
        #self.formatted_print(response.json())
        return HttpResponse(response)
    else:
        #print(f"Hello person, there's a {response.status_code} error with your request")
        return HttpResponse('não foi dessa vez')