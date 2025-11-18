from django.contrib import admin
from django.contrib import admin
from .models import Book, Author, Publisher

# admin.site.register(Manufacturer)
# admin.site.register(Item)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
