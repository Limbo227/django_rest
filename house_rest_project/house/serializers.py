from rest_framework import serializers
from .models import House
from .permissions import *


class HouseListSerializers(serializers.ModelSerializer):
    class Meta:
        model = House   
        fields = '__all__'


class HouseSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = House
        fields = '__all__'
