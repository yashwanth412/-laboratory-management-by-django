"""login_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from.import index
from login import views
#from login.views import studentlogin, studentregister


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.home),
    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('stafflogin/', views.stafflogin, name='stafflogin'),
    path('studentregister/',views.studentregister, name='studentregister'),
    path('studentregister/studentlogin', views.studentlogin, name='studentlogin'),
    path('help/', views.help, name='help'),
    path('about/', views.about, name='about'),
    path('about/help', views.help, name='home'),
    path('about/home', views.about, name='about'),
    path('help/home', views.help, name='home'),
    path('help/about', views.about, name='about'),
    path('help/help', views.help, name='help'),
    path('about/about', views.about, name='about'),
    path('batch/', views.batch, name='batch'),
    path('batch/about', views.about, name='about'),

]
