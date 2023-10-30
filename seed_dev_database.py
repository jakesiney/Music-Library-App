from lib.database_connection import DatabaseConnection

# This file resets the database using the seeds file.
# This is useful if you want to start from scratch.

connection = DatabaseConnection(test_mode=False)
connection.connect()
connection.seed("seeds/music_app.sql")
