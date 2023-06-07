# routes/book_routes.py
from flask import Blueprint, jsonify, request
from controllers.book_controller import get_books, get_book, add_book, update_book, delete_book

book_routes = Blueprint('book_routes', __name__)

@book_routes.route('/books', methods=['GET'])
def get_all_books():
    return get_books()

@book_routes.route('/books/<book_id>', methods=['GET'])
def get_single_book(book_id):
    return get_book(book_id)

@book_routes.route('/books', methods=['POST'])
def create_book():
    return add_book()

@book_routes.route('/books/<book_id>', methods=['PUT'])
def update_single_book(book_id):
    return update_book(book_id)

@book_routes.route('/books/<book_id>', methods=['DELETE'])
def delete_single_book(book_id):
    return delete_book(book_id)
