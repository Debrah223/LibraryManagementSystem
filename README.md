# LibraryManagementSystemAPI
1. Books Management (CRUD):

    I Implemented the ability to Create, Read, Update, and Delete (CRUD) books.
   POST/ GET/ PUT/ DELETE/ http://127.0.0.1:8000/api/books/
Creating a book 
POST http://127.0.0.1:8000/api/books/
    Each book has the following attributes: Title, Author, ISBN, Published Date, Number of available copies 
    Body
    {
    "title":  "The universe",

    "author": "Water brook",

    "isbn": "912098-654945",

    "published_date": "1928-07-28",
    
    "available copies": 11
    
    }
    I ensured validations such as a unique ISBN number for each book.
Get all books GET http://127.0.0.1:8000/api/books

Update a book with a token
PATCH http://127.0.0.1:8000/api/books/4/
Body 
{
  "title": "New Book Title",
  "author": "Updated Author"
}
To delete a book endpoint with a token
DELETE http://127.0.0.1:8000/api/books/3/

2. Users Management (CRUD):

    I Implemented CRUD operations for library users.
Register user
    POST http://127.0.0.1:8000/api/token/
    Body
    {
    "username": "kell",
    "email": "kell@gmail.com",
    "password": "kell1"
    }
    Login user
    POST http://127.0.0.1:8000/login/
     I ensured a user should have a unique Username, Email, Date of Membership, and Active Status.
Get all users
    GET http://127.0.0.1:8000/api/users/

To update user details
PATCH http://127.0.0.1:8000/api/users/9/
With a valid token
Body
{
    "email": "email@gmail.com"
}
with the user token
**To delete user**
DELETE http://127.0.0.1:8000/api/accounts/3/
A user can delete their account with authorized token

3. Check-Out and Return Books:

I Created an endpoint to allow users to check out available books.
    POST http://127.0.0.1:8000/api/checkout/
Only one copy of a book can be checked out per user at a time.
    Body
    {
    "book": 2
    }
    When a book is checked out, reduce the number of available copies.

    Ensure that users can only check out books if there are available copies.
    {
    "error": "You have already checked out this book"
    }
Created an endpoint to allow users to return checked-out books.
    PUT http://127.0.0.1:8000/api/return/2/
    Body
    {
    "book": 2,
    "user": 10
    }
Once a book is returned, increase the number of available copies.
    Log the date when the user checked out and returned each book.
    {
    "id": 2,
    "user": 10,
    "book": 2,
    "checkout_date": "2025-04-04T13:28:15.393435Z",
    "return_date": null
    }
4. View Available Books:

Created an endpoint to view all books and filter by availability (i.e., only show books with available copies).
    
    GET http://127.0.0.1:8000/api/books/available/
     {
        "id": 5,
        "title": "Your best life now",
        "author": "Joel Osteen",
        "isbn": "9870980030973",
        "published_date": "2021-08-23",
        "available_copies": 1
    },
Implemented query filters to search by Title, Author, or ISBN.
    GET http://127.0.0.1:8000/api/books/available/?title= The universe


What My Library Management System API Solves:
>Efficient book management
>User Management
>Secure Access
>Borrowing & Returning Books
>Search & Filter

