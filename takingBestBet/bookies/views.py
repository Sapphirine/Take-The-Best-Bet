from django.shortcuts import render
from django.http import HttpResponse
from .odds import get_soccer_leagues, get_odds
from operator import add
import json, numpy

# Create your views here.
def index(request):
    return render(request, 'bookies/index.html')

def init(request):
    response = get_soccer_leagues()
    #print (json.dumps(response, indent=2))
    return HttpResponse(json.dumps(response), content_type='application/json')

def requestOdds(request):
    sport = request.GET['sport']
    region = request.GET['region']
    response = get_odds(sport, region)
    data = response['data']['events']
    for i in data:
        a = [0] * 3
        cnt = 0
        for j in data[i]['sites']:
            odds = data[i]['sites'][j]['odds']['h2h']
            if len(odds) < 3:
                continue
            cnt += 1
            for k in range(3):
                a[k] += float(odds[k])
        for k in range(3):
            a[k] /= cnt
            a[k] = 1/a[k]
            if a[k] > 0.2:
                a[k] *= 0.75
            else:
                a[k] *= 0.98
            a[k] = 1/a[k]
            a[k] = format(a[k], '.2f')
        data[i]['p_odds'] = [str(x) for x in a]
    return HttpResponse(json.dumps(response), content_type='application/json')

