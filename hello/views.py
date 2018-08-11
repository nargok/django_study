from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm

def index(request):
  params = {
    'title':'Hello/Index',
    'message': 'your data:',
    'form': HelloForm()
  }

  if (request.method == 'POST'):
    params['message'] = '名前: ' + request.POST['name'] + \
                        '<br>メール: ' + request.POST['mail'] + \
                        '<br>年齢: ' + request.POST['age']

    # 入力されたときの値をformに保持する
    params['form'] = HelloForm(request.POST)

  return render(request, 'hello/index.html', params)