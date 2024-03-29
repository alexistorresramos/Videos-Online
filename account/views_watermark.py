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
from .models import Book, Category, Videos_sold, Buyer, News, Create_Watermark, Cart

from moviepy.editor import *
import moviepy.editor as mp

# from cart.cart import Cart
# from myproducts.models import Product

import ntpath
import os

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
    if request.user.is_authenticated:
        videos = Book.objects.filter(author=request.user)  
        return render(request,'my_account.html', {'videos': videos})
    else:
        return render(request,'login.html') 

def news_account(request):
    print('denteo course************########################################')    

    if request.user.is_authenticated:
        videos = News.objects.filter(news_station=request.user)  
        return render(request,'my_account.html', {'videos': videos})
    else:
        return render(request,'login.html') 



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

def buy_video(request,pk):

    print(pk)
    videotobuy=Book.objects.get(pk=pk) 
    videos=Cart()

    videos.title= videotobuy.title
    videos.category = videotobuy.category
    videos.author = videotobuy.author 
    videos.news_station = request.user
    videos.desc = videotobuy.desc
    videos.pdf = videotobuy.pdf
    videos.video_watermark = videotobuy.video_watermark    
    videos.price = videotobuy.price
    videos.price_exclusive = videotobuy.price_exclusive    
    videos.minutes_exclusive = videotobuy.minutes_exclusive

    videos.save()

    print
    print(request.user)
    print('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')

#    videos = Buyer.objects.get(news_name=6)
    videos = News.objects.filter(news_station=request.user)
    return redirect('cart')
#    return render(request,'course_details.html', {'videos': videos}) 


def videos(request):
    print('denteo course************########################################')    

#    pks=[24,25]
#    for i in range(len(pks)):
#        categories = Book.objects.filter(pk=pks[i]).update(attr=i) 
#        categories.save()

#    categories = Book.objects.filter(id)
#    categories = Book.objects.filter(id=25).filter(id=25)
#   categories2 = Book.objects.filter(id=25)   
#    categories=categories1 + categories2
    categories = Book.objects.filter(id__in=25) 
    print(categories)  

#    cat = Category.objects.filter(author=request.user)

#    categories = Book.objects.filter(pk=['24','25'])
#    categories = Book.objects.filter(news_name=request.user)
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

def cart(request):
    books = Cart.objects.all()
    return render(request, 'cart.html', {
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

#            uploaded_file = request.FILES['pdf']
#            dests = Book.objects.get()
#            print(dests.author)
            videos=Create_Watermark()
            videos.pkin= instance.pk
            videos.save()
            print(videos.pkin, 'pkpkpkpkkpkpkp')

            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', { 'form': form  })



def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


def delete_cart(request, pk):
    if request.method == 'POST':
        book = Cart.objects.get(pk=pk)
        book.delete()
    return redirect('cart')

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

def Watermark(request):
                
    videos=Create_Watermark.objects.all()
    i=1
    #add_to_cart(request, 1, 1)
    
    for video in  videos:
        video_pk = video.pkin
        pk_watermark=video.id
        original_video= Book.objects.get(pk=video_pk)
        video_to_watermark = str(original_video.pdf)

        print(i,'iiiiiiiiiiiiiiiiiiiiiii')
        print(video_to_watermark)

        name_path=str("D:\\Python\\Anaconda\\New_Project\\project\\media\\") + str(video_to_watermark)

        print('ggggggg', name_path)
        video_prepare = VideoFileClip(name_path)

    #    logo = TextClip("This is Watermark",fontsize=70,color='white')
    #    logo = logo.set_pos('center').set_duration(video.duration)    
        logo = (ImageClip("D:\\Python\\Anaconda\\New_Project\\project\\logo\\android.png")
    #    logo = (("Watermark")
                .set_duration(video_prepare.duration)
                .resize(height=200) # if you need to resize...
    #            .margin(right=8, top=8, opacity=70) # (optional) logo-border padding
    #            .set_pos(("right","top")))
                .set_pos(("center","center",)))

 #########################
        print('watermark text')
        my_clip  = VideoFileClip(name_path)

        w,h = my_clip.size  # size of the clip

        # A CLIP WITH A TEXT AND A BLACK SEMI-OPAQUE BACKGROUND

        txt = TextClip("THE WATERMARK TEXT", font='Amiri-regular',
                        color='white',fontsize=24)

        txt_col = txt.on_color(size=(my_clip.w + txt.w,txt.h-10),
                        color=(0,0,0), pos=(6,'center'), col_opacity=0.6)

        # This example demonstrates a moving text effect where the position is a function of time(t, in seconds).
        # You can fix the position of the text manually, of course. Remember, you can use strings,
        # like 'top', 'left' to specify the position
        txt_mov = txt_col.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)),
                                        max(5*h/6,int(100*t))) )


        final = CompositeVideoClip([my_clip,txt_mov])

#########################################
#        final = CompositeVideoClip([video_prepare, logo])
    #    final = mp.CompositeVideoClip([video, "logo"])
#        head, tail = os.path.split(video_to_watermark)

        base=os.path.basename(video_to_watermark)
        tail = os.path.splitext(base)
        tail = os.path.splitext(base)[0]

#        tail = os.path.splitext(video_to_watermark)[0]
####        print(os.path.splitext("/path/to/some/file.txt")[0])
        print(tail,'tailllll')
        watermark_path= str("D:\\Python\\Anaconda\\New_Project\\project\\media\\") 
#        final.write_videofile("D:\\Python\\Anaconda\\New_Project\\project\\logo\\test.mp4")
        DB_watermark_path =  watermark_path + str('books\\watermark\\')+ str(tail) + str('.MP4')
        print(DB_watermark_path)
#        final.write_videofile(DB_watermark_path)
        final.write_videofile(DB_watermark_path, threads=4)
        original_video.video_watermark=DB_watermark_path
        original_video.save()

##        Create_Watermark.objects.filter(pk=pk_watermark).delete()
    return redirect('index')

def add_to_cart(request, product_id, quantity):
#    product = News.objects.get(id=product_id)
    product = News.objects.get(id=10)
    cart = Cart(request)
    print('paseeeeee')
    cart.add(product, product.price, quantity)


def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

def get_cart(request):
    return render(request, 'cart.html', {'cart': Cart(request)})
