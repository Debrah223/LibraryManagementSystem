from django.urls import path
from .views import BookListCreateView, BookDetailView, BookListView, UserListView, UserDetailView, CheckoutBookView, ReturnBookView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'), #For creating books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'), # allows updating and deleting books by ID.
    path('books/all/', BookListView.as_view(), name='book-list'),  # For retrieving books
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('checkout/', CheckoutBookView.as_view(), name='checkout-book'),
    path('return/<int:pk>/', ReturnBookView.as_view(), name='return-book'),
]
