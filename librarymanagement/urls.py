"""
URL configuration for librarymanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token  # Import token view
from library_app.views import BookListView, CheckoutBookView, ReturnBookView
from accounts.urls import RegisterView, LoginView

def home(request):
    return HttpResponse("Welcome to the Library Management System API")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/', include('library_app.urls')),  # Your API endpoints for books, users, etc.
    path('accounts/', include('accounts.urls')),  #  to include the register and login endpoints
    path('api/books/', include('library_app.urls')),  # To include book API routes
    path('api/books/', BookListView.as_view(), name='book-list'), #To list all books
    path('checkout/', CheckoutBookView.as_view(), name='checkout-book'),
    path('return/<int:pk>/', ReturnBookView.as_view(), name='return-book'),
    path('api/accounts/', include('accounts.urls')),  # Add authentication routes
    path('api-auth/', include('rest_framework.urls')),  # For REST framework authentication
    path('api/token/', obtain_auth_token, name='api-token'),  # Token authentication
]
