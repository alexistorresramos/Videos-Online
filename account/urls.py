from django.urls import path

from .views import CheckoutView, PaymentView
from . import (views )
# from django.views import CheckoutView

urlpatterns = [
    path("register_buyer", views.register_buyer, name="register_buyer"),
    path("registration", views.registration, name="registration"),
    path("register_seller", views.register_seller, name="register_seller"),  
    path('buy_videos', views.buy_videos, name='buy_videos'),
    path('my_account', views.my_account, name='my_account'), 
    path('modify_book/<int:pk>', views.modify_book, name='modify_book'), 
    path('news_account', views.news_account, name='news_account'), 
    path('account_details', views.account_details, name='account_details'), 
#    path('filter', views.filter, name='filter'), 
    path('BootstrapFilterView', views.BootstrapFilterView, name='BootstrapFilterView'), 



    path('buy_video/<int:pk>', views.buy_video, name='buy_video'), 

#    path('videos', views.videos, name='videos'),
    path('course_details/<str:kategory>', views.course_details, name='course_details'),
    path('index1', views.index1, name='index1'),
    path("login", views.login, name="login"),   
    path("logout", views.logout, name="logout"),    
    path("Watermark", views.Watermark, name="Watermark"),   
    path("modify_account", views.modify_account, name="modify_account"),   


    path('home', views.home, name='home'),
#    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),

    path('books/', views.BookListView.as_view(), name='class_book_list'),
    path('books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),

    path('cart', views.cart, name='cart'), 
    path('delete_cart/<int:pk>/', views.delete_cart, name='delete_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),  
    path('add_profile', views.add_profile, name='add_profile'),

#    path('checkout', views.checkout, name='checkout'),  

]