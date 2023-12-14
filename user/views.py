from django.shortcuts import render
from .models import MenuItems

# Create your views here.
def homepage(req):
    records = MenuItems.objects.all()
    return render(req,"index.html",{'items':records})
