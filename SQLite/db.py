import sqlite3
import random

from faker import Faker


def create_cust(num):
    fake = Faker()
    data = []
    for i in range(0, num):
        data.append(
            (
                fake.first_name(),
                fake.last_name(),
                fake.address(),
                int(round(random.random(), 2) * 100),
            )
        )
    return data


def create_track(num):
    fake = Faker()
    data = []
    for i in range(0, num):
        data.append(
            (fake.name(), fake.date_between(), int(round(random.random(), 3) * 1000))
        )
    return data


con = sqlite3.connect("music.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS customers;")
cur.execute(
    """CREATE TABLE customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR NOT NULL,
            last_name VARCHAR NOT NULL,
            address VARCHAR NOT NULL,
            age VARCHAR(2) NOT NULL
            )"""
)

cur.execute("DROP TABLE IF EXISTS tracks;")
cur.execute(
    """CREATE TABLE tracks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist VARCHAR NOT NULL,
            release_date DATE NOT NULL,
            lasting_time INTEGER(3)
            )"""
)

customer_data = create_cust(100)
cur.executemany(
    "INSERT INTO customers (first_name, last_name, address, age) VALUES (?, ?, ?, ?)",
    customer_data,
)

track_data = create_track(100)
cur.executemany(
    "INSERT INTO tracks (artist, release_date, lasting_time) VALUES (?, ?, ?)",
    track_data,
)

con.commit()
