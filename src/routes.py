from flask import request, jsonify
from models import User, Book
from db import db
from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')


# Helper function for serializing users and books
def serialize_user(user):
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }

def serialize_book(book):
    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "published_date": book.published_date
    }

# Routes for User CRUD operations
@bp.route("/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        new_user = User(username=data.get("username"), email=data.get("email"), password=data.get("password"))
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@bp.route("/users", methods=["GET"])
def get_all_users():
    try:
        users = User.query.all()
        user_list = [serialize_user(user) for user in users]
        return jsonify({"users": user_list})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):  
    try:
        # sourcery skip: use-named-expression
        user = User.query.get(user_id)
        if user:
            return jsonify(serialize_user(user))
        return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Route to update a user by ID
@bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        # sourcery skip: use-named-expression
        user = User.query.get(user_id)
        if user:
            data = request.get_json()
            user.username = data.get("username", user.username)
            user.email = data.get("email", user.email)
            user.password = data.get("password", user.password)
            db.session.commit()
            return jsonify({"message": "User updated successfully"})
        return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Route to delete a user by ID
@bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        # sourcery skip: use-named-expression
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "User deleted successfully"})
        return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Routes for Book CRUD operations
# Route to create a new book
@bp.route("/books", methods=["POST"])
def create_book():
    try:
        data = request.get_json()
        new_book = Book(
            title=data.get("title"),
            author=data.get("author"),
            published_date=data.get("published_date"),
        )
        db.session.add(new_book)
        db.session.commit()
        return jsonify({"message": "Book created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Route to get all books
@bp.route("/books", methods=["GET"])
def get_all_books():
    try:
        books = Book.query.all()
        book_list = [
            {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "published_date": book.published_date,
            }
            for book in books
        ]
        return jsonify({"books": book_list})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Route to get a specific book by ID
@bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    try:
        # sourcery skip: use-named-expression
        book = Book.query.get(book_id)
        if book:
            return jsonify(
                {
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "published_date": book.published_date,
                }
            )
        return jsonify({"message": "Book not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Route to update a book by ID
@bp.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    try:
        # sourcery skip: use-named-expression
        book = Book.query.get(book_id)
        if book:
            data = request.get_json()
            book.title = data.get("title", book.title)
            book.author = data.get("author", book.author)
            book.published_date = data.get("published_date", book.published_date)
            db.session.commit()
            return jsonify({"message": "Book updated successfully"})
        return jsonify({"message": "Book not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Route to delete a book by ID
@bp.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    try:
        # sourcery skip: use-named-expression
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return jsonify({"message": "Book deleted successfully"})
        return jsonify({"message": "Book not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# General error handler
@bp.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Resource not found"}), 404


@bp.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error"}), 500
