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
    if request.method == 'POST':
        rollnum = request.POST.get('roll_number')
        pass1 = request.POST.get('password')
        print(pass1)
        # Check if the student exists in the database
        try:
            student = Student.objects.get(roll_number=rollnum)
        except Student.DoesNotExist:
            return render(request, 'student_login.html', {'error': 'Invalid credentials'})
            

        # Compare the provided password with the stored password
        if student.password == pass1:
            # Authentication succeeded, set a session variable or store relevant information
            request.session['authenticated'] = True
            request.session['roll_number'] = rollnum
            return redirect('batch')
        else:
            # Authentication failed, show an error message or redirect to a login page
            print("hi")
            print(pass1,rollnum)
            return render(request, 'student_login.html', {'error': 'Invalid credentials'})

    return render(request, 'student_login.html')

def stafflogin(request):
    return render(request,'staff_login.html')


def studentregister(request):
    if request.method=='POST':
        rollnum=request.POST.get('roll_number')
        branch1 = request.POST.get('branch')
        mobil=request.POST.get('mobile_number')
        pass1= request.POST.get('password')
        pass2= request.POST.get('password')
        gmail1=request.POST.get('gmail')
        
        if Student.objects.filter(roll_number=rollnum):
            return HttpResponse("roll number already exist! Please try some other roll number.")
        
        if Student.objects.filter(gmail = gmail1).exists():
            return HttpResponse("Email Already Registered!!")
        
        if Student.objects.filter(mobile_number = mobil).exists():
            return HttpResponse("mobile Number is Already Registered!!")
        
        if len(rollnum)>20:
            return HttpResponse("roll number must be under 20 charcters!!")
        
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
           my_user=Student(roll_number= rollnum,gmail=gmail1,password=pass1,branch=branch1,mobile_number=mobil)
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
