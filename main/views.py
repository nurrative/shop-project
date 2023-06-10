from rest_framework import generics, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'price']
    ordering = ['-created_at']  # Новейшие продукты по умолчанию

    def get_queryset(self):
        queryset = super().get_queryset()
        promotional_products = self.request.query_params.get('promotional_products', None)
        if promotional_products is not None:
            queryset = queryset.filter(promotional_products=promotional_products)
        return queryset


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
