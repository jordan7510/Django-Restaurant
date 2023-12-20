from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MenuItems, OrdersDetails
from .serializers import ReservationSerializer, OrdersSerializer, MenuItemsSerializer


# Create your views here.


class reservationDetails(APIView):
    def post(self, req, format=None):
        serializer = ReservationSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            # records = MenuItems.objects.all()
            return JsonResponse({"message": "Form submitted successfully"}, status=200)
        print(serializer.errors)
        return JsonResponse({'error':serializer.errors}, status=400)


class orderDetals(APIView):
    def get(self, req, format=None):
        records = MenuItems.objects.all()
        serializer = MenuItemsSerializer(records, many=True)
        return render(req, "index.html", {"items": serializer.data})

    def post(self, req, format=None):
        serializer = OrdersSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            records = MenuItems.objects.all()
            return render(req, "index.html", {"items": records})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def cart(req):
    return render(req, "user-cart.html")


def login(req):
    if req.method=="POST":
        username = req.POST["username"]
        password = req.POST["password"]

        user = authenticate(req, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                auth_login(req,user)
                return redirect('admin/')
    form = AuthenticationForm()
    return render(req, 'login.html', {'form': form})



