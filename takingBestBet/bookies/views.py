from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return render(request, 'bookies/index.html')

def init(request):
    response = {"text": "place holder"}
    return HttpResponse(json.dumps(response), content_type='application/json')

def requestOdds(request):
    response = {"text": "place holder"}
    return HttpResponse(json.dumps(response), content_type='application/json')
