from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path('library_app/', BookListCreateView.as_view(), name='book-list-create'),
    path('library_app/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
