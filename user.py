from database import Database  # Import class Database dari database.py

class User:
    def __init__(self, db: Database):
        self.db = db  # Simpan objek Database untuk dipakai di method lain

    def create_user(self, username, password, role, staff_id=None):
        """Tambah user baru"""
        query = "INSERT INTO user (username, password, role, staff_id) VALUES (%s, %s, %s, %s)"  # SQL untuk menambahkan user
        self.db.execute(query, (username, password, role, staff_id))  # Eksekusi query dengan parameter
        self.db.commit()  # Simpan perubahan ke database
        print(f"User {username} has been added successfully")  # Pesan sukses dalam bahasa Inggris


    def read_user(self):
        """Ambil semua data user"""
        query = "SELECT * FROM user"  # SQL untuk mengambil semua user
        return self.db.fetch_all(query)  # Eksekusi query dan ambil semua hasil

    def update_user(self, user_id, username=None, password=None, role=None, staff_id=None):
        """Update data user"""
        fields = []  # List untuk kolom yang akan diupdate
        values = []  # List untuk nilai baru tiap kolom

        if username:
            fields.append("username=%s")  # Tambah kolom username
            values.append(username)       # Tambah nilai username
        if password:
            fields.append("password=%s")  # Tambah kolom password
            values.append(password)       # Tambah nilai password
        if role:
            fields.append("role=%s")      # Tambah kolom role
            values.append(role)           # Tambah nilai role
        if staff_id is not None:
            fields.append("staff_id=%s")  # Tambah kolom staff_id
            values.append(staff_id)       # Tambah nilai staff_id

        if not fields:
            print("No fields to update.")  # Pesan kalau tidak ada yang diupdate
            return

        query = f"UPDATE user SET {', '.join(fields)} WHERE user_id=%s"  # Query update dinamis
        values.append(user_id)  # Tambahkan user_id untuk WHERE clause

        self.db.execute(query, tuple(values))  # Eksekusi query
        self.db.commit()  # Simpan perubahan
        print(f"User with ID {user_id} has been successfully updated")  # Pesan sukses


    def delete_user(self, user_id):
        """Hapus user"""
        query = "DELETE FROM user WHERE user_id=%s"  # Siapkan query untuk hapus user
        self.db.execute(query, (user_id,))          # Eksekusi query dengan parameter user_id
        self.db.commit()                             # Commit perubahan ke database
        print(f"User with ID {user_id} has been successfully deleted")  # Pesan sukses

    def validate_login(self, username, password):
        """Validasi login user"""
        query = "SELECT * FROM user WHERE username=%s AND password=%s"  # Query untuk cek username & password
        return self.db.fetch_one(query, (username, password))           # Eksekusi query dan ambil 1 record

