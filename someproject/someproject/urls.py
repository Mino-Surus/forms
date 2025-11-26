from django.contrib import admin
from django.urls import path, include
from someapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/', views.get_items),  
]