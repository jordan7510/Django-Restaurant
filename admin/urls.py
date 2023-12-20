from . import views
from django.urls import path
from .views import adminOrdersApiView, AdminItemsApiView, AdmiItemsEdit, AdmiItemsDelete

urlpatterns = [
    path("", views.adminOrdersApiView.as_view(), name="adminOrders"),
    path("logout/", views.logout_view, name="logout"),
    path("reservations", views.adminReservationApiView.as_view(), name="adminreserv"),
    path("items", AdminItemsApiView.as_view(), name="adminitems"),
    path("items/edit/<int:item_id>/", AdmiItemsEdit.as_view(), name="adminitems-edit"),
    path("items/delete/<int:item_id>/", AdmiItemsDelete.as_view(), name="adminitems-delete"),
]
