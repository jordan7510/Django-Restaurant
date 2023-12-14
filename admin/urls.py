from . import views
from django.urls import path
from .views import AdminItemsApiView,AdmiItemsEdit,AdmiItemsDelete

urlpatterns = [
    path("", views.adminhome, name="adminhome"),
    path("reservations", views.adminreserv, name="adminreserv"),
    path("items", AdminItemsApiView.as_view(), name="adminitems"),
    path("items/edit/<int:item_id>/", AdmiItemsEdit.as_view(), name="adminitems-edit"),
    path("items/delete/<int:item_id>/", AdmiItemsDelete.as_view(), name="adminitems-delete"),
]
