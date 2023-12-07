from django.urls import path
from . import views

urlpatterns = [
    #path("endereço/", MinhaView.as_view(), name='nome da url')
    path("", views.index, name='inicio'),
]