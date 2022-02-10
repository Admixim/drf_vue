from django.core.validators import FileExtensionValidator
from django.db import models


class Author(models.Model):
    """Таблица Авторов книг"""
    name = models.CharField(
                            max_length=255,
                            blank=True,
                            null=True,
                            default=None,
                        )
    country = models.CharField(
                               max_length=255,
                               blank=True,
                               null=True,
                               default=None,
                               )
    description = models.TextField(
                                   max_length=255,
                                   blank=True,
                                   null=True,
                                   default=None,
                                    )

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Publisher(models.Model):
    """Таблица Издательств"""
    name = models.CharField(
                            max_length=255,
                            blank=True,
                            null=True,
                            default=None,
                            )
    address = models.CharField(
                             max_length=255,
                             blank=True,
                             null=True,
                             default=None,
                              )
    email = models.EmailField(
                            max_length=255,
                            blank=True,
                            null=True,
                            default=None,
                             )
    description = models.TextField(
                                   max_length=255,
                                   blank=True,
                                   null=True,
                                   default=None,
                                   )

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'



class Category(models.Model):
    """Таблица Категорий"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Image(models.Model):
    """Таблица фотографий обложек книг"""

    book = models.ForeignKey(
                            'Book',
                            related_name='image',
                            on_delete=models.CASCADE,
                            max_length=255
                        )
    name = models.CharField(
                            max_length=255,
                            blank=True,
                            null=True,
                            default=None,
                            )
    img = models.ImageField(
                            upload_to='image/',
                            blank=True,
                            null=True,
                            default=None,
                            validators=[FileExtensionValidator(allowed_extensions=['jpg'])]
                            )

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'



class Book(models.Model):
    """Таблица Книг"""

    title = models.CharField(
                            max_length=120,
                            blank=True,
                            null=True,
                            default=None,
                            )
    description = models.TextField(
                                    blank=True,
                                    null=True,
                                    default=None,
                                    )
    body = models.TextField(
                            blank=True,
                            null=True,
                            default=None,
                            )
    author = models.ManyToManyField(
                                    'Author',
                                    related_name='books'
                                    )
    publisher = models.ForeignKey(
                                Publisher,
                                related_name='book',
                                on_delete=models.CASCADE,
                                max_length=255
                                )
    published_date = models.DateField(
                                    blank=True,
                                    null=True,
                                    default=None,
                                    )
    page = models.PositiveIntegerField()
    category = models.ForeignKey(
                                Category,
                                related_name='book',
                                on_delete=models.CASCADE,
                                max_length=255
                                )
    file = models.FileField(
                            upload_to='book/',
                            blank=True,
                            null=True,
                            default=None,
                            validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
                            )

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
