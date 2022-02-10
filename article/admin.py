from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


admin.site.register(Author)


admin.site.register(Book)


admin.site.register(Image)


admin.site.register(Category)


admin.site.register(Publisher)

