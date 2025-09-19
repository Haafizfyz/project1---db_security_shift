from database import Database  # Import class Database untuk koneksi ke MySQL

class Shift:
    def __init__(self, db):
        self.db = db  # Simpan instance Database agar bisa dipakai di method lain

    def create_shift(self, shift_name, start_time, end_time):
        query = "INSERT INTO shift (shift_name, start_time, end_time) VALUES (%s, %s, %s)"  # SQL query untuk tambah shift
        self.db.execute(query, (shift_name, start_time, end_time))  # Eksekusi query dengan parameter
        self.db.commit()  # Commit perubahan ke database
        print("Shift successfully added.")  # Cetak pesan sukses dalam bahasa Inggris

    def timedelta_to_str(self, td):  # Method untuk konversi objek timedelta MySQL TIME ke string HH:MM:SS
        """Convert MySQL TIME (timedelta) to string HH:MM:SS"""  # Docstring menjelaskan fungsi method
        total_seconds = int(td.total_seconds())  # Ambil total detik dari timedelta
        hours = total_seconds // 3600  # Hitung jam dari total detik
        minutes = (total_seconds % 3600) // 60  # Hitung menit dari sisa detik setelah dikurangi jam
        seconds = total_seconds % 60  # Hitung detik sisa
        return f"{hours:02}:{minutes:02}:{seconds:02}"  # Format ke string HH:MM:SS, selalu 2 digit


    def read_shift(self):  # Method untuk mengambil semua data shift
     """Fetch all shift data and format times"""  # Docstring menjelaskan fungsi method
     query = "SELECT * FROM shift"  # SQL query untuk ambil semua data dari tabel shift
     result = self.db.fetch_all(query)  # Eksekusi query dan ambil semua row sebagai list of dict

     formatted = []  # List kosong untuk menampung data yang sudah diformat
     for row in result:  # Loop setiap row dari hasil query
        row["start_time"] = self.timedelta_to_str(row["start_time"])  # Konversi start_time dari timedelta ke string HH:MM:SS
        row["end_time"] = self.timedelta_to_str(row["end_time"])  # Konversi end_time dari timedelta ke string HH:MM:SS
        formatted.append(row)  # Tambahkan row yang sudah diformat ke list
     return formatted  # Kembalikan list yang berisi semua shift dengan waktu yang sudah diformat

def update_shift(self, shift_id, shift_name=None, start_time=None, end_time=None):  # Method untuk update data shift, bisa update 1 field saja
     """Update shift, can update one or more fields"""  # Docstring menjelaskan fungsi method
     fields = []  # List untuk menampung field yang akan diupdate
     values = []  # List untuk menampung nilai baru dari field yang diupdate

     if shift_name:  # Jika parameter shift_name diberikan
         fields.append("shift_name=%s")  # Tambahkan ke list fields
         values.append(shift_name)  # Tambahkan nilai baru ke list values
     if start_time:  # Jika parameter start_time diberikan
         fields.append("start_time=%s")
         values.append(start_time)
     if end_time:  # Jika parameter end_time diberikan
         fields.append("end_time=%s")
         values.append(end_time)

     if not fields:  # Jika tidak ada field yang diberikan
         print("No field to update.")  # Tampilkan pesan
         return  # Keluar dari method

     query = f"UPDATE shift SET {', '.join(fields)} WHERE shift_id=%s"  # Buat query SQL dinamis
     values.append(shift_id)  # Tambahkan shift_id ke tuple values untuk kondisi WHERE

     self.db.execute(query, tuple(values))  # Eksekusi query dengan values
     self.db.commit()  # Commit perubahan ke database
     print("Shift updated successfully.")  # Tampilkan pesan sukses

def delete_shift(self, shift_id):  # Method untuk menghapus shift berdasarkan shift_id
     query = "DELETE FROM shift WHERE shift_id=%s"  # SQL query untuk menghapus shift tertentu
     self.db.execute(query, (shift_id,))  # Eksekusi query dengan parameter shift_id
     self.db.commit()  # Commit perubahan ke database
     print("Shift deleted successfully.")  # Tampilkan pesan sukses
