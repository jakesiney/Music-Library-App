from example_routes import apply_example_routes
import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.artist import Artist


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums/index.html", albums=albums)


# @app.route('/albums', methods=['POST'])
# def post_album():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     album = Album(
#         None,
#         request.form['title'],
#         request.form['release_year'],
#         request.form['artist_id'],
#     )
#     repository.create(album)
#     return "", 200


# @app.route('/albums', methods=['GET'])
# def get_albums():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     return "\n".join(
#         f"{album}" for album in repository.all()

#     )


@app.route('/artist', methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(
        request.form['name'],
        request.form['genre']
    )
    repository.create(artist)
    return "", 200


@app.route('/artist', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    return "\n".join(
        f"{artist}" for artist in repository.all())

# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:8000/emoji


@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 8000)))
