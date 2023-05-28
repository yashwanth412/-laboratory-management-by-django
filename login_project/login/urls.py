from django.urls import path

from . import views

"""urlpatterns = [
    path('home', views.home, name='home'),  # URL pattern for the home page
    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('stafflogin/', views.stafflogin, name='stafflogin'),
    path('studentregister/', views.studentregister, name='studentregister'),
    path('studentregister/studentlogin', views.studentlogin, name='studentlogin'),
    path('help/', views.help, name='help'),
    path('about/', views.about, name='about'),
    path('about/help', views.help, name='home'),
    path('about/home', views.about, name='about'),
    path('help/home', views.help, name='home'),
    path('help/about', views.about, name='about'),
    path('help/help', views.help, name='help'),
    path('about/about', views.about, name='about'),

]
"""