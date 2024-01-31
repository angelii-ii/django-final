from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import logInForm

app_name= 'homepage'

urlpatterns=[
    path('',views.index,name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='homepage/login.html', authentication_form=logInForm),name='login'),
    path('logout/',views.logout,name='logout')
]