# web_app/routes/book_routes.py

from flask import Blueprint, jsonify, request, render_template #, flash, redirect

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
    books = [
        {"id": 1, "title": "The Harry Potter Series"},
        {"id": 2, "title": "The First Law Series"},
        {"id": 3, "title": "Enders Game"},
    ]
    return jsonify(books)

@book_routes.route("/books")
def list_books_for_humans():
    books = [
        {"id": 1, "title": "The Harry Potter Series"},
        {"id": 2, "title": "The First Law Series"},
        {"id": 3, "title": "Enders Game"},
    ]
    return render_template("books.html", message="Here's some fantasy and sci fi books I love", books=books)

# @book_routes.route("/books/new")
# def new_book():
#     return render_template("new_book.html")

# @book_routes.route("/books/create", methods=["POST"])
# def create_book():
#     print("FORM DATA:", dict(request.form))
#     # todo: store in database
#     return jsonify({
#         "message": "BOOK CREATED OK (TODO)",
#         "book": dict(request.form)
#     })
#     #flash(f"Book '{new_book.title}' created successfully!", "success")
#     #return redirect(f"/books")