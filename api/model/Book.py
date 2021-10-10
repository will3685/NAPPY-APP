from django.db import models
from django.db.models.fields import CharField, IntegerField


class Book(models.Model):
  userhost = models.ForeignKey('UserHost', related_name='books', on_delete=models.CASCADE)
  bookcategory = models.ForeignKey('BookCategory', related_name='book', on_delete=models.CASCADE)
  class Meta:
    db_table = 'Book'