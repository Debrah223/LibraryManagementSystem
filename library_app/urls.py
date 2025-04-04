from django.urls import path
from .views import BookListCreateView, BookDetailView, BookListView, UserListView, UserDetailView, CheckoutBookView, ReturnBookView, AvailableBooksView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'), #For creating books
    path('api/books/', BookListView.as_view(), name='book-list'),  #to list all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'), # allows updating and deleting books by ID.
    path('books/all/', BookListView.as_view(), name='book-list'),  # For retrieving books
    path('users/', UserListView.as_view(), name='user-list'), # to list users
    path('books/available/', AvailableBooksView.as_view(), name='available-books'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'), # allow deleting and updating users
    path('checkout/', CheckoutBookView.as_view(), name='checkout-book'),
    path('return/<int:pk>/', ReturnBookView.as_view(), name='return-book'),
]
