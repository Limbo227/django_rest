from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.


class HouseCreationView(generics.CreateAPIView):
    serializer_class = HouseSerializers
    permission_classes = (IsAdminUser, IsAuthenticated,)


class HouseListView(generics.ListAPIView):
    serializer_class = HouseListSerializers
    queryset = House.objects.all()


class HouseUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HouseSerializers
    queryset = House.objects.all()
    permission_classes = (OwnerOrReadOnly, IsAuthenticated, )