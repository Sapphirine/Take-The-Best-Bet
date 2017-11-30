from django.shortcuts import render
from django.http import HttpResponse
from .odds import get_soccer_leagues, get_odds
import json

# Create your views here.
def index(request):
    return render(request, 'bookies/index.html')

def init(request):
    response = get_soccer_leagues()
    print (json.dumps(response, indent=2))
    return HttpResponse(json.dumps(response), content_type='application/json')

def requestOdds(request):
    sport = request.GET['sport']
    region = request.GET['region']
    response = get_odds(sport, region)
    #print (json.dumps(response, indent=2))
    return HttpResponse(json.dumps(response), content_type='application/json')
