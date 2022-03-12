from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import *
from .serializers import *
from .models import *
# Create your views here.

class MaqolaViewSet(ModelViewSet):
    queryset = Maqola.objects.all()
    serializer_class = MaqolaSerial

class ImageCreateList(ListCreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerial

class ImageDelete(DestroyAPIView):
    queryset = Maqola.objects.all()
    serializer_class = MaqolaSerial