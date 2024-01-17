from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name = 'index')       #when the first quotes are epmty it means root url
]