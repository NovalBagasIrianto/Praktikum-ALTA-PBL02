import sqlite3

# Membuat koneksi ke database
koneksi = sqlite3.connect("cars.db")

# Membuat cursor untuk menjalankan perintah SQL
cursor = koneksi.cursor()

# Menghapus data dari tabel TBCars dengan id = 102
cursor.execute("""
    DELETE FROM TBCars
    WHERE id = 102
""")

# (Optional) Menampilkan hasil, tapi untuk DELETE tidak ada data yang diambil
# print(cursor.fetchall())  ← sebaiknya dihapus atau dikomentari

# Menyimpan perubahan
koneksi.commit()

# Menutup koneksi
koneksi.close()