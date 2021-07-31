from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('postRegister/', views.postRegister),
    path('login/', views.login, name='login'),
    path('postLogin/', views.postLogin),
    path('logout/', views.logout, name='logout'),
    path('reset/', views.reset),
    path('postReset/', views.postReset),
]