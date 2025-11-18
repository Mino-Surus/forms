
from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Count, F 

def get_items(request):
    result = (
        Book
        .objects
        .values('publisher')
        .aggregate(
            sum_book=Count(F('id')), 
        )
    )

    return render(request,
              'main.html',
              {'sum_book': result})

    # sum_book = items['book']
    # return HttpResponse({sum_book})