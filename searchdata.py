import sqlite3

# Membuka koneksi ke database
koneksi = sqlite3.connect("cars.db")

# Membuat cursor untuk menjalankan perintah SQL
cursor = koneksi.cursor()

# Menjalankan query untuk mencari data dengan id = 101
cursor.execute("""
    SELECT * FROM TBCars
    WHERE id = 102
""")

# Menampilkan hasil pencarian
print(cursor.fetchall())

# Menutup koneksi ke database
koneksi.close()
