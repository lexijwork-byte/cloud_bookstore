DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;


CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT
);