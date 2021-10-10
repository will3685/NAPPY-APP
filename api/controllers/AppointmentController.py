from django.shortcuts import render, get_object_or_404
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from api.models import *
from api.serializers import *

class AppointmentList(APIView):
  def get(self, request):
      appointments = Appointment.objects.all()
      data = AppointmentSerializer(appointments, many=True).data
      return Response(data)
  def post(self, request):
        # name = request.data["name"]
        # description = request.data["description"]
        # bookcategory = BookCategory( name=name, description=description)
        # description.save()
        # serializer = BookCategorySerializer(bookcategory).data

      serializer = AppointmentSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)

# class BookCategoryDetail(APIView):
#   def get(self,request, id):
#     bookcategory = get_object_or_404(BookCategory, id=id)
#     serializer = BookCategorySerializer(bookcategory).data
#     return Response(serializer)


