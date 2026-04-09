from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Category, Product
from api.serializers import CategorySerializer, ProductSerializer

# Product endpoints
class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

# Category endpoints
class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'category_id'

# Custom endpoint: /categories/<id>/products/
class CategoryProductsAPIView(APIView):
    def get(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=404)
        
        products = category.products.filter(is_active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)