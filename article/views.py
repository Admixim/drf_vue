from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .models import Book, Image
from .serializers import BookListSerializer, BookDetailSerializer, BookCreateSerializer, ImageCreateSerializer, ImageListSerializer


class BookListView(generics.GenericAPIView):
    """Вывод списка книг"""

    def get(self, request):
        book = Book.objects.all()
        serializer = BookListSerializer(book, many=True)
        return Response(serializer.data)


class ImageListView(APIView):
    """ Вывод списка изображений"""

    def get(self, request):
        image = Image.objects.all()
        serializer = ImageListSerializer(image, many=True)
        return Response(serializer.data)


class BookDetailView(APIView):
    """Вывод информации о  книге"""

    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)


class BookCreateView(APIView):
    """Создание- добавление книги"""
    def post(self, request):
        book = BookCreateSerializer(data=request.data)
        if book.is_valid():
            book.save()
            return Response(book.data, status=status.HTTP_201_CREATED)
        return Response(book.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageCreateView(APIView):
    """Добавление изображения  книги"""
    def post(self, request):
        image = ImageCreateSerializer(data=request.data)
        if image.is_valid():
            image.save()
            return Response(image.data, status=status.HTTP_201_CREATED)
        return Response(image.errors, status=status.HTTP_400_BAD_REQUEST)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        print('HTTP_X_FORWARDED_FOR', ip)
    else:
        ip = request.META.get('REMOTE_ADDR')
        print('REMOTE_ADDR', ip)
    return HttpResponse("<p>Ваш ip адрес:%s</p>" % ip)