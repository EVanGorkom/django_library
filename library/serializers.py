from rest_framework import serializers
from .models import Book
from .models import Author

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ['title', 'author', 'price', 'checked_out']

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ['name']