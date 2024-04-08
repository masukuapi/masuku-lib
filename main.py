from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

@app.route("/")
def index():
    return render_template("index.html", books=books)

@app.route("/books", methods=["GET"])
def get_books():
    if request.headers.get("HX-Request"):
        # HTMX request, return partial HTML
        return render_template("_books.html", books=books)
    else:
        # API request, return JSON
        return jsonify(books)

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        if request.headers.get("HX-Request"):
            # HTMX request, return partial HTML
            return render_template("_book_details.html", book=book)
        else:
            # API request, return JSON
            return jsonify(book)
    else:
        return "Book not found", 404
@app.route("/mouse",methods=["GET"])
def mouse():
    print("Somthing happened")
    return "Something",200

if __name__ == "__main__":
    app.run(debug=True)
