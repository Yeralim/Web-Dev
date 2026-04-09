""" 
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product, Category

def products_list(request):
    products = Product.objects.filter(is_active=True)
    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'count': product.count,
            'is_active': product.is_active,
            'category': {
                'id': product.category.id,
                'name': product.category.name
            }
        })
    return JsonResponse(data, safe=False)

def product_detail(request, id):
    product = get_object_or_404(Product, id=id, is_active=True)
    data = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'count': product.count,
        'is_active': product.is_active,
        'category': {
            'id': product.category.id,
            'name': product.category.name
        }
    }
    return JsonResponse(data)

def categories_list(request):
    categories = Category.objects.all()
    data = []
    for category in categories:
        data.append({
            'id': category.id,
            'name': category.name
        })
    return JsonResponse(data, safe=False)

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    data = {
        'id': category.id,
        'name': category.name
    }
    return JsonResponse(data)

def category_products(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.products.filter(is_active=True)
    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'count': product.count,
            'is_active': product.is_active,
            'category': {
                'id': category.id,
                'name': category.name
            }
        })
    return JsonResponse(data, safe=False)
"""
    
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        """GET /api/categories/{id}/products/"""
        category = self.get_object()
        products = category.products.filter(is_active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer