from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('book/', views.BookListView.as_view()),
    path('book/<int:pk>/', views.BookDetailView.as_view()),
    path('create_book/', views.BookCreateView.as_view()),
    path('create_image/', views.ImageCreateView.as_view()),
    path('image/', views.ImageListView.as_view()),
    path('get_client_ip/', views.get_client_ip),


]