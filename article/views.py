from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookListSerializer


class BookListView(APIView):
    """Вывод списка книг"""
    def  get(self, request):
        book = Book.objects.filter(author=False)
        serializer = BookListSerializer(book, many=True)
        return Response(serializer.data)


