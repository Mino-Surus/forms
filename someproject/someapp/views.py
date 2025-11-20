
from django.shortcuts import render
from .models import Book
from django.db.models import Count, F

def get_items(request):
    result = (
        Book
        .objects
        .values('publisher__name') 
        .annotate(
            sum_book=Count(F('id')), 
        )
    )

    # total_books = sum(item['sum_book'] for item in result)

    return render(request, 'main.html', {
        'publishers': result,
        # 'total_books': total_books  

    })
