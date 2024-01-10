from django.template.defaulttags import url
from django.urls import path, include
from rest_framework import routers
from .views import productApp, productGet

# router = routers.DefaultRouter()
#
# router.register(r'products', ProductView)
#
# urlpatterns = router.urls

urlpatterns = [
    path('products', productGet),
    path('products/<int:pk>/', productGet),
    path('addproduct/', productApp),
]

