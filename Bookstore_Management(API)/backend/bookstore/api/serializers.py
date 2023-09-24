from rest_framework import serializers
from .models import BookStoreModel

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStoreModel
        fields = '__all__'