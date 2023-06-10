# from rest_framework import generics, filters
# from .models import Product
# from .serializers import ProductSerializer
#
# # class ProductListAPIView(generics.ListAPIView):
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer
# #     filter_backends = [filters.OrderingFilter]
# #     ordering_fields = ['created_at', 'price']
# #     ordering = ['-created_at']  # Новейшие продукты по умолчанию
# #
# #     def get_queryset(self):
# #         queryset = super().get_queryset()
# #         promotional_products = self.request.query_params.get('promotional_products', None)
# #         if promotional_products is not None:
# #             queryset = queryset.filter(promotional_products=promotional_products)
# #         return queryset
#
# from rest_framework import generics
# from rest_framework import filters
# from .models import Product
# from .serializers import ProductSerializer
#
# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [filters.OrderingFilter]
#
#     ordering_fields = ['created_at', 'price']
#     ordering = ['-created_at', 'price']  # Сортировка по умолчанию: новые продукты вначале, затем по возрастанию цены
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         # Фильтрация по наличию товара
#         available = self.request.query_params.get('available', None)
#         if available is not None:
#             queryset = queryset.filter(available=available)
#
#         # Фильтрация по наличию акции
#         promotional_products = self.request.query_params.get('promotional_products', None)
#         if promotional_products is not None:
#             queryset = queryset.filter(promotional_products=promotional_products)
#
#         return queryset

from rest_framework import generics
from rest_framework import filters
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]

    ordering_fields = ['created_at', 'price']
    ordering = ['-created_at', 'price']  # Сортировка по умолчанию: новые продукты вначале, затем по возрастанию цены

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

        # Дополнительные фильтры...
        # Добавьте здесь свои дополнительные фильтры, используя метод filter()

        return queryset


