from rest_framework import serializers
from .models import Drawings,PriceList


class DrawingSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Drawings
        fields = ['id', 'Commissioned','image','year','created_at']


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = '__all__'