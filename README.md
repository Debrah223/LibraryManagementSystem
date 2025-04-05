# LibraryManagementSystem
1. Books Management (CRUD):

    I Implemented the ability to Create, Read, Update, and Delete (CRUD) books.
    Each book has the following attributes: Title, Author, ISBN, Published Date, Number of Copies Available.
    I ensured validations such as a unique ISBN number for each book.
2. Users Management (CRUD):

    I Implemented CRUD operations for library users.
    I ensured a user should have a unique Username, Email, Date of Membership, and Active Status.
3. Check-Out and Return Books:

    I Create an endpoint to allow users to check out available books.

    Only one copy of a book can be checked out per user at a time.
    When a book is checked out, reduce the number of available copies.
    Ensure that users can only check out books if there are available copies.
    Create an endpoint to allow users to return checked-out books.
    Once a book is returned, increase the number of available copies.
    Log the date when the user checked out and returned each book.
4. View Available Books:

    Create an endpoint to view all books and filter by availability (i.e., only show books with available copies).
    Implement optional query filters to search by Title, Author, or ISBN.




