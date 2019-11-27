from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination2
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
# from account.forms import DocumentForm

# from upload form
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import BookForm
from .models import Book, Category, Videos_sold

from moviepy.editor import *

def login(request):
    if request.method == 'POST': 
        username = request.POST['username']
#        email = request.POST['email']
        password = request.POST['password']  
        print('dentrode login 6666666666666666666666666666')

    
        user = authenticate(username=username,password=password)
        print('dentrode login 7777777777777777777777777777777')
        if user is not None:
            print('si user')
            auth.login(request,user)
            return redirect('index')
        else:
            print('invalid user')
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        print ('sali,noPOst1')
        return render(request,'login.html') 

    print('saliendo')
    return render(request,'login.html')

# Create your views here.
def register(request): 
    print('dentro')
    print(request.method)
    if request.method == 'POST': 
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name'] 
        username = request.POST['username']
        password1 = request.POST['password1']  
        password2 = request.POST['password2'] 
        email = request.POST['email']         
        print( first_name, last_name, email, 'mensajes')


        if password1 == password2 :
            print('111111111111111111111111111111111')
            if User.objects.filter(username=username).exists():
                print('user name taken')
                messages.info(request, 'user name taken' )
                return redirect('register')

            else:
                print('22222222222222222222222222222222222222222222')               
                user = User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save()
                print('user created')
                messages.info(request,'user created..' )
        else:
            print('password not matched..')
            messages.info(request,'password not matched..' )
            return redirect('register')
        return redirect('/index')
#        return redirect('')

    return render(request,'register.html')
#    return (request,'index.html')
#    return render(request,'home.html')

def courses(request):
    print('denteo course************########################################')    

#    books = Book.objects.filter(author=request.user)
    books = Category.objects.all()    
    return render(request,'courses.html', {'books': books})

# videos downloaded to be sold 
def my_account(request):
    print('denteo course************########################################')    

#    books = Book.objects.filter(author=request.user)
    videos = Book.objects.filter(author=request.user)  
    return render(request,'my_account.html', {'videos': videos})

def course_details(request,kategory):
    print('dentrrrrrrrrrrreo course************########################################')    
    j=1    
    obj = Category.objects.filter(id=1).first() 
    while str(obj) != str(kategory): 
        j+=1   
        obj = Category.objects.filter(id=j).first() 
        print(obj)
        print(j)
        print('next')

#    videos = Book.objects.filter(category=j).filter(author=request.user)   
    videos = Book.objects.filter(category=j)  
#    print(videos) 
    return render(request,'course_details.html', {'videos': videos})

def buy_video(request):
    videotobuy=Book.objects.filter(pk=2)
#    videotobuy.save()
    r=1
#    while r >0:
#        r+=1

    buyer=Videos_sold()
    buyer.save()
    buyer.videos_to_sell.add(videotobuy)
    print
    books = Category.objects.all()   
    return render(request,'index.html') 
    return render(request,'courses.html', {'books': books})

def videos(request):
    print('denteo course************########################################')    

#    cat = Category.objects.filter(author=request.user)
    categories = Category.objects.all()
    return render(request,'videos.html', {'categories': categories})

def index1(request):
    #    return HttpResponse("Hello, world. Tu Tu You're at the polls index.")

    print('tesststtttttttta*********##################4*****')
    return render(request,'index.html')


def logout(request):
    print('log')
    auth.logout(request)
    print('out')
    return redirect('/')  




# from upload form

# class Home(TemplateView):
#     template_name = 'home.html'


def home(request):
    #    return HttpResponse("Hello, world. Tu Tu You're at the polls index.")


    return render(request,'home.html')

def upload(request):
    print('check')
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        name_path=str("D:\\Python\\Anaconda\\New_Project\\project\\media\\") + str(name)
        print('clippppppppppppppppppppppppppppppppppppp')
 
        context['url'] = fs.url(name)
        print(name)
        print(fs.url(name))
        print(name_path)
#        clip = VideoFileClip(name_path)
#        clip = VideoFileClip("D:\Python\Anaconda\google\Alexis First Video.mov")
#       clip.save_frame("D:\\Python\\Anaconda\\google\\test\\thumbnail.jpg",t=2.00)

    return render(request, 'upload.html', context)


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author=request.user
            instance.save()
            print('LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL')

            uploaded_file = request.FILES['pdf']
#            dests = Book.objects.get()
#            print(dests.author)

            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })



def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'

################
