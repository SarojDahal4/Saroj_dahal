from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import handler404
from .views import custom_404_view

handler404 = custom_404_view


urlpatterns = [
    path('',  views.home , name="home" ),
    path('MYcv/',  views.cv, name="cv" ),
    path('contact/',  views.contact , name="contact" ),
    path('project/',  views.project , name="project" ),
    path('image/',  views.image , name="image" ),
    path('Fimage/',  views.Fimage , name="Fimage" ),
    path('about/',  views.about , name="about" ),
    path('login/',  views.login_user , name="login" ),
    path('logout/',  views.logout_user , name="logout" ),
    path('register/',  views.register_user , name="register" ),

]
