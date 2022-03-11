from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Product
from .forms import ProductDetails
# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        print(password,confirmpassword)
        if password != confirmpassword:
            messages.error(request,'Password Mismatch')
            return redirect('signup')

        try:
            myuser=User.objects.create_user(username=username,email=email,password=password)
        except:
            messages.error(request,'Username Exists')
            return redirect('signin')
        myuser.first_name=name
        myuser.save()
        messages.success(request,'Your Account has been successfully Created')

        return redirect('/')

    return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
    
        user=authenticate(username=username,password=password)

        if user is not None:
            context={
                'username':user.first_name
            }
            login(request,user)
            messages.success(request,'Login Successful')
            return render(request,'index.html',context)
        else:
            messages.error(request,'Wrong Credentials')
            return redirect('/')
            
    return render(request,'signin.html')
    # return HttpResponse('signin')

def signout(request):
    logout(request)
    messages.success(request,'Logged Out Succesfully')
    return redirect('/')

def seller(request):
    if request.method == 'POST':
        form=ProductDetails(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            img_object=form.instance
            return render(request,'seller.html',{'form':form,'img_obj':img_object})
    else:
        form=ProductDetails() 
    
    return render(request,'seller.html',{'form':form})

def buyer(request):
    pass

def gallery(request):
    products=Product.objects.all()
    return render(request,'gallery.html',context={'products':products})