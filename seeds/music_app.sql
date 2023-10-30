-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables

DROP TABLE IF EXISTS tracks;
DROP SEQUENCE IF EXISTS tracks_id_seq;
DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

-- Then, we recreate them

CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    genre VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);


CREATE TABLE tracks (
  id SERIAL PRIMARY KEY,
  title text,
  artist_id int,
  album_id int,
  FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE CASCADE,
  FOREIGN KEY (album_id) REFERENCES albums(id) ON DELETE CASCADE
);






-- Finally, we add any records that are needed for the tests to run

INSERT INTO albums (title, release_year, artist_id) VALUES ('An Album', 2023, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Another Album', 1999, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('A Third Album', 2000, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('A Fourth Album', 2001, 4);

INSERT INTO artists (name, genre) VALUES ('Pixies', 'Rock');
INSERT INTO artists (name, genre) VALUES ('ABBA', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'Jazz');

INSERT INTO tracks (title, artist_id, album_id) VALUES ('A Track', 1, 1);
INSERT INTO tracks (title, artist_id, album_id) VALUES ('Another Track', 2, 2);
INSERT INTO tracks (title, artist_id, album_id) VALUES ('A Third Track', 3, 3);
INSERT INTO tracks (title, artist_id, album_id) VALUES ('A Fourth Track', 4, 4);

