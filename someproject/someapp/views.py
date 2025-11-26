
from django.shortcuts import HttpResponse, get_object_or_404
from .models import Item, Manufacturer
from django.db.models import Count, F

def get_items(request):
    manufacturer = get_object_or_404(
        Manufacturer,
        name= 'Привет' 
    )
    item= Item(
        name= request.GET.get('name', ''),
        price= request.GET.get('price', '0'),
        quantity= request.GET.get('quantity', '0'),
        manufacturer=manufacturer
    )
    item.save()
    return HttpResponse(status=201)
