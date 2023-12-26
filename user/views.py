from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
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
     records = MenuItems.objects.all()
     serializer = MenuItemsSerializer(records, many=True)
     userDetails = User.objects.all()
     return render(req, "user-cart.html",{"items": serializer.data,"userDetails":userDetails})

def user_index(req):
    return render(req, "user_index.html")


def login(req):
    if req.method=="POST":
        username = req.POST["username"]
        password = req.POST["password"]

        user = authenticate(req, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                auth_login(req,user)
                return redirect('admin/')
            else:
               auth_login(req,user)
               return redirect('/')
   
    form = AuthenticationForm()
    return render(req, 'login.html', {'form': form})

def user_profile(request):
    return render(request, "user-profile.html")


def logout_view(request):
    logout(request)
    # Redirect to a page after logout (e.g., home page)
    return redirect('/') 


def signupApiView(req):
    if req.method =="POST":
        first_name= req.POST['first_name']
        last_name= req.POST['last_name']
        email= req.POST['email']
        mobile= req.POST['mobile']
        password= req.POST['password']
        my_user = User.objects.create_user(username=email,email=email,password=password)
        my_user.first_name=first_name
        my_user.last_name=last_name
        my_user.save()
        return redirect("/")
    
    return render(req, "signup.html")




