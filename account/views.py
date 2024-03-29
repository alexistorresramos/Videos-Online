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

from .forms import BookForm, PaymentForm, UserForm, UserProfileForm
from .models import Book, Category, Videos_sold, Buyer, News, Create_Watermark, Cart, User_Info, Profile, UserProfile, Account, Country, News_Type

from moviepy.editor import *
import moviepy.editor as mp

from datetime import date
from django.urls import reverse

from .forms import CheckoutForm, ExtendedUserCreationForm, UserProfileForm
from django.views.generic import ListView, DetailView, View
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

  
from django.db.models import Q, Count
#from rest_framework import generics
#from rest_framework.response import Response
#from .serializers import JournalSerializer

# from django_countries.fields import CountryField
#from django_countries.serializer_fields import CountryField


# from cart.cart import Cart
# from myproducts.models import Product

import ntpath
import os
from account.models import Country

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
def register_buyer(request): 
    print('dentro')
    print(request.method)
    if request.method == 'POST': 
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
#        first_name = request.POST['first_name'] 
#        last_name = request.POST['last_name'] 
        if form.is_valid() and profile_form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  
            password2 = form.cleaned_data.get('password1') 
            email = form.cleaned_data.get('email')         
            print(email, 'mensajes')
            if password == password2 :
                print('111111111111111111111111111111111')
                if User.objects.filter(username=username).exists():
                    print('user name taken')
                    messages.info(request, 'user name taken' )
                    return redirect('register_buyer')

                else:
                    print('22222222222222222222222222222222222222222222')  
                    user = form.save()

                    profile = profile_form.save(commit=False)
                    profile.user = user
                    profile.if_seller = True
                    profile.save()

                    user = authenticate(username=username, password=password)
    ##                login(request, user)
    #                user = User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                    user.save()
                    print('user created')
    #                profile = profile_form.save(commit=False)
    #               profile.user =user
    #                profile.save

                    messages.info(request,'user created..' )
                    auth.login(request,user)
                    return redirect('index')
            else:
                print('password not matched..')
                messages.info(request,'password not matched..' )
                return redirect('register_buyer')
        
        print('Invalid parameter..')
        messages.info(request,'Invalid parameter..' )        
        return redirect('register_buyer')
#        return redirect('')
    form = ExtendedUserCreationForm()
    profile_form= UserProfileForm()
    context ={'form':form, 'profile_form':profile_form}
    return render(request,'register.html',context)
#    return (request,'index.html')
#    return render(request,'home.html')

# Create your views here.
def register_seller(request): 
    print('dentro')
    print(request.method)
    if request.method == 'POST': 
        form = ExtendedUserCreationForm(request.POST)
###        profile_form = UserProfileForm(request.POST)
#        first_name = request.POST['first_name'] 
#        last_name = request.POST['last_name'] 
###        if form.is_valid() and profile_form.is_valid():
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  
            password2 = form.cleaned_data.get('password1') 
            email = form.cleaned_data.get('email')         
            print(email, 'mensajes')
            if password == password2 :
                print('111111111111111111111111111111111')
                if User.objects.filter(username=username).exists():
                    print('user name taken')
                    messages.info(request, 'user name taken' )
                    return redirect('register_seller')

                else:
                    print('22222222222222222222222222222222222222222222')  
                    user = form.save()

###                    profile = profile_form.save(commit=False)
###                    profile.user = user
###                    profile.save()

                    user = authenticate(username=username, password=password)
    ##                login(request, user)
    #                user = User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                    user.save()

                    profile = UserProfile()
                    profile.user = user
                    profile.if_seller = False
                    profile.save()

                    print('user created')
    #                profile = profile_form.save(commit=False)
    #               profile.user =user
    #                profile.save

                    messages.info(request,'user created..' )
                    auth.login(request,user)
                    return redirect('index')
            else:
                print('password not matched..')
                messages.info(request,'password not matched..' )
                return redirect('register_seller')
        
        print('Invalid parameter..')
        messages.info(request,'Invalid parameter..' )        
        return redirect('register_seller')
#        return redirect('')
    form = ExtendedUserCreationForm()
    profile_form= UserProfileForm()
    context ={'form':form, 'profile_form':profile_form}
    return render(request,'register_seller.html',context)
#    return (request,'index.html')
#    return render(request,'home.html')

def registration(request):
    #    return HttpResponse("Hello, world. Tu Tu You're at the polls index.")


    return render(request,'registration.html')

def buy_videos(request):
    print('denteo course************########################################')    

#    books = Book.objects.filter(author=request.user)
    books = Category.objects.all().order_by('category')     
    return render(request,'buy_videos.html', {'books': books})

# videos downloaded to be sold 
def my_account(request):
    print('denteo course************########################################')    

#    books = Book.objects.filter(author=request.user)
    if request.user.is_authenticated:
        videos_list = Book.objects.filter(author=request.user)  

    else:
        return render(request,'login.html') 

    page = request.GET.get('page',1)
    paginator = Paginator(videos_list, 20)   # num of videos per page
    print(page)
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)
    return render(request,'my_account.html', {'videos': videos})


def news_account(request):
    print('denteo course************########################################')    

    if request.user.is_authenticated:

        check_user = UserProfile.objects.get(user_id=request.user)
        if check_user.if_seller == False:   # if false means it is seller 
            videos_list = Book.objects.filter(author=request.user)
        else:  
            videos_list = News.objects.filter(news_station=request.user).order_by('-incident_date') 

    else:
        return render(request,'login.html') 

    page = request.GET.get('page',1)
    paginator = Paginator(videos_list, 20)   # num of videos per page
    print(page)
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)
    return render(request,'my_account.html', {'videos': videos})

#  @login_required
def course_details(request,kategory):
    print('dentrrrrrrrrrrreo course************########################################')    
    
    if request.user.is_authenticated:
        j=1
        check_user = UserProfile.objects.get(user_id=request.user)
        print(request.user)
#        check_user = UserProfile.objects.get(user_id=14)
        if check_user.if_seller == False:
            print('noo es sellerrrrrrrrrrrrrrrrrrrrrr')
            return render(request,'not_buyer.html')
        obj = Category.objects.filter(id=1).first() 
        while str(obj) != str(kategory): 
            j+=1   
            obj = Category.objects.filter(id=j).first() 
            print(obj)
            print(j)
            print('next')

    #    videos = Book.objects.filter(category=j).filter(author=request.user)   
        if kategory == 'All':
            videos_list = Book.objects.all().order_by('created_at').reverse()
        else:
            videos_list = Book.objects.filter(category=j).filter(watermark_ready=True)  
    #    print(videos) 

#        numbers_list = range(1, 1000)
        page = request.GET.get('page',1)
        paginator = Paginator(videos_list, 20)   # num of videos per page
        print(page)
        try:
            videos = paginator.page(page)
        except PageNotAnInteger:
            videos = paginator.page(1)
        except EmptyPage:
            videos = paginator.page(paginator.num_pages)

        countries = Country.objects.all()

        for cou in countries:
            print(cou.code)

        context = {
            'videos': videos,
            'categories': Category.objects.all().order_by('category'),
            'countries' :  countries
        }


        return render(request, "BootstrapFilterView.html", context)
        return render(request,'course_details.html', {'videos': videos})
    return redirect('login')   

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
    videos.purchase_date = date.today()
    videos.incident_date = videotobuy.incident_date
    videos.country = videotobuy.country


    videos.save()

    print
    print(request.user)
    print('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')

#    videos = Buyer.objects.get(news_name=6)
    videos = Cart.objects.filter(news_station=request.user)
    vote_count = News.objects.filter(news_station=request.user).count()
    return redirect('cart')
#    return render(request,'course_details.html', {'videos': videos}) 


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
    print('checkggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg')
    context = {}

    if request.user.is_authenticated:
        print('uplod authenticated')
    else:
        return render(request,'login.html')     
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

    if request.user.is_authenticated:
        print('uplod authenticated')
    else:
        return render(request,'login.html')  
    books = Cart.objects.filter(news_station=request.user)
    return render(request, 'cart.html', {
        'books': books
    })

def account_details(request):
    books = Account.objects.filter(user=request.user)
    return render(request, 'account_details.html', {
        'books': books
    })

def upload_book(request):

    if request.user.is_authenticated:
        print('uplod authenticated')
    else:
        return render(request,'login.html')     
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
            return redirect('Watermark')

            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', { 'form': form  })



def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


def modify_book(request, pk):
    countries = Country.objects.all()
    if request.method == 'POST':

        check_user = UserProfile.objects.get(user_id=request.user)
        if check_user.if_seller == False:   # if false means it is seller 
            videos = Book.objects.get(pk=pk)
            print('vendedor modificarrrrrrrrrrrrrrrrrrrrrrr')
        else:  
            videos = News.objects.get(pk=pk) 
            print('comprador modificar rrrrrrrrrrrrrrrrrrrrrr')

        videos.title = request.POST.get('title')   
        videos.desc = request.POST.get('description')      
        videos.price = int(request.POST.get('price') )  
        videos.price_exclusive = int(request.POST.get('exclusive_price') )  
        videos.minutes_exclusive = int(request.POST.get('exclusive_minutes'))
        incident_date = request.POST.get('incident_date') 
        country= request.POST.get('country')
        category =  request.POST.get('category')
        print(request.POST.get('category')  ,'jjjjjjjjjjjjjjjjjjjjjjj ') 

        if incident_date  != '':  
            videos.incident_date = incident_date 
        if country  != 'Choose...':  
            videos.country = country
        if category  != 'Choose...':  
            videos.category_id = category             

 
        print(request.POST.get('category') ) 

        print(country,incident_date)
        print('no es gettttttttttttttttttttttttttttttttttttttt')
        print(videos.title, videos.desc, videos.price, videos.price_exclusive, videos.minutes_exclusive,videos.incident_date,videos.country,videos.category)
        videos.save()

        check_user = UserProfile.objects.get(user_id=request.user)
        if check_user.if_seller == False:   # if false means it is seller 
            videos = Book.objects.filter(pk=pk)
            print('vendedorrrrrrrrrrrrrrrrrrrrrrr')
        else:  
            videos = News.objects.filter(pk=pk) 
            print('compradorrrrrrrrrrrrrrrrrrrrrrr')  

        context = {
            'videos': videos,
            'categories': Category.objects.all().order_by('category'),
            'countries' : countries
            }
        return render(request,'modify_book.html', context)
    else:
        print('es gettttttttttttttttttttttttttttttttttttttt')

        check_user = UserProfile.objects.get(user_id=request.user)
        if check_user.if_seller == False:   # if false means it is seller 
            videos = Book.objects.filter(pk=pk)
            print('vendedorrrrrrrrrrrrrrrrrrrrrrr')
        else:  
            videos = News.objects.filter(pk=pk) 
            print('compradorrrrrrrrrrrrrrrrrrrrrrr')        

    context = {
        'videos': videos,
        'categories': Category.objects.all().order_by('category'),
        'countries' : countries
        }

    return render(request,'modify_book.html', context)


def modify_account(request):
    countries = Country.objects.all()
    profiles = UserProfile.objects.get(user=request.user)
    type_news =  News_Type.objects.all()
    if request.method == 'POST':
        profiles.company_name = request.POST.get('company_name')   
        type_new = request.POST.get('type_newss') 

        profiles.web =  request.POST.get('web')
        profiles.alt_email= request.POST.get('alt_email')
        country = request.POST.get('country')
        print(type_new,country,'ddddddddddddddddddddddddddddddddddd')  

        if country  != 'Choose...':  
            profiles.country = country
        if type_new  != 'Choose...':  
            profiles.type_news_id = type_new

        profiles.save()
        profiles = UserProfile.objects.filter(user=request.user)
        context = {
            'profiles': profiles,
            'countries' : countries,
            'type_news' : type_news
            }
        return render(request,'modify_account.html', context)
    else:
        print('es gettttttttttttttttttttttttttttttttttttttt')


    print(request.user, profiles.if_seller) 
    if profiles.if_seller !=  False:  

        print( profiles.company_name ,
        profiles.type_news,
        profiles.web ,
        profiles.alt_email,
        profiles.country,'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz' )

    profiles = UserProfile.objects.filter(user=request.user)
    context = {
            'profiles': profiles,
            'countries' : countries,
            'type_news' : type_news
       }

    return render(request,'modify_account.html', context)

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
    print('entre a watermarkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')                
    videos=Create_Watermark.objects.all()
    i=1
#    add_to_cart(request, 1, 1)
    
    for video in  videos:
        video_pk = video.pkin
        pk_watermark=video.id
        original_video= Book.objects.get(pk=video_pk)
        video_to_watermark = str(original_video.pdf)

        name_path=str("D:\\Python\\Anaconda\\New_Project\\project\\media\\") + str(video_to_watermark)

        video_prepare = VideoFileClip(name_path)
        w,h = video_prepare.size 

        txt = TextClip("Copyright Videos Online",fontsize=70,color='white')
        txt = txt.set_pos('center').set_duration(video_prepare.duration)    
        txt = txt.set_duration(video_prepare.duration)   

#@#        txt_col = txt.on_color(size=(video_prepare.w + txt.w,txt.h-10),
#@#                  color=(0,0,0), pos=(6,'center'), col_opacity=0.6)

# This example demonstrates a moving text effect where the position is a function of time(t, in seconds).
# You can fix the position of the text manually, of course. Remember, you can use strings,
# like 'top', 'left' to specify the position
#@#        txt_mov = txt_col.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)),
#@#                                  max(5*h/6,int(100*t))) )
                                  
        print('trtrtrtrrtrtrtrtrtrtrtrtrt', name_path)
#        logo = TextClip ("Watermark  Watermark  Watermark", font="Amiri-Bold", fontsize=70,color="black" )

        print('fffffffffffffffffffffffff', name_path)
        final = CompositeVideoClip([video_prepare, txt])
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
        final.write_videofile(DB_watermark_path)
#        final.write_videofile("D:\\Python\\Anaconda\\New_Project\\project\\media\\books/pdfs/Motor_Accident.mp4")
        original_video.video_watermark=DB_watermark_path
        original_video.watermark_ready = True
        original_video.save()

        Create_Watermark.objects.filter(pk=pk_watermark).delete()

    return redirect('book_list')        
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

class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            print('chequear ventas fuera44444444444444444444444')
            books = Cart.objects.filter(news_station=self.request.user)
            form = CheckoutForm()
            context = {
                'form': form,
#                'couponform': CouponForm(),
                'order': books,
                'DISPLAY_COUPON_FORM': True
            }
            print('check checkput')
            return render(self.request, 'checkout.html', {'books': books})

#        return render(request, 'cart.html', {'books': books})
#            return render(self.request, 'checkout.html', context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("account:checkout")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        print('chequear ventas fuer22222222222222222222222224444')
        try:
            order = Cart.objects.filter(news_station=self.request.user)

            print(form.is_valid())

#  the form is falling, country            
            if '1'=='1':
#            if form.is_valid():
                print("User is entering a new billing address")
                billing_address1 = form.cleaned_data.get(
                        'billing_address')
                billing_address2 = form.cleaned_data.get(
                        'billing_address2')
                billing_country = form.cleaned_data.get(
                        'billing_country')
                billing_zip = form.cleaned_data.get('billing_zip')

#                if is_valid_form([billing_address1, billing_country, billing_zip]):
                billing_address = User_Info(
                            news_name=self.request.user,
                            address=billing_address1,
                            address1=billing_address2,
#                           country=billing_country,
                           country='Puerto Rico',
                            zipcode =billing_zip,
                            active=1
                        )
                print(billing_address.news_name,billing_address.address,billing_address.country,billing_address.zipcode)
#                billing_address.save()

            else:
                messages.info(
                            self.request, "Please fill in the required billing address fields")
                return redirect('checkout')
                payment_option = form.cleaned_data.get('payment_option')
            print('chequear ventas')
#            purchased = News()
            for item in order:
                purchased = News()
                account_details = Account() # create transaction log
                print('yyyyyyyyyyyyyy')
                print(purchased.title,'1', item.title)
                purchased.title = item.title
                purchased.category = item.category
                purchased.author = item.author
                purchased.news_station =item.news_station
                purchased.desc = item.desc
                purchased.pdf = item.pdf
                purchased.price = item.price
                purchased.price_exclusive = item.price_exclusive  
                purchased.minutes_exclusive = item.minutes_exclusive
                purchased.purchase_date = item.purchase_date
                purchased.incident_date = item.incident_date
                purchased.country = item.country                      
                purchased.save()

                account_details.title = item.title
                account_details.category = item.category
                account_details.author = item.author  
                account_details.user = item.news_station
                account_details.desc = item.desc
                account_details.price = item.price
#   Default    transacion_date
                book_id = item.news_station
                account_details.news_id = item.news_station
                account_details.incident_date = item.incident_date
                account_details.country = item.country 
#                account_details.if_seller_id = True
                account_details.save()

            print('chequear ventas fuera')
            Cart.objects.filter(news_station=self.request.user).delete()
            return redirect('news_account')
#            return redirect('payment', payment_option='stripe')
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("core:order-summary")

#    return redirect('checkout')

class PaymentView(View):
    def get(self, *args, **kwargs):
        order = Cart.objects.get(news_station=self.request.user)
        return render(self.request, "payment.html")
 

    def post(self, *args, **kwargs):
        order = Cart.objects.get(news_station=self.request.user)
        form = PaymentForm(self.request.POST)
        userprofile = User_Info.objects.get(user=self.request.user)
        if form.is_valid():
            token = form.cleaned_data.get('stripeToken')
            save = form.cleaned_data.get('save')
            use_default = form.cleaned_data.get('use_default')

            amount = int(order.get_total() * 100)

            try:

                # assign the payment to the order

                order_items = order.items.all()
                order_items.update(ordered=True)
                for item in order_items:
                    item.save()

#                order.ordered = True
#                order.payment = payment
#                order.ref_code = create_ref_code()
#                order.save()

                messages.success(self.request, "Your order was successful!")
                return redirect("/")

            except Exception as e:
                # send an email to ourselves
                messages.warning(
                    self.request, "A serious error occurred. We have been notifed.")
                return redirect("/")

        messages.warning(self.request, "Invalid data received")
        return redirect("/")

def add_profile(request):
    if request.method == 'POST':
        print('userrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr post')
        form =  UserForm(request.POST)
        if form.is_valid():
            type_news = request.POST['type_news'] 
            web = request.POST['web'] 
            alt_email = request.POST['alt_email']
            country = request.POST['country']  
            print(type_news,web,alt_email,country)
            instance = form.save(commit=False)
            instance.user=request.user
            instance.save()


            print('LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL')

#            uploaded_file = request.FILES['pdf']
#            dests = Book.objects.get()
#            print(dests.author)
 #           news=Profile()
   #         news.user = request.user
    #        news.web = web
     #       news.id = type_news
      #     news.alt_email = alt_email
       #     news.country = country
        #    news.save()

            print('updateuuuuuuuuLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL')

#            uploaded_file = request.FILES['pdf']
#            dests = Book.objects.get()
#            print(dests.author)

        return redirect('/')
    else:
        print('userrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr get')
        form =  UserForm()
    return render(request, 'add_profile.html', { 'form': form  })

# Filter 

def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):

#    return render(request,'filter.html')


    videos = Book.objects.all()
    categories = Category.objects.all()
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    incident_date = request.GET.get('incident_date')
    incident_date_up = request.GET.get('incident_date_up')
    category = request.GET.get('category')
    print(request.GET.get('country'))
    print('pasee la fromaaaaaaaaaaaaaaaaaa')
    country= request.GET.get('country')
    reviewed = request.GET.get('reviewed')
    not_reviewed = request.GET.get('notReviewed')

    print(category, request.GET.get('category'))
    print('pasee la fromaaaaaaaaaaaaaaaaaa')
#    return render(request,'filter.html')


    if is_valid_queryparam(title_contains_query):
        videos = videos.filter(title__icontains=title_contains_query)

    elif is_valid_queryparam(id_exact_query):
        videos = videos.filter(id=id_exact_query)

    elif is_valid_queryparam(title_or_author_query):
        videos = videos.filter(Q(title__icontains=title_or_author_query)
                       | Q(author__name__icontains=title_or_author_query)
                       ).distinct()

    if is_valid_queryparam(incident_date_up):
        videos = videos.filter(incident_date__gte=incident_date_up)

#    if is_valid_queryparam(date_min):
#        videos = videos.filter(publish_date__gte=date_min)

    print(incident_date)
    if is_valid_queryparam(incident_date):
        videos = videos.filter(incident_date=incident_date)

    if is_valid_queryparam(country) and country != 'Choose...':
        videos = videos.filter(country=country)

    if is_valid_queryparam(category) and category != 'Choose...':
        if category == 'All':
            videos = videos.filter().order_by('-incident_date')          
        else:    
            videos = videos.filter(category__category=category).order_by('-incident_date') 
            print(category)

    if reviewed == 'on':
        videos = videos.filter(reviewed=True)

    elif not_reviewed == 'on':
        videos = videos.filter(reviewed=False)

    print('pasee los iffffffffffffffffffffffffffffffffffff')

    return videos

def BootstrapFilterView(request):
    
    print('pasee bootstrapppppppppppppppppppppppppa')
    videos_list = filter(request)

#        numbers_list = range(1, 1000)
    page = request.GET.get('page',1)
    paginator = Paginator(videos_list, 20)   # num of videos per page
    print(page)
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)
    countries = Country.objects.all()

    context = {
        'videos': videos,
        'categories': Category.objects.all().order_by('category'),
        'countries' : countries
    }




    return render(request, "BootstrapFilterView.html", context)

def infinite_filter(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    return Book.objects.all()[int(offset): int(offset) + int(limit)]


def is_there_more_data(request):
    offset = request.GET.get('offset')
    if int(offset) > Book.objects.all().count():
        return False
    return True





#class ReactFilterView(generics.ListAPIView):
#    serializer_class = JournalSerializer

#    def get_queryset(self):
#        videos = filter(self.request)
#        return videos


#class ReactInfiniteView(generics.ListAPIView):
#    serializer_class = JournalSerializer

    def get_queryset(self):
        videos = infinite_filter(self.request)
        return videos

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response({
            "journals": serializer.data,
            "has_more": is_there_more_data(request)
        })
