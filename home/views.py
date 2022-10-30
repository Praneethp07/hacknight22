from multiprocessing import context
from django.shortcuts import render,HttpResponse

# Create your views here.
def homepage(request):
    return render(request,"index.html")         
def index(request):
    return render(request,"base.html")  
def about(request):
    return render(request,"about.html",{"name":"Hangyo Icecreams"})  
def services(request):
    return render(request,"services.html")  
def icecream(request):
    return render(request,"icecreams.html")  