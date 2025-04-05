# LibraryManagementSystem
1. Books Management (CRUD):

    I Implemented the ability to Create, Read, Update, and Delete (CRUD) books.
   POST/ GET/ PUT/ DELETE/ http://127.0.0.1:8000/api/books/

    Each book has the following attributes: Title, Author, ISBN, Published Date, Number of available copies 
    {
    "title":  "The universe",

    "author": "Water brook",

    "isbn": "912098-654945",

    "published_date": "1928-07-28",
    
    "available copies": 11
    
}
    I ensured validations such as a unique ISBN number for each book.
2. Users Management (CRUD):

    I Implemented CRUD operations for library users.
    I ensured a user should have a unique Username, Email, Date of Membership, and Active Status.
    GET http://127.0.0.1:8000/api/users/
    {
        "id": 10,
        "username": "kell",
        "email": "kell@gmail.com",
        "date_joined": "2025-04-04T08:51:25.012918Z",
        "is_active": true
    }
3. Check-Out and Return Books:

    I Create an endpoint to allow users to check out available books.
    POST http://127.0.0.1:8000/api/checkout/

    Only one copy of a book can be checked out per user at a time.
    When a book is checked out, reduce the number of available copies.
    Ensure that users can only check out books if there are available copies.
    Create an endpoint to allow users to return checked-out books.
    PUT http://127.0.0.1:8000/api/return/2/
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

    Create an endpoint to view all books and filter by availability (i.e., only show books with available copies).
    
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



