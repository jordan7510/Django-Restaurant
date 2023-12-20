from rest_framework import serializers
from user.models import MenuItems


class MenuItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = ['id', 'item_name', 'item_desc', 'item_type', 'item_price', 'item_image']