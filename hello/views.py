from django.shortcuts import render
from django.http import HttpResponse

def index(request, id, nickname):
  result = 'your id: ' + str(id) + ', name: "' + nickname + '".'

  return HttpResponse(result)
