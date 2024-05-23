from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def review(request):
    return render(request,"review.html")

def signup(request):
    return render(request,"signup.html")

def login(request):
    return render(request,"login.html")


