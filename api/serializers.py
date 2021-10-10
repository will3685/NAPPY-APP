from rest_framework import serializers
from .models import *
from .views import *
# class UserClientSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = UserClient
#     fields = '__all__'

class UserHostSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserHost
    fields = '__all__' 

class HairCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = HairCategory
    fields = '__all__'

class HairSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hair
    fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = '__all__'

class UniqueCategoryHairSerializer(serializers.ModelSerializer):
  hairs = HairSerializer(many=True, read_only=True)  
  class Meta:
    model = HairCategory
    fields = '__all__'

class UniqueCategoryBookSerializer(serializers.ModelSerializer):
  books = BookSerializer(many=True, read_only=True)  
  class Meta:
    model = UserHost
    fields = '__all__'

class BookCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = BookCategory
    fields = '__all__'



# class AppointmentSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Appointment
#     fields = '__all__'