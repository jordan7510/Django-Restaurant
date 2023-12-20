from . import views
from django.urls import path
from .views import reservationDetails, orderDetals
from .views import *

urlpatterns = [
    # path("", views.homepage, name='homepage'),
    path("", orderDetals.as_view(), name='homepage'),
    path("add-reservation", reservationDetails.as_view(), name='add-reservation'),
    path("user-cart", views.cart, name='user-cart'),
    path("login", views.login, name='login'),
]
