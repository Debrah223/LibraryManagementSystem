from django.shortcuts import render
from rest_framework import generics, status
from .models import Book, Checkout
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, CheckoutSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.utils import timezone


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # To ensure only authenticated users can access

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # To ensure only authenticated users can access
 
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields = ['title', 'author', 'isbn']  # to search for fields using query parameters

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Anyone can create a user

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update/delete

class CheckoutBookView(generics.CreateAPIView):
    serializer_class = CheckoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        book_id = request.data.get("book")
        user = request.user

        try:
            book = Book.objects.get(id=book_id)
            if book.copies_available < 1:
                return Response({"error": "No copies available"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Check if the user already checked out this book
            if Checkout.objects.filter(user=user, book=book, return_date__isnull=True).exists():
                return Response({"error": "You have already checked out this book"}, status=status.HTTP_400_BAD_REQUEST)

            # Create a checkout record
            checkout = Checkout.objects.create(user=user, book=book)
            book.copies_available -= 1
            book.save()

            return Response(CheckoutSerializer(checkout).data, status=status.HTTP_201_CREATED)

        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

class ReturnBookView(generics.UpdateAPIView):
    serializer_class = CheckoutSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        checkout_id = kwargs.get("pk")

        try:
            checkout = Checkout.objects.get(id=checkout_id, user=request.user, return_date__isnull=True)
            checkout.return_date = timezone.now()
            checkout.save()

            # Increase book availability
            checkout.book.copies_available += 1
            checkout.book.save()

            return Response(CheckoutSerializer(checkout).data, status=status.HTTP_200_OK)

        except Checkout.DoesNotExist:
            return Response({"error": "No active checkout record found"}, status=status.HTTP_404_NOT_FOUND)