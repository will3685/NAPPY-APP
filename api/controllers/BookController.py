from django.shortcuts import render, get_object_or_404
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from api.models import *
from api.serializers import *

class BookList(APIView):
  def get(self, request):
      books = Book.objects.all()
      data = BookSerializer(books, many=True).data
      return Response(data)
  def post(self, request):
        # name = request.data["name"]
        # description = request.data["description"]
        # haircategory = HairCategory( name=name, description=description)
        # description.save()
        # serializer = HairCategorySerializer(haircategory).data

      serializer = BookSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)

