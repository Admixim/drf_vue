from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Book, Image
from .serializers import BookListSerializer, BookDetailSerializer, BookCreateSerializer, ImageCreateSerializer, \
    ImageListSerializer


class BookListView(generics.ListAPIView):
    """Вывод списка книг"""

    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class ImageListView(generics.ListAPIView):
    """ Вывод списка изображений"""

    queryset = Image.objects.all()
    serializer_class = ImageListSerializer


class BookDetailView(generics.RetrieveAPIView):
    """Вывод информации о  книге"""

    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


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
