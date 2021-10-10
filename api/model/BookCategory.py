from django.db import models
from django.db.models.fields import CharField, EmailField

class BookCategory(models.Model):
  name = models.CharField(max_length=20, blank=False)
  description = models.CharField(max_length=254, null=True)
  class Meta:
    db_table = 'Book_Category'