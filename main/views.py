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
}


firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


def HomePage(request):
    return render(request,"Home.html")

def signIn(request):
    return render(request,"Login.html")

def postsignIn(request):
    
    email = request.POST.get("email")
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message = "Invalid credentials"
        return render(request ,"Login.html",{"messg":message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    

    return render(request ,"welcome.html",{"e":email})
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"Login.html")

def signUp(request):
    return render(request,"Registration.html")

def postsignup(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw)
    except:
        messg="unable to create account try again"
        return render(request,"registration.html",{"messg":messg})
    uid = user['localId']
    data={"name":name,"status":"1"}
    database.child("users").child(uid).child("details").set(data)
    return render(request,"login.html")

def profile(request):
    return render(request,"ProfilePage.html")