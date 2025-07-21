import sqlite3

# Membuat koneksi ke database
koneksi = sqlite3.connect("cars.db")

# Membuat cursor untuk menjalankan perintah SQL
cursor = koneksi.cursor()

# Mengupdate data harga mobil dengan id = 101
cursor.execute("""
    UPDATE TBCars SET
        price = 50000
    WHERE
        id = 101
""")

# (Optional) Menampilkan hasil, meskipun untuk UPDATE biasanya tidak ada hasil yang ditampilkan
# print(cursor.fetchall())  ← sebaiknya dihapus atau dikomentari

# Menyimpan perubahan
koneksi.commit()

# Menutup koneksi ke database
koneksi.close()