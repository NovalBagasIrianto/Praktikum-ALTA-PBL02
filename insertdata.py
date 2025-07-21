import sqlite3

# Membuat koneksi ke database
koneksi = sqlite3.connect("cars.db")

# Membuat cursor untuk menjalankan perintah SQL
cursor = koneksi.cursor()

# Menambahkan data ke tabel TBCars
cursor.execute("""
    INSERT INTO TBCars (
        id,
        name,
        brand,
        model,
        price
    ) VALUES (
        101,
        'Red Car',
        'Honda',
        'CRV',
        12000
    ),
    (   "102",
        "Yellow Car",
        "koenigsegg",
        "jesko",
        "60000"
    )
""")

# Menyimpan perubahan
koneksi.commit()

# Menutup koneksi
koneksi.close()