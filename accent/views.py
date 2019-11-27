from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):
    #    return HttpResponse("Hello, world. Tu Tu You're at the polls index.")
    dest = Destination()
    print('pruebbbbbba*********##################4*****')
    return render(request,'index.html')

def index1(request):
    #    return HttpResponse("Hello, world. Tu Tu You're at the polls index.")

    print('tesststtttttttta*********##################4*****')
    return render(request,'index.html')

def courses(request):
    print('denteo course########################################')    
#    return HttpResponse("Hello, world. Tu Tu You're at the polls index.")
    dests = Destination.objects.all()
#    dests = Book.objects.all()
#    dest1 = Destination()
#    dest1.name = 'Ingles'
#    dest1.img = 'p1.jpg' 
#    dest1.desc = 'Engish Class'
#    dest1.price = 500
#    dest1.offer = False
#    dests = [dest1, dest2, dest3, dest4]

#    return render(request,'courses.html', {'dest1': dest1})
    return render(request,'courses.html', {'dests': dests})

#    return render(request,'courses.html')

def login2(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']  

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            print('si user')
            auth.loogin(request,user)
            return redirect('index')
        else:
            print('invalid user')
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        print ('sali,noPOst')
        return render(request,'login') 

    print('saliendo')
    return render(request,'login.html')

# Create your views here.

