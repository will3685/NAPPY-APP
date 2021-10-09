from django.db import models
from django.db.models.fields import CharField, DateField

class HairCategory(models.Model):
  name = models.CharField(max_length=20)
  description= models.CharField(max_length=200)
  class Meta:
    db_table = 'Hair_Category'