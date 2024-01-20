from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    features = Feature.objects.all()
  
    return render(request, 'index.html', {'features': features}) 

    
def counter(request):
    words = request.POST['text']
    amount_of_words = len(words.split())

    return render(request,'counter.html', {'amount': amount_of_words})   

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password= request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already use')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exist')
            else:
                user = User.objects.create_user(username=username, email = email,password = password)    
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'password not the same') 
            return redirect('register')   


    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password= request.POST['password']
        
        user = auth.authenticate(username = username,password = password ) 
 
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Credential Ivalid') 
            return redirect ('login')       
    else:
        return render(request, 'login.html')