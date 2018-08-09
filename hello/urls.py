from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/<nickname>', views.index, name='index'),
]
