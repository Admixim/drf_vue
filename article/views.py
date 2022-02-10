from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookListSerializer, BookDetailSerializer


class BookListView(APIView):
    """Вывод списка книг"""
    def  get(self, request):
        book = Book.objects.all()
        serializer = BookListSerializer(book, many=True)
        return Response(serializer.data)


class BookDetailView(APIView):
    """Вывод информации о  книге"""
    def  get(self, request, pk):
        book = Book.objects.get(id = pk)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)