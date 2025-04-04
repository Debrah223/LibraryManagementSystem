# LibraryManagementSystem
In my library app i have defined a book model with title, author, published date, ISBN, available copies as attributes
Step 2
I registered the models in django ADMIN in the books_app admin.py
Step3
I created a superuser account for login
Step 4
I created a Book serializer and added it in the app to allow books to be converted to and from JSON format.
Step 5:
I created views for CRUD operations in the library_app views.py. The main views I created were
    BookListCreateView: To Handle listing all books and adding a new book.
    BookDetailView: To Handle retrieving, updating, and deleting a book by ID.
Step 6: 
I created a url pattern in the library_app/ urls.py
Endpoints:
GET /api/books/ → List all books
POST /library_app/ → Add a new book
GET /libary_app/<id>/ → Get book details
PUT /libary_app/<id>/ → Update a book
DELETE /libary_app/<id>/ → Delete a book
Step 7:
I included url in the main project librarymanagement to ensure all book-related endpoints will be under /api/library_app/.
step 8:
I set up a new app accounts for user management
I registered it under main project as an app
Step 9:
I created a serializer for user registration in he accounts/serializers.py to Create users securely using create_user(), which hashes passwords.
Step 10:
I created views for registrarion and login in accounts/views.py
Endpoints:
    POST /register/ → Register a new user
    POST /login/ → Login and receive an authentication token
Step 11:
I created a configuration in the main project settings for Token Authentication → Users get a token when they log in and for Permissions → Only authenticated users can access the API.
Step 12:
Step 13:
I created a urls pattern in accounts/urls.py and also added it in the main project url(librarymanagement/urls)

Main endpoints









