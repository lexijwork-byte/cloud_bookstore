import sys
import os

# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
from lib.database_connection_2 import DatabaseConnect
from lib.film_repository import FilmRepository

from playwright.sync_api import Page, expect

def test_book_list_contains_all_books(page: Page):
    connection = DatabaseConnect()
    connection.connect()
    connection.seed("./seeds/films.sql")

def test_book_list_contains_all_books_2(page: Page):
    
    page.goto("http://127.0.0.1:5001/film")

    films = page.locator('li')

    expected_films = [
      'The Hobbit'
    ]

    # here's the neat part which saves you from iterating over the `li` elements
    actual_films = films.all_inner_texts()

    assert actual_films == expected_films

def test_film_list_creates_film(page: Page):
    page.goto("http://127.0.0.1:5001/film")

    page.get_by_placeholder("Title").fill("Avengers")

    page.get_by_role("button", name="Submit").click()

    films = page.locator('li')
    new_film = films.all_inner_texts()[-1]

    assert new_film == "Avengers"