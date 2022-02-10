from rest_framework import serializers

from .models import Book


class BookListSerializer(serializers.ModelSerializer):
    """Список книг"""

    class Meta:
        model = Book
        fields = ('title', 'description')