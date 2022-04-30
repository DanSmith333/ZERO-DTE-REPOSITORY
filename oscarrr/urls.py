from django.urls import path
from oscarrr import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    
    
    path('doit/', views.doit, name='doit'),
    path('user_parameters/', views.user_parameters, name='user_parameters'),
    
    
    #path('posts/create/', views.create, name='posts.create'),
    #path('posts/<int:id>/', views.show, name='posts.show'),
    #path('posts/<int:id>/edit/', views.edit, name='posts.edit'),
    #path('posts/<int:id>/delete/', views.delete, name='posts.delete'),
] 