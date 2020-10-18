# viewsfile
from django.shortcuts import render

import pyrebase
config={
    "apiKey": "AIzaSyA1_TbZc_DAJVAosBsBXHKVnANss0_220U",
    "authDomain": "freshers-portal.firebaseapp.com",
    "databaseURL": "https://freshers-portal.firebaseio.com",
    "projectId": "freshers-portal",
    "storageBucket": "freshers-portal.appspot.com",
    "messagingSenderId": "620782197376",
    "appId": "1:620782197376:web:f7835cc81df3aced7d2465",
    "measurementId": "G-KH43ST917G"
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