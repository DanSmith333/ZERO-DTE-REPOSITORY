from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='graditudor.home'),
    path('graditudor/', views.random_graditude, name='random_graditude'),
    #path('posts/create/', views.create, name='posts.create'),
    #path('posts/<int:id>/', views.show, name='posts.show'),
    #path('posts/<int:id>/edit/', views.edit, name='posts.edit'),
    #path('posts/<int:id>/delete/', views.delete, name='posts.delete'),
] 
