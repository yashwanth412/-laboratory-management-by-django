from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Student,staff
#from django import HttpResponsr

# Create your views here.
@login_required(login_url='login')
def home(request):
    # View logic goes here
    return render(request, 'home.html')


def studentlogin(request):
    if request.method=='POST':
        roll_number = request.POST.get('roll_number')
        password = request.POST.get('password')
        roll_number = authenticate(request,roll_number=roll_number,password=password)
        if User is not None:
            login(request,User)
            return redirect('batch')
        else:
            return HttpResponse ("roll_numbername or Password is incorrect!!!")
    
    return render(request,'student_login.html')

def stafflogin(request):
    return render(request,'staff_login.html')


def studentregister(request):
    if request.method=='POST':
    
        
        roll_number=request.POST.get('roll_number')
        branch = request.POST.get('branch')
        mobil_number=request.POST.get('mobile_number')
        pass1= request.POST.get('password')
        pass2= request.POST.get('password')
        gmail=request.POST.get('gmail')
        
        if Student.objects.filter(roll_number=roll_number):
            return HttpResponse("roll number already exist! Please try some other roll number.")
        
        if Student.objects.filter(gmail = gmail).exists():
            return HttpResponse("Email Already Registered!!")
        
        if len(roll_number)>20:
            return HttpResponse("roll number must be under 20 charcters!!")
        
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
           my_user=User.objects.create_user(roll_number,gmail,pass1)
           my_user.save()
           return redirect('studentlogin')
         #print(roll_number,branch,mobile_number,password,gmail)
    return render(request,'student_signup.html')

def help(request):
    return render(request,'help.html')

def about(request):
    return render(request,'about.html')

def Components(request):
    return render(request,'Components.html')

def batch(request):
    return render(request,'form_batch.html')
