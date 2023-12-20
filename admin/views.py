from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse   
from user.models import MenuItems, ReservationDetails, OrdersDetails
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  logout
from django.utils.decorators import method_decorator


from .serializers import MenuItemsSerializer
from user.serializers import ReservationSerializer, OrdersSerializer


def logout_view(request):
    logout(request)
    # Redirect to a page after logout (e.g., home page)
    return redirect('login') 


# Create your views here.
@method_decorator(login_required(login_url='login'), name='dispatch')
class adminOrdersApiView(APIView):
    def get(self, req,format=None):
        items=OrdersDetails.objects.all()
        serializer=OrdersSerializer(items, many=True)
        return render(req, 'admin_index.html',{'items':serializer.data})

    
# def adminreserv(req):
#     data=ReservationDetails.objects.all()
#     return render (req, 'admin_reservation.html')
@method_decorator(login_required(login_url='login'), name='dispatch')
class adminReservationApiView(APIView):
    def get(self, req,format=None):
        items=ReservationDetails.objects.all()
        serializer = ReservationSerializer(items, many=True)
        return render (req, 'admin_reservation.html', {'items':serializer.data})


# Items view ,add,edit and delete views
@method_decorator(login_required(login_url='login'), name='dispatch')
class AdminItemsApiView(APIView):
    def get(self,req,format=None):
        items = MenuItems.objects.all()
        serializer = MenuItemsSerializer(items, many=True)
        # return Response({'items':serializer.data})
        return render(req,'admin_items.html',{'items':serializer.data})
    
    def post(self, req, format=None):
        serializer = MenuItemsSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            items = MenuItems.objects.all()
            serializer = MenuItemsSerializer(items, many=True)
            return render(req, 'admin_items.html', {'items': serializer.data})
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
    

    
# Items view ,add,edit and delete views END
        









    




