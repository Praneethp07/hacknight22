from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("home",views.index,name='home'),
    path("services",views.services,name='services'),
    path("icecream/",views.icecream,name='icecream'),
    path("about",views.about,name='about'),
]
