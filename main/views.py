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
    time_stamps = database.child("Blogs").shallow().get().val()
    blog = [database.child("Blogs").child(time).child("Description").get().val() for time in time_stamps]
    written = [database.child("Blogs").child(time).child("Written by").get().val() for time in time_stamps]
    names = [database.child("users").child(x).child('name').get().val() for x in written]
    comb_lis = list(zip(blog,names))
    for a,b in comb_lis:
        print(a)
        print(b)
    return render(request,"Home.html",{"comb":comb_lis})
    
    

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
    request.session['uid'] = str(session_id)
    a = authe.get_account_info(request.session['uid'])
    a = a['users']
    a = a[0]
    a = a['localId']
    name = database.child('users').child(a).child('name').get().val()
    return render(request ,"ProfilePage.html",{"e":name})

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
    branch=request.POST.get('sel')
    enroll=request.POST.get('enrolls')
    roll=request.POST.get('roll')
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw)
    except:
        messg="unable to create account try again"
        return render(request,"registration.html",{"messg":messg})
    uid = user['localId']
    data={"name":name,"USER_TYPE":"user","device_token":"","email":email,"id":roll,"imgUrl":"","branch":branch,"uid":uid,"enrollment":enroll}
    database.child("users").child(uid).set(data)
    return render(request,"login.html")

def profile(request):
    return render(request,"ProfilePage.html")

def addPost(request):
    return render(request,"AddPost.html")

def afteraAddPost(request):
    from datetime import datetime, timezone
    import time
    import pytz

    idToken = request.session['uid']
    if idToken:
        tz = pytz.timezone('Asia/Kolkata')
        Currenttime = datetime.now(timezone.utc).astimezone(tz).strftime("%H%M%S")
        millis = int(Currenttime)
        tyype = request.POST.get('type')
        title = request.POST.get('title')
        description = request.POST.get('desc')
        branch=request.POST.get('sel')
    
        a = authe.get_account_info(idToken)
        a = a['users']
        a = a[0]
        a = a['localId']
        print(str(a))
       

        data ={
            "Type":tyype,
            "Title":title,
            "Description":description,
            "Written by":a,
            "Time":Currenttime,
            "Department":branch,
        }

        database.child('Blogs').child(millis).set(data)
        
       
        return render(request,"ProfilePage.html")
    

