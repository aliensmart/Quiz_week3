# Quiz 3

For this quiz, use the attached `orm.py` file.

First, create a new subclass for our ORM called `TSLA`. It should have the fields `open`, `high`, `low`, `close`, and `adjusted_close` (all floats), and `volume`, an integer. It should also have a primary key, `pk`.

Write a separate script to insert all the data from the attached `TSLA.csv` into a database, using your new `TSLA` class. You can create the database however you choose (i.e. through Python, through the sqlite3 repl, etc.). Submit your database, `tsla.py`, and script by 11:00.