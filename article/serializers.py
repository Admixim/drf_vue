from rest_framework import serializers

from .models import Book, Image


class BookListSerializer(serializers.ModelSerializer):
    """Список книг"""
    author = serializers.SlugRelatedField(slug_field="name", read_only=True)
    publisher = serializers.SlugRelatedField(slug_field="name", read_only=True)
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Book
        fields = "__all__"


class ImageCreateSerializer(serializers.ModelSerializer):
    """Выввод всех изображений связанных с книгой"""
    class Meta:
        model = Image
        fields = ("name", "book",)



class BookCreateSerializer(serializers.ModelSerializer):
    """Создание  книги"""

    class Meta:
        model = Book
        exclude = ("file", "published_date",)


class ImageListSerializer(serializers.ModelSerializer):
    """Список изображений"""
    author = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Image
        fields = "__all__"


class BookDetailSerializer(serializers.ModelSerializer):
    """Список  Информация о книге"""
    author = serializers.SlugRelatedField(slug_field="name", read_only=True)
    publisher = serializers.SlugRelatedField(slug_field="name", read_only=True)
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    image = ImageCreateSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"
