from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL pattern for the home page
    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('stafflogin/', views.stafflogin, name='stafflogin'),
    path('studentregister/', views.studentregister, name='studentregister'),
]
