from django.urls import path
from .views import ProductList

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),  # /api/products/
]
