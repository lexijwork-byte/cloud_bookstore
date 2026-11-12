from flask import Flask, render_template, request, redirect
from lib.DatabaseConnection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.book import Book

from lib.database_connection_2 import DatabaseConnect
from lib.film_repository import FilmRepository
from lib.film import Film

# instantiate a Flask app object
app = Flask(__name__)

# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

# duplicate route
@app.route('/hello', methods=['GET'])
def hello_again():
    return "Hello, hello and hello again!"


@app.route('/books', methods=['GET'])
def books():
    return [
  {
    "title": "The Gruffalo",
    "author": "Julia Donaldson"
  },
  {
    "title": "Ada Twist, Scientist",
    "author": "Andrea Beaty"
  },
  {
    "title": "The Girl Who Drank the Moon",
    "author": "Kelly Barnhill"
  },
  {
    "title": "Dragons in a Bag",
    "author": "Zetta Elliott"
  }
]

@app.route('/authors', methods=['GET'])
def list_authors():
    return [
  {
    "name": "Julia Donaldson",
    "dob": "1948-09-16"
  },
  {
    "name": "Andrea Beaty",
    "dob": "1961-10-08"
  },
  {
    "name": "Kelly Barnhill",
    "dob": "1973-01-01"
  },
  {
    "name": "Zetta Elliott",
    "dob": "1979-11-11"
  }
]

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/book", methods=["GET"])
def get_books():
  connection = DatabaseConnection()
  connection.connect()
  book_repository = BookRepository(connection)
  books = book_repository.all()
  print(books)
  return render_template("books.html", books=books)

@app.route('/book', methods=['POST'])
def create_book():
   # make a new database connection
    connection = DatabaseConnection()
    connection.connect()

    # make a new instance of BookRepository
    book_repository = BookRepository(connection)

    # get the request body
    book_details = request.form

    # my BookRepository expects an instance of Book, so make one here
    book = Book(title=book_details["title"], author=book_details["author"])

    # save the book
    book_repository.create(book)

    return redirect("/book")

@app.route('/team', methods=['GET'])
def get_team():
  team = ["Dorothy", "Rose", "Blanche", "Sophia"]
  return render_template("team.html", team=team)

@app.route('/film', methods=['GET'])
def get_films():
  connection = DatabaseConnect()
  connection.connect()
  film_repository = FilmRepository(connection)
  films = film_repository.all()
  print(films)
  return render_template("films.html", films=films)

@app.route('/film', methods=['POST'])
def create_film():
   connection = DatabaseConnect()
   connection.connect()

   # make a new instance of BookRepository
     
   film_repository = FilmRepository(connection)
  
      # get the request body
   film_details = request.form
  
      # my BookRepository expects an instance of Book, so make one here
   film = Film(title=film_details["title"])
  
      # save the book
   film_repository.create(film)
  
   return redirect("/film")



# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

