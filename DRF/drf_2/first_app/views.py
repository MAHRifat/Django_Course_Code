from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
from rest_framework.permissions import IsAuthenticated
from . import permissions

class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]    # Authanticate user na hoile product dekhte dibe na\
    permission_classes = [permissions.AdminOrReadOnly]    # costom permission
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.ReviewerOrReadOnly]  # costom permission
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializer
   