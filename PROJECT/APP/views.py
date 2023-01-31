from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login


def home(request):
    return render(request,"APP/index.html")
    
def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        pass1=request.POST.get("pass1")
        pass2=request.POST.get("pass2")

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        if pass1==pass2:
            myuser.save()
            messages.success(request,"Ur account has been successfully created")
            return redirect("signin")
    return render(request,"APP/signup.html")


def signin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("pass1")
        

        user=authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"APP/index.html",{'fname':fname})
        else:
            messages.info(request,"Wrong Credentials")
            return redirect("home")
            
    return render(request,"APP/signin.html")



def signout(request):
    auth.logout(request)
    return redirect("home")




def Order(request):
    if request.method=="POST":
        country=request.POST.get("country")
        state=request.POST.get("state")
        district=request.POST.get("district")
        town=request.POST.get("town")
        pincode=request.POST.get("pincode")
        
        myorders=Order.objects.create_Order(country,state,district)
        myorders.save()
        

        
  
    return render(request,"APP/order.html")

def final(request):
    return render(request,"APP/final.html")

def abt(request):
    return render(request,"APP/abt.html")

def contact(request):
    return render(request,"APP/contact.html")

def myorders(request):
    return render(request,"APP/myorders.html")


from .forms import profileform
from .models import User
from django.contrib.auth.decorators import login_required
@login_required
def profile(request):
    return render(request,'APP/profile.html')
    
@login_required

def UpdateProfile(request):
    if request.method == 'POST':
        u_form=profileform(request.POST,request.FILES,instance=request.user)
        if u_form.is_valid:
            u_form.save()
            return redirect('profile') 
    else :
        u_form=profileform(instance=request.user)
        return render(request,'APP/update_profile.html',{'u_form':u_form})