from django.contrib import admin
from .models import Book
from .models import Author
from .models import Library

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)