from django.shortcuts import render
import requests
import json
from .api import ClanWars

instance = ClanWars()

# Create your views here.
def getStatus(request):
    result = instance.get_status()
    return render(request, 'clanwars/status.html',{
        'success':result['success'], 
        'data': result['data']['status'],
        'appVersion': result['appVersion']
        })
   
def getUser(request):
    result = instance.get_user()
    #print(result)
    return render(request,'clanwars/user.html',{'result': result['data']})