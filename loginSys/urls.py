from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homePage'),
    path('login/', views.login, name='loginPage'),
    path('signup/', views.signup, name='signupPage'),
    path('logout/', views.logout, name='logout'),
]
