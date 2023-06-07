from flask import jsonify, request
from models.book import Book
from app import db

def get_books():
    books = Book.query.all()
    results = [book.serialize() for book in books]
    return jsonify(results)

def get_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        return jsonify({'message': 'Book not found'})
    return jsonify(book.serialize())

def add_book():
    data = request.get_json()
    title = data['title']
    author = data['author']
    book = Book(title, author)
    db.session.add(book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'})

def update_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        return jsonify({'message': 'Book not found'})
    data = request.get_json()
    book.title = data['title']
    book.author = data['author']
    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})

def delete_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        return jsonify({'message': 'Book not found'})
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})
