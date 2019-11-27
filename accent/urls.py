from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='index'),
#    path('courses', views.courses, name='courses'),
    path('index', views.index1, name='index')  
#    path('', views.courses, name='courses')    
#    path('', views.courses, {"template_names" : "accent/courses.html"})
]