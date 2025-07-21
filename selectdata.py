import sqlite3

# Membuat koneksi ke database
koneksi = sqlite3.connect("cars.db")

# Membuat cursor untuk menjalankan perintah SQL
cursor = koneksi.cursor()

# Menjalankan perintah untuk mengambil semua data dari TBCars
cursor.execute("""
    SELECT * FROM TBCars
""")

# Menampilkan semua data yang diambil
print(cursor.fetchall())

# Menutup koneksi ke database
koneksi.close()