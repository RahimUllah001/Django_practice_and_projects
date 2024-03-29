from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name = 'index'),       #when the first quotes are epmty it means root url
    path('counter', views.counter, name = 'counter'), 
    path('register', views.register, name = 'register'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('post/<str:pk>', views.post,name='post')
]