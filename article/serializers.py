from rest_framework import serializers

from .models import Book


class BookListSerializer(serializers.ModelSerializer):
    """Список книг"""
    author = serializers.SlugRelatedField(slug_field="name", read_only=True)
    publisher = serializers.SlugRelatedField(slug_field="name", read_only=True)
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Book
        fields = "__all__"


class BookDetailSerializer(serializers.ModelSerializer):
    """Список  Информация о книге"""
    author = serializers.SlugRelatedField(slug_field="name", read_only=True)
    publisher = serializers.SlugRelatedField(slug_field="name", read_only=True)
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)


    class Meta:
        model = Book
        fields = "__all__"

# class ReviewCreateSerialazer(serializers.ModelSerializer):
