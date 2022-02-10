from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('book/', views.BookListView.as_view()),
    path('book/<int:pk>/', views.BookDetailView.as_view()),
    path('create/', views.BookCreateView.as_view()),

]