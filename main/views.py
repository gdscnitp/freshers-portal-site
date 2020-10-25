# viewsfile
from django.shortcuts import render
<<<<<<< HEAD
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
=======
>>>>>>> c3a4ac32ae73e708cca1e6549f8792d6ce1549e2
import pyrebase

config={
    "apiKey": "AIzaSyA1_TbZc_DAJVAosBsBXHKVnANss0_220U",
    "authDomain": "freshers-portal.firebaseapp.com",
    "databaseURL": "https://freshers-portal.firebaseio.com",
    "projectId": "freshers-portal",
    "storageBucket": "freshers-portal.appspot.com",
    "messagingSenderId": "620782197376",
    "appId": "1:620782197376:web:f7835cc81df3aced7d2465",
    "measurementId": "G-KH43ST917G",
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def HomePage(request):
<<<<<<< HEAD
    import datetime
    timestamp=database.child('Blogs').shallow().get().val()
    lis_time = [];
    for i in timestamp:
        lis_time.append(i)
    Descriptions = []
    Titles = []
    Types = []
    Departments = []
    Writtenbys = []
    for i in lis_time:
        Department = database.child('Blogs').child(i).child('Department').get().val()
        Description =database.child('Blogs').child(i).child('Description').get().val()
        Title =database.child('Blogs').child(i).child('Title').get().val()
        Type =database.child('Blogs').child(i).child('Type').get().val()
        Writtenby =database.child('Blogs').child(i).child('Writtenby').get().val()
        Departments.append(Department)
        Descriptions.append(Description)
        Titles.append(Title)
        Types.append(Type)
        name = database.child('users').child(Writtenby).child('name').get().val()
        Writtenbys.append(name)
    date = []
    for i in timestamp:
        i = float(i)
        dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%y')
        date.append(dat)
    comb_lis = zip(lis_time, date, Descriptions,Departments,Titles,Types,Writtenbys)
    return render(request,"Home.html",{"comb_lis":comb_lis})
=======
    time_stamps = database.child("Blogs").shallow().get().val()
    blog = [database.child("Blogs").child(time).child("Description").get().val() for time in time_stamps]
    written = [database.child("Blogs").child(time).child("Written by").get().val() for time in time_stamps]
    names = [database.child("users").child(x).child('name').get().val() for x in written]
    comb_lis = list(zip(blog,names))
    for a,b in comb_lis:
        print(a)
        print(b)
    return render(request,"Home.html",{"comb":comb_lis})
    
    
>>>>>>> c3a4ac32ae73e708cca1e6549f8792d6ce1549e2

@csrf_exempt
def search(request):
    return render(request,"Search.html")
def signIn(request):
    return render(request,"Login.html")

def postsignIn(request):
<<<<<<< HEAD
    if request.method=='POST':
        email = request.POST.get('email')
        pasw = request.POST.get('pass')
        try:
            user = authe.sign_in_with_email_and_password(email, pasw)
        except:
            message = "Invalid Credentials!!Please Chech your Data"
            return render(request, "Login.html", {"message": message})
        session_id = user['idToken']
        request.session['uid'] = str(session_id)
        return render(request, "ProfilePage.html", {"email": email})
    message = "Please Login In First"
    return render(request, "Login.html", {"message": message})
=======
    
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

>>>>>>> c3a4ac32ae73e708cca1e6549f8792d6ce1549e2
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"Login.html")

def signUp(request):
    return render(request,"Registration.html")

def postsignup(request):
    if request.method == 'POST':
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
    message = "Please Login In First"
    return render(request, "Login.html", {"message": message})
def profile(request):
    return render(request,"ProfilePage.html")

def addPost(request):
<<<<<<< HEAD
        return render(request,"AddPost.html")


def afteraAddPost(request):
    if request.method=='POST':
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
                "Writtenby":a,
                "Time":Currenttime,
                "Department":branch,
            }

            database.child('Blogs').child(millis).set(data)
            return render(request,"ProfilePage.html")
    message = "Please Login In First"
    return render(request, "Login.html", {"message": message})



def gotoedit(request):
        return render(request,'editprofile.html')

def postedit(request):
    if request.method=='POST':
        import time
        from datetime import datetime,timezone
        import pytz
        tz = pytz.timezone('Asia/Kolkata')
        time_now = datetime.now(timezone.utc).astimezone(tz)
        millis = int(time.mktime(time_now.timetuple()))

        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        dname=request.POST.get('dname')
        email=request.POST.get('email')
        tarea=request.POST.get('tarea')
        course=request.POST['course']
        branch=request.POST['branch']
        year=request.POST['year']
        furl=request.POST.get('furl')
        turl=request.POST.get('turl')
        lurl=request.POST.get('lurl')
        wurl=request.POST.get('wurl')

        idtoken=request.session['uid']
        a = authe.get_account_info(idtoken)
        a=a['users']
        a=a[0]
        a=a['localId']

        data={
            "fname":fname,
            "lname":lname,
            "dname":dname,
            "email":email,
            "tarea":tarea,
            "course":course,
            "branch":branch,
            "year":year,
            "furl":furl,
            "turl":turl,
            "lurl":lurl,
            "wurl":wurl
        }
        database.child('users').child(a).update(data)

        return render(request,'editprofile.html')
    message = "Please Login In First"
    return render(request, "Login.html", {"message": message})
=======
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
    

>>>>>>> c3a4ac32ae73e708cca1e6549f8792d6ce1549e2
