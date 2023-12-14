from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.models import MenuItems
from .serializers import MenuItemsSerializer


# Create your views here.
def adminhome(req):
    return render(req, 'admin_index.html')

def adminreserv(req):
    return render (req, 'admin_reservation.html')

# def adminitems(req):
#     if req.method == "POST":
#         name = req.POST['itemName']
#         desc = req.POST['itemDesc']
#         type = req.POST['itemType']
#         price = req.POST['itemPrice']
#         itemObject = MenuItems.objects.create(item_name=name, item_desc=desc, item_type=type, item_price=price)
#         itemObject.save()
#     records = MenuItems.objects.all()
#     return render(req,'admin_items.html',{'items':records})


class AdminItemsApiView(APIView):
    def get(self,req,format=None):
        items = MenuItems.objects.all()
        serializer = MenuItemsSerializer(items, many=True)
        # return Response({'items':serializer.data})
        return render(req,'admin_items.html',{'items':serializer.data})
    
    def post(self,req,format=None):
        serializer = MenuItemsSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            items = MenuItems.objects.all()
            serializer = MenuItemsSerializer(items, many=True)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return render(req,'admin_items.html',{'items':serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class AdmiItemsEdit(APIView):
    def post(self,req,item_id, format=None):
        item = get_object_or_404(MenuItems, pk=item_id)
        serializer = MenuItemsSerializer(item, data=req.data)
        if serializer.is_valid():
            serializer.save()
            items = MenuItems.objects.all()
            serializer = MenuItemsSerializer(items, many=True)
            return render(req,'admin_items.html',{'items':serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AdmiItemsDelete(APIView):
    def post(self,req,item_id, format=None):
        item = get_object_or_404(MenuItems, pk=item_id)
        item.delete()
        items = MenuItems.objects.all()
        serializer = MenuItemsSerializer(items, many=True)
        return render(req,'admin_items.html',{'items':serializer.data})
        









    




