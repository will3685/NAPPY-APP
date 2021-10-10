from rest_framework import serializers
from .models import *
from .views import *
class UserClientSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserClient
    fields = '__all__'
    
class HairCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = HairCategory
    fields = '__all__'

class HairSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hair
    fields = '__all__'

class HairCategoryHairSerializer(serializers.ModelSerializer):
  hairs = HairSerializer(many=True, read_only=True)
  class Meta:
    model = HairCategory
    fields = '__all__'