from django.urls import  path,include
from rest_framework import routers
from .views import ProductViewSet, ProductReviewViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('reviews', ProductReviewViewSet, basename='product-review')

urlpatterns = [
    path('', include(router.urls)),
    # path('log_in/', include("rest_framework.urls")),
]