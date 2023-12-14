from django.shortcuts import render
from user.models import MenuItems



# Create your views here.
def adminhome(req):
    return render(req, 'admin_index.html')

def adminreserv(req):
    return render (req, 'admin_reservation.html')

def adminitems(req):

    if req.method == "POST":
        name = req.POST['itemName']
        desc = req.POST['itemDesc']
        type = req.POST['itemType']
        price = req.POST['itemPrice']
        # img = req.POST['itemImg']
        itemObject = MenuItems.objects.create(item_name=name, item_desc=desc, item_type=type, item_price=price)
        itemObject.save()
    records = MenuItems.objects.all()
    return render(req,'admin_items.html',{'items':records})


def editItems(req):
    if(req.method == "POST"):
        name = req.POST['itemName']
        desc = req.POST['itemDesc']
        type = req.POST['itemType']
        price = req.POST['itemPrice']
    




