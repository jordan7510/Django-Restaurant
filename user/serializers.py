from rest_framework import serializers
from .models import MenuItems, ReservationDetails, OrdersDetails



class MenuItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationDetails
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersDetails
        fields = '__all__'