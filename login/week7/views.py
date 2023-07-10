from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import cache_control


# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
# @login_required(login_url='login')
def homepage(request):
    if 'user' in request.session:
        return render(request,'home.html')
    else:
        return redirect('login')

def signuppage(request):
    if 'user' in request.session:
        return redirect('home')
    
    if request.method=='POST':
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            repeatpassword=request.POST.get('repeatpassword')
            print(password,repeatpassword)
            
            if password != repeatpassword:
                messages.error(request, "password not match")
                return redirect(signuppage)
            else:
                my_user = User.objects.create_user(username=username, email=email, password=password)
                my_user.save()
                return redirect('login')
    return render(request, 'Signup.html')
    # return render(request, 'Signup.html')
   
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def loginpage(request):
    if 'user' in request.session:
        return redirect('home')
    
    if request.method=='POST':
        username=request.POST.get('form3Example3')
        password=request.POST.get('form3Example4')
        print(username,password)
        
        user=authenticate(request,username=username,password=password)
        if user:
            request.session['user'] = username
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"User name and password are in correct !!!")
    
        
    return render(request,'login.html')
def Logoutpage(request):
    logout(request)
    return redirect('login')
