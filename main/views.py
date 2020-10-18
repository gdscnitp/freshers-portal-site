# viewsfile
from django.shortcuts import render

import pyrebase
config={
    "apiKey": "#Add Api ",
    "authDomain": "#Add Here",
    "databaseURL": "#Add Here",
    "projectId": "#Add Here",
    "storageBucket": "#Add Here",
    "messagingSenderId": "#Add Here",
    "appId": "#Add Here",
    "measurementId": "#Add Here"
};


firebase=pyrebase.initialize_app(config)


def HomePage(request):
    return render(request,"Home.html")

def signIn(request):
    return render(request,"Login.html")

def signUp(request):
    return render(request,"Registration.html")

def profile(request):
    return render(request,"ProfilePage.html")
