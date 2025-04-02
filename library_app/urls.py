from django.urls import path
from .views import BookListCreateView, BookDetailView, BookListView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'), #For creating books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'), # allows updating and deleting books by ID.
    path('books/all/', BookListView.as_view(), name='book-list'),  # For retrieving books

]
