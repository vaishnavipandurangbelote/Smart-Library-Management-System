from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

DB = "library.db"


# ---------------- DATABASE ----------------

def connect_db():
    return sqlite3.connect(DB)


def init_db():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            category TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ---------------- FRONTEND ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- REST API ----------------

# GET - View all books
@app.route("/books", methods=["GET"])
def get_books():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM books")
    books = cur.fetchall()

    conn.close()

    data = []

    for book in books:
        data.append({
            "id": book[0],
            "title": book[1],
            "author": book[2],
            "category": book[3],
            "status": book[4]
        })

    return jsonify(data)


# POST - Add a new book
@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO books(title, author, category, status) VALUES (?, ?, ?, ?)",
        (
            data["title"],
            data["author"],
            data["category"],
            "Available"
        )
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Book Added Successfully"})


# PUT - Update book status
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "UPDATE books SET status=? WHERE id=?",
        (data["status"], book_id)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Book Status Updated Successfully"})


# DELETE - Delete book
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM books WHERE id=?", (book_id,))

    conn.commit()
    conn.close()

    return jsonify({"message": "Book Deleted Successfully"})


# ---------------- MAIN ----------------

if __name__ == "__main__":
    init_db()
    app.run(debug=True)