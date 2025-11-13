
from django.shortcuts import HttpResponse, render, get_object_or_404
from .models import Item
from django.db.models import Min, F 
def get_items(request):
    items = (
        Item.objects  
        .aggregate(
            min_cost=Min(F('price') * F('quantity')), 
        )
    )

    min_cost = items['min_cost']
    return HttpResponse({min_cost})