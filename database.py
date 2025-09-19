import mysql.connector  # Import modul mysql.connector untuk koneksi MySQL

class Database:
    def __init__(self, host, user, password, database):
        # ================= Konfigurasi koneksi =================
        self.host = 'localhost'          # Host database, biasanya 'localhost'
        self.user = 'root'          # Username database
        self.password = 'Dabi0o0hfz'  # Password database
        self.database = 'db_security_shift'  # Nama database

        # ================= Atribut koneksi =================
        self.conn = None          # Akan menyimpan objek koneksi
        self.cursor = None        # Akan menyimpan objek cursor untuk eksekusi query

        # ================= Lakukan koneksi =================
        self.connect()            # Panggil method connect untuk langsung connect ke DB

    def connect(self):
        """Membuat koneksi ke database MySQL"""
        try:
            # ================= Buat koneksi =================
            self.conn = mysql.connector.connect(
                host=self.host,       # Host database
                user=self.user,       # Username
                password=self.password,# Password
                database=self.database # Nama database
            )

            # ================= Buat cursor =================
            self.cursor = self.conn.cursor(dictionary=True)  
            # dictionary=True supaya hasil query berupa dict, lebih mudah diakses per kolom

            print("Database connected")  # Informasi kalau koneksi berhasil

        except mysql.connector.Error as err:
            # Tangani error koneksi MySQL
            print(f"Error: {err}")

    def execute(self, query, params=None):
        """Eksekusi query (INSERT, UPDATE, DELETE)"""
        # params or () → kalau params None, pakai tuple kosong
        self.cursor.execute(query, params or ())
        return self.cursor  # kembalikan cursor, bisa cek lastrowid dsb

    def fetch_all(self, query, params=None):
        """Ambil banyak row (SELECT)"""
        self.cursor.execute(query, params or ())  # jalankan query
        return self.cursor.fetchall()             # ambil semua hasil sebagai list of dict

    def fetch_one(self, query, params=None):
        """Ambil satu row (SELECT)"""
        self.cursor.execute(query, params or ())  # jalankan query
        return self.cursor.fetchone()             # ambil satu row saja

    def commit(self):
        """Simpan perubahan ke DB"""
        self.conn.commit()  # commit wajib buat INSERT, UPDATE, DELETE

    def close(self):
        """Tutup koneksi"""
        if self.cursor:        # cek apakah cursor masih ada
            self.cursor.close()  # tutup cursor
        if self.conn:          # cek apakah koneksi masih ada
            self.conn.close()    # tutup koneksi
            print("Database connection closed")
