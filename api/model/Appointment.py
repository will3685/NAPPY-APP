from django.db import models
from django.db.models.fields import CharField, EmailField, DateField, TimeField

class Appointment(models.Model):
  # bookcategory = models.ForeignKey('BookCategory', related_name='appointments', on_delete=models.CASCADE)
  date = models.DateField(auto_now=False)
  time = models.TimeField(auto_now=False)
  class Meta:
    db_table = 'Appointment'