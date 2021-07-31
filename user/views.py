from django.shortcuts import render
import pyrebase

config = {
    "apiKey": "AIzaSyAjcf-37_fsXaTZubI_MbsBRdmkAQKwp2w",
    "authDomain": "color-picker-c3823.firebaseapp.com",
    "projectId": "color-picker-c3823",
    "storageBucket": "color-picker-c3823.appspot.com",
    "messagingSenderId": "1058305178629",
    "appId": "1:1058305178629:web:739379b321753d9740b06c",
    "measurementId": "G-4P7CYXNYSG",
    "databaseURL": "",
}

# Initialising database, auth and firebase for further use 
firebase = pyrebase.initialize_app(config)
authen = firebase.auth()
database=firebase.database()

def login(request):
    return render(request,"login.html")

def home(request):
    return render(request,"home.html")
  
def postLogin(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user=authen.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials! Please check your Data"
        return render(request,"login.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"home.html",{"email":email})
  
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"login.html")
  
def register(request):
    return render(request,"registration.html")
  
def postRegister(request):
     email = request.POST.get('email')
     passs = request.POST.get('pass')
     name = request.POST.get('name')
     try:
        # creating a user with the given email and password
        user=authen.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
     except:
        return render(request, "registration.html")
     return render(request,"login.html")