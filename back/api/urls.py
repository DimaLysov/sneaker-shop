from django.urls import path, include
from rest_framework import routers

from .viewsets.brand import BrandViewSet
from .viewsets.model_sneaker import ModelSneakerViewSet
from .viewsets.sku import SKUViewSet
from .viewsets.size import SizeViewSet
from .viewsets.cart_item import CartItemViewSet
from .viewsets.user import UserViewSet
from .viewsets.order import OrderViewSet
from .viewsets.item_order import ItemOrderViewSet

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'model-sneakers', ModelSneakerViewSet)
router.register(r'skus', SKUViewSet, basename='sku')
router.register(r'sizes', SizeViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'users', UserViewSet)
router.register('orders', OrderViewSet)
router.register('item_order', ItemOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
