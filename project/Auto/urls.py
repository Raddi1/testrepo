from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('email/', views.mail),
    path('cache/', views.caches),
    path('add/', views.add_pr)
] 

