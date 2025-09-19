from database import Database  # Import class Database untuk koneksi MySQL

class Schedule:
    def __init__(self, db: Database):  # Constructor Schedule, menerima objek Database
         self.db = db  # Simpan objek Database agar bisa dipakai di semua method Schedule


    # ---------- Helper konversi timedelta ke str ----------
    def timedelta_to_str(self, td):  # Fungsi bantu untuk ubah MySQL TIME (timedelta) ke string HH:MM:SS
         """Konversi timedelta MySQL TIME ke string HH:MM:SS"""
         total_seconds = int(td.total_seconds())  # Ambil total detik dari timedelta
         hours = total_seconds // 3600  # Hitung jam
         minutes = (total_seconds % 3600) // 60  # Hitung menit
         seconds = total_seconds % 60  # Hitung detik
         return f"{hours:02}:{minutes:02}:{seconds:02}"  # Format string jadi HH:MM:SS


    def format_schedule_row(self, row):  # Fungsi untuk format kolom waktu di satu row schedule
         """Format kolom waktu supaya lebih enak dibaca"""
         if "start_time" in row and row["start_time"]:  # Cek apakah ada start_time dan tidak kosong
             row["start_time"] = self.timedelta_to_str(row["start_time"])  # Konversi timedelta ke string HH:MM:SS
         if "end_time" in row and row["end_time"]:  # Cek apakah ada end_time dan tidak kosong
             row["end_time"] = self.timedelta_to_str(row["end_time"])  # Konversi timedelta ke string HH:MM:SS
         return row  # Kembalikan row yang sudah diformat


    def create_schedule(self, staff_id, shift_id, day_of_week):  # Fungsi untuk menambahkan jadwal baru
         """Add a new schedule"""
         query = "INSERT INTO schedule (staff_id, shift_id, day_of_week) VALUES (%s, %s, %s)"  # SQL query insert
         self.db.execute(query, (staff_id, shift_id, day_of_week))  # Eksekusi query dengan parameter
         self.db.commit()  # Commit perubahan ke database
         print(f"Schedule for staff {staff_id}, shift {shift_id} on {day_of_week} has been added.")  # Cetak konfirmasi sukses


    def create_schedule(self, staff_id, shift_id, day_of_week):  # Fungsi untuk menambahkan jadwal baru
         """Add a new schedule"""
         query = "INSERT INTO schedule (staff_id, shift_id, day_of_week) VALUES (%s, %s, %s)"  # SQL query insert
         self.db.execute(query, (staff_id, shift_id, day_of_week))  # Eksekusi query dengan parameter
         self.db.commit()  # Commit perubahan ke database
         print(f"Schedule for staff {staff_id}, shift {shift_id} on {day_of_week} has been added.")  # Cetak konfirmasi sukses

    
    def read_schedule_by_staff(self, staff_id):  # Fungsi untuk mengambil jadwal khusus untuk satu staff
         """Get schedule for a specific staff"""
         query = """
         SELECT s.schedule_id, sh.shift_name, sh.start_time, sh.end_time, s.day_of_week
         FROM schedule s
         JOIN shift sh ON s.shift_id = sh.shift_id
         WHERE s.staff_id = %s
         ORDER BY FIELD(s.day_of_week,'Monday','Tuesday','Wednesday',
                   'Thursday','Friday','Saturday','Sunday')
         """  # SQL query ambil semua jadwal staff tertentu dan urutkan berdasarkan hari
         rows = self.db.fetch_all(query, (staff_id,))  # Eksekusi query dengan parameter staff_id
         return [self.format_schedule_row(r) for r in rows]  # Format kolom waktu dan kembalikan list hasil


    def update_schedule(self, schedule_id, staff_id=None, shift_id=None, day_of_week=None):  # Update schedule data, bisa pilih field mana saja
        """Update schedule data, can update any field"""
        fields = []  # List untuk menyimpan nama kolom yang mau diupdate
        values = []  # List untuk menyimpan nilai baru sesuai kolom

        if staff_id:  # Kalau staff_id diberikan
            fields.append("staff_id=%s")  # Tambahkan field staff_id ke query
            values.append(staff_id)       # Tambahkan nilai staff_id ke values
        if shift_id:  # Kalau shift_id diberikan
            fields.append("shift_id=%s")  # Tambahkan field shift_id ke query
            values.append(shift_id)       # Tambahkan nilai shift_id ke values
        if day_of_week:  # Kalau day_of_week diberikan
            fields.append("day_of_week=%s")  # Tambahkan field day_of_week ke query
            values.append(day_of_week)       # Tambahkan nilai day_of_week ke values

        if not fields:  # Kalau tidak ada field yang dipilih
            print("No fields to update.")  # Tampilkan pesan
            return  # Keluar dari fungsi

        query = f"UPDATE schedule SET {', '.join(fields)} WHERE schedule_id=%s"  # Buat query UPDATE dengan field yang dipilih
        values.append(schedule_id)  # Tambahkan schedule_id ke values untuk kondisi WHERE

        self.db.execute(query, tuple(values))  # Eksekusi query ke database
        self.db.commit()  # Commit perubahan
        print(f"Schedule with ID {schedule_id} successfully updated")  # Tampilkan pesan sukses


    def delete_schedule(self, schedule_id):  # Delete schedule by its ID
        """Delete schedule based on ID"""
        query = "DELETE FROM schedule WHERE schedule_id=%s"  # Buat query DELETE untuk schedule_id tertentu
        self.db.execute(query, (schedule_id,))  # Eksekusi query dengan parameter schedule_id
        self.db.commit()  # Commit perubahan ke database
        print(f"Schedule with ID {schedule_id} successfully deleted")  # Tampilkan pesan sukses

