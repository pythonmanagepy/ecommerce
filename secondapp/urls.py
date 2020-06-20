from django.urls import path
from . import views

urlpatterns = [
	path('placeorder',views.placeorder,name="placeorder"),
    path('about',views.cfout,name="about"),
    path('index',views.index,name="index"),
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    #path('about',views.about,name="about"),
    path('register',views.register,name="register"),
    path('check',views.check_user,name="check_user"),
    path('allproduct/<int:pk>/',views.allprod,name="allproduct"),
    path('singleproduct/<int:pk>/',views.oneproduct,name="singleproduct"),
]