
from django.urls import path, include
from .views import product_list, product_detail

app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    
    path('catalog/', product_list, name='catalog'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    
    

]