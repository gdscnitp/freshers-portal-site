# viewsfile
from django.shortcuts import render

def HomePage(request):
    return render(request,"Home.html")

def signIn(request):
    return render(request,"Login.html")

def signUp(request):
    return render(request,"Registration.html")

def profile(request):
    return render(request,"ProfilePage.html")