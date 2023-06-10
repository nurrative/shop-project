from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
]