from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # To include all fields

 # Validation to ensure the ISBN is unique
    def validate_isbn(self, value):
        if Book.objects.filter(isbn=value).exists():
            raise serializers.ValidationError("A book with this ISBN already exists.")
        return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined', 'is_active'] # to expose user details
