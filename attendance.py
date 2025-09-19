from database import Database  # Import class Database untuk koneksi ke MySQL
from datetime import datetime, timedelta, time  # Import modul datetime untuk tanggal/waktu

class Attendance:
    def __init__(self, db: Database):
        self.db = db  # Simpan objek Database untuk eksekusi query

    def timedelta_to_str(self, td):  # Fungsi untuk konversi timedelta MySQL ke string HH:MM:SS
        """Convert MySQL TIME (timedelta) to string HH:MM:SS"""
        if td is None:  # Cek kalau nilai None
            return None  # Kembalikan None
        total_seconds = int(td.total_seconds())  # Konversi timedelta jadi total detik
        hours = total_seconds // 3600  # Hitung jam
        minutes = (total_seconds % 3600) // 60  # Hitung menit
        seconds = total_seconds % 60  # Hitung detik
        return f"{hours:02}:{minutes:02}:{seconds:02}"  # Format jadi string HH:MM:SS


    def timedelta_to_time(self, td):  # Fungsi untuk konversi timedelta MySQL ke datetime.time
        """Convert MySQL TIME (timedelta) to datetime.time object"""
        if td is None:  # Cek apakah td None
            return None  # Kembalikan None
        hours = td.seconds // 3600  # Ambil jam dari total detik
        minutes = (td.seconds % 3600) // 60  # Ambil menit
        seconds = td.seconds % 60  # Ambil detik
        return time(hour=hours, minute=minutes, second=seconds)  # Buat objek datetime.time

    
    def date_to_str(self, d):  # Fungsi untuk konversi datetime.date ke string
        """Convert datetime.date to string YYYY-MM-DD"""
        return d.strftime("%Y-%m-%d")  # Format date menjadi 'YYYY-MM-DD'

    def create_attendance(self, staff_id, date, check_in=None, check_out=None, status="present"):
        """Tambah data attendance baru (dipakai saat staff absen masuk/pulang)"""
        query = """
            INSERT INTO attendance (staff_id, date, check_in, check_out, status)
            VALUES (%s, %s, %s, %s, %s)
        """  # Query untuk insert data ke tabel attendance
        self.db.execute(query, (staff_id, date, check_in, check_out, status))  # Eksekusi query dengan nilai parameter
        self.db.commit()  # Commit supaya perubahan tersimpan di database
        print("Attendance record added successfully.")  # Pesan sukses (sudah diganti ke Inggris)


    def read_attendance(self):
        """Retrieve all attendance data (joined with staff name)"""
        query = """
            SELECT a.attendance_id, s.name AS staff_name, a.date, a.check_in, a.check_out, a.status
            FROM attendance a
            JOIN security_staff s ON a.staff_id = s.staff_id
            ORDER BY a.attendance_id ASC
        """  # Query untuk ambil semua data attendance dan join dengan tabel staff supaya dapat nama staff
        result = self.db.fetch_all(query)  # Eksekusi query dan ambil semua hasilnya

        formatted = []  # List kosong untuk menampung hasil yang sudah diformat
        for row in result:
            row["date"] = self.date_to_str(row["date"])  # Format tanggal jadi string 'YYYY-MM-DD'
            row["check_in"] = self.timedelta_to_str(row["check_in"])  # Format waktu check_in jadi 'HH:MM:SS'
            row["check_out"] = self.timedelta_to_str(row["check_out"])  # Format waktu check_out jadi 'HH:MM:SS'
            formatted.append(row)  # Masukkan row yang sudah diformat ke list
        return formatted  # Kembalikan list data attendance yang sudah diformat


    def update_attendance(self, attendance_id, check_in=None, check_out=None, status=None):
        """Update a specific attendance record"""
        fields = []  # List untuk menampung nama kolom yang mau diupdate
        values = []  # List untuk menampung nilai baru yang sesuai kolom

        if check_in:  # Kalau ada input check_in baru
            fields.append("check_in=%s")  # Tambahkan nama kolom ke query
            values.append(check_in)  # Tambahkan nilai baru ke values
        if check_out:  # Kalau ada input check_out baru
            fields.append("check_out=%s")
            values.append(check_out)
        if status:  # Kalau ada input status baru
            fields.append("status=%s")
            values.append(status)

        if not fields:  # Kalau tidak ada field yang diupdate
            print("No fields to update.")  # Tampilkan pesan ke user
            return

        query = f"UPDATE attendance SET {', '.join(fields)} WHERE attendance_id=%s"  # Buat query update dinamis
        values.append(attendance_id)  # Tambahkan ID attendance ke tuple values

        self.db.execute(query, tuple(values))  # Eksekusi query dengan parameter
        self.db.commit()  # Commit perubahan ke database
        print(f"Attendance with ID {attendance_id} has been successfully updated.")  # Pesan sukses


    def delete_attendance(self, attendance_id):
        """Delete an attendance record"""
        query = "DELETE FROM attendance WHERE attendance_id=%s"  # Buat query DELETE berdasarkan attendance_id
        self.db.execute(query, (attendance_id,))  # Eksekusi query dengan parameter attendance_id
        self.db.commit()  # Commit perubahan ke database
        print(f"Attendance with ID {attendance_id} has been successfully deleted.")  # Pesan sukses


 # ================= STAFF ACTION =================
    def check_in(self, staff_id):
        """Staff check in → automatically assign status present/late (prevent duplicate)"""
        today_name = datetime.now().strftime("%A")  # Get current day name, e.g., Monday
        today_date = datetime.now().date()          # Get current date
        now_time = datetime.now().time()            # Get current time

        # Get today's schedule for the staff
        query = """
            SELECT sh.start_time, sh.end_time 
            FROM schedule sc
            JOIN shift sh ON sc.shift_id = sh.shift_id
            WHERE sc.staff_id = %s AND sc.day_of_week = %s
        """
        schedule = self.db.fetch_one(query, (staff_id, today_name))  # Fetch schedule for staff today

        if not schedule:
            print("No schedule found for today.")  # Pesan jika tidak ada jadwal
            return

        # Check if already checked in today
        query = "SELECT * FROM attendance WHERE staff_id=%s AND date=%s"
        record = self.db.fetch_one(query, (staff_id, today_date))
        if record:
            print("You have already checked in today.")  # Pesan jika sudah check-in
            return

        # Convert start_time (timedelta) to datetime.time
        start_time = self.timedelta_to_time(schedule["start_time"])
        limit_time = (datetime.combine(today_date, start_time) + timedelta(minutes=5)).time()  # Grace period 5 min

        # Determine status: present or late
        status = "present" if now_time <= limit_time else "late"

        # Insert check-in record into attendance table
        query = """
            INSERT INTO attendance (staff_id, date, check_in, status)
            VALUES (%s, %s, %s, %s)
        """
        self.db.execute(query, (staff_id, today_date, now_time, status))  # Execute insert
        self.db.commit()  # Commit changes to DB
        print(f"Check in successful. Status: {status}")  # Success message


    def check_out(self, staff_id):
        """Staff check out → update today's attendance"""
        today_date = datetime.now().date()       # Get current date
        now_time = datetime.now().time()         # Get current time

        # Look for today's attendance record
        query = "SELECT * FROM attendance WHERE staff_id=%s AND date=%s"
        record = self.db.fetch_one(query, (staff_id, today_date))  # Fetch today's record

        if not record:
            # If no check-in record exists, create a new record with only check_out
            query = "INSERT INTO attendance (staff_id, date, check_out, status) VALUES (%s, %s, %s, %s)"
            self.db.execute(query, (staff_id, today_date, now_time, None))  # Insert record
            self.db.commit()  # Commit changes to DB
            print("No check-in record found, but check-out has been saved.")  # Success message
            return

        # Update check_out for existing attendance
        query = "UPDATE attendance SET check_out=%s WHERE attendance_id=%s"
        self.db.execute(query, (now_time, record["attendance_id"]))  # Execute update
        self.db.commit()  # Commit changes to DB
        print("Check-out successful.")  # Success message
