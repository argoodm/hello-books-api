from flask import Blueprint, jsonify

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description


books = [Book(1, "book A", "description A"), 
Book(2, "book B", "description  b"),
Book(3, "titlte", "description")]

hello_books_bp = Blueprint("hello_books", __name__)
books_bp = Blueprint("books", __name__, url_prefix="/books")

@hello_books_bp.route("/hello-books", methods=["GET"])

def say_hello_books():
    my_beautiful_books = "Hello books!"

    return my_beautiful_books, 200


@hello_books_bp.route("/hello/JSON", methods=["GET"])

def json_response():
    json_dict = {
        "title": "gideon the ninth",
        "description": "space!"
    }

    return json_dict, 200

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })

    return jsonify(books_response, 200)

@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    try:
        book_id = int(book_id)
    except:
        return {"message": f"book {book_id} invalid id"}
    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        
    return {"message": f"book{boo.id} not found"}, 404