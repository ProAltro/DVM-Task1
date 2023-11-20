import sqlite3

conn = sqlite3.connect("timetable_app.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS timetable")
cur.execute(
    "CREATE TABLE timetable (id INTEGER PRIMARY KEY, com_cod INTEGER, id TEXT, title TEXT, credits TEXT, sections TEXT)"
)
