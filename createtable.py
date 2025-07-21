import sqlite3

# Membuat koneksi ke database
koneksi = sqlite3.connect("cars.db")

# Membuat cursor untuk menjalankan perintah SQL
cursor = koneksi.cursor()

# Menjalankan perintah untuk membuat tabel jika belum ada
cursor.execute("""
    CREATE TABLE IF NOT EXISTS TBCars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        brand TEXT NOT NULL,
        model TEXT NOT NULL,
        price REAL NOT NULL
    )
""")
