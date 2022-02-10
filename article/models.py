from django.core.validators import FileExtensionValidator
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Image(models.Model):
    book = models.ForeignKey('Book', related_name='image', on_delete=models.CASCADE, max_length=255)
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='image/', validators=[FileExtensionValidator(allowed_extensions=['jpg'])])

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'



class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ManyToManyField('Author', related_name='books')
    publisher = models.ForeignKey(Publisher, related_name='book', on_delete=models.CASCADE, max_length=255)
    published_date = models.DateField()
    page = models.PositiveIntegerField()
    category = models.ForeignKey(Category, related_name='book', on_delete=models.CASCADE, max_length=255)
    file = models.FileField(upload_to='book/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
