from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=50, null=False)
  
  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=100, null=False)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
  checked_out = models.BooleanField(default=False)

  def __str__(self):
    return self.title
  
class Library(models.Model):
  name = models.CharField(max_length=100, null=False)
  books = models.ManyToManyField('Book')

  def __str__(self):
    return self.name