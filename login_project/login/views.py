from django.shortcuts import render

# Create your views here.
def home(request):
    # View logic goes here
    return render(request, 'home.html')

def studentlogin(request):
    return render(request,'student_login.html')

def stafflogin(request):
    return render(request,'staff_login.html')

def studentregister(request):
    return render(request,'student_signup.html')