from django.urls import path,re_path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    re_path('register', views.register, name='register'),
    re_path('login', views.login, name='login'),
    re_path('logout', views.logout, name='logout'),
    re_path('dashboard', views.dashboard, name='dashboard'),
]