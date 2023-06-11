from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.exceptions import APIException


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ('category__name', 'available', 'promotional_products')  # Обратите внимание на использование category__name

    ordering_fields = ['created_at', 'price']
    #фильтруем только по цене и по новинкам
    ordering = ['-created_at', 'price']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Фильтрация по наличию товара
        available = self.request.query_params.get('available', None)
        if available is not None:
            queryset = queryset.filter(available=available)

        # Фильтрация по наличию акции
        promotional_products = self.request.query_params.get('promotional_products', None)
        if promotional_products is not None:
            queryset = queryset.filter(promotional_products=promotional_products)

        category = self.request.query_params.get('category', None)
        if category is not None:
            category_queryset = Category.objects.values_list('name', flat=True).distinct()  # distinct() добавлен здесь
            if category not in category_queryset:
                raise APIException(f"Invalid category: {category}")
            queryset = queryset.filter(category__name=category)

        return queryset

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer