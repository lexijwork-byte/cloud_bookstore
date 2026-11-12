import sys
import os

# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
from lib.DatabaseConnection import DatabaseConnection
from lib.book_repository import BookRepository

from playwright.sync_api import Page, expect

def test_book_list_contains_all_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/test_book_store.sql")

# a descriptive test name
def test_get_books_returns_a_200():
    # here's where we make the test client
    client = app.test_client()

    # here's where we make the request
    response = client.get("/books")

    # here's where we assert that the response's status code is 200
    assert response.status_code == 200

# a descriptive test name
def test_get_books_returns_all_the_books():

    client = app.test_client()
    response = client.get("/books")

    # here's where we assert that the response body contains all the books
    # note that we need to call .json on the response
    assert response.json == [
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

def test_get_authors_returns_200():
    client = app.test_client()

    response = client.get("/authors")

    assert response.status_code == 200

def test_get_authors_returns_all_authors():
    client = app.test_client()
    
    response = client.get("/authors")

    assert response.json == [
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

def test_book_list_contains_all_books_2(page: Page):
    
    page.goto("http://127.0.0.1:5001/book")

    books = page.locator('li')

    expected_books = [
      'The Gruffalo by Julia Donaldson',
      'Ada Twist, Scientist by Andrea Beaty',
      'The Girl Who Drank the Moon by Kelly Barnhill',
      'Dragons in a Bag by Zetta Elliott',
      'The Chroicles of Geronimo (the cat) by Geronimo',
      'The Chroicles of Geronimo (the cat) by Geronimo'
    ]

    # here's the neat part which saves you from iterating over the `li` elements
    actual_books = books.all_inner_texts()

    assert actual_books == expected_books

# def test_create_new_book(page: Page):
#     page.goto("http://127.0.0.1:5001/book")

#     page.get_by_placeholder("Title").fill("The Chroicles of Geronimo (the cat)")
#     page.get_by_placeholder("Author").fill("Geronimo")
#     page.get_by_role("button", name="Submit").click()

#     books = page.locator('li')
#     new_book = books.all_inner_texts()[-1]

#     assert new_book == "The Chroicles of Geronimo (the cat) by Geronimo"
