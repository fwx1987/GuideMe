from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('register.html', views.registerView.as_view(), name='register'),
    path('login.html', views.loginView, name='login'),
]