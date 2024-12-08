import sqlite3

DB_NAME = "ice_cream_parlor.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_db():
    conn = get_connection()
    with conn:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS Flavors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            season TEXT NOT NULL,
            price REAL NOT NULL
        );
        CREATE TABLE IF NOT EXISTS Ingredients (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            stock INTEGER NOT NULL,
            allergen_info TEXT
        );
        CREATE TABLE IF NOT EXISTS CustomerSuggestions (
            id INTEGER PRIMARY KEY,
            flavor_name TEXT NOT NULL,
            customer_name TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS Cart (
            id INTEGER PRIMARY KEY,
            flavor_id INTEGER NOT NULL,
            FOREIGN KEY(flavor_id) REFERENCES Flavors(id)
        );
        """)
    conn.close()
