from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('password-create/', views.PasswordCreate, name='password-create'),
    path('signup/', views.Signup, name='Signup'),
    path('login/', views.Login, name='Login'),
]
