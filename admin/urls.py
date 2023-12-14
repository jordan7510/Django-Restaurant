from . import views
from django.urls import path

urlpatterns = [
    path("", views.adminhome, name="adminhome"),
    path("reservations", views.adminreserv, name="adminreserv"),
    path("items", views.adminitems, name="adminitems"),
]
