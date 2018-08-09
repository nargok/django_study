from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  if 'msg' in request.GET:
    msg = request.GET['msg']
    result = 'you typed: "' + msg + '".'
  else:
    result = 'Please send message parameter!'

  return HttpResponse(result)
