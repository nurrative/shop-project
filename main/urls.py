from django.urls import path
from .views import ProductListAPIView, CategoryListAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('category', CategoryListAPIView.as_view()),
]