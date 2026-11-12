from lib.film import Film

class FilmRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all books
    def all(self):
        rows = self._connection.execute('SELECT * from films')
        films = []
        for row in rows:
            item = Film(row["title"], row["id"])
            films.append(item)
        return films

    # Find a single artist by their id
    def find(self, film_id):
        rows = self._connection.execute(
            'SELECT * from films WHERE id = %s', [film_id])
        row = rows[0]
        return Film(row["id"], row["title"])

    def create(self, film):
        self._connection.execute(
            'INSERT INTO films (title) VALUES (%s)',
            [film.title]
        )
        return None