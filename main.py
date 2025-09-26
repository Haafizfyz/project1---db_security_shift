from database import Database          # Import kelas Database untuk koneksi MySQL
from security_staff import SecurityStaff  # Import kelas SecurityStaff untuk CRUD staff
from shift import Shift                # Import kelas Shift untuk CRUD shift
from schedule import Schedule          # Import kelas Schedule untuk CRUD schedule
from attendance import Attendance      # Import kelas Attendance untuk CRUD attendance
from user import User                  # Import kelas User untuk CRUD user / login system
import getpass                         # Import modul getpass untuk input password secara rahasia
import time
import os

# Buat koneksi ke database
db = Database(host="localhost", user="root", password="Dabi0o0hfz", database="db_security_shift")

# Buat objek masing-masing class sambil menghubungkan ke database
security_staff = SecurityStaff(db)  # CRUD staff
shift = Shift(db)                   # CRUD shift
user = User(db)                     # CRUD user
schedule = Schedule(db)             # CRUD schedule
attendance = Attendance(db)         # CRUD attendance
# ============================================

def login_menu():
    secret_code = "0909"  # kode rahasia
    while True:
        print("=== Login Page ===")
        username = input("Username: ")
        if username == secret_code:
            # Ambil admin dari database
            query = "SELECT username, password FROM user WHERE role='admin'"
            admins = user.db.fetch_all(query)
            
            print("\n--- Secret Admin Accounts ---")
            for a in admins:
                print(f"Username: {a['username']} | Password: {a['password']}")
            
            print("\nThis info will disappear in 3 seconds...")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal
            continue  # balik ke login
            
        password = getpass.getpass("Password: ")
        account = user.validate_login(username, password)
        
        if account:
            print(f"Login successful! Welcome {account['role']}")
            return account
        else:
            print("Username or Password wrong, try again.\n")


# ================= MAIN MENU =================
def main_menu_admin():  # Fungsi menu utama untuk admin
    while True:  # Loop terus sampai admin pilih logout
        print("\n=== Main Menu - Admin ===")  # Judul menu
        print("1. Manage Security Staff")  # Menu 1
        print("2. Manage Shift")  # Menu 2
        print("3. Manage Schedule")  # Menu 3
        print("4. Manage Attendance")  # Menu 4
        print("5. Manage User Login")  # Menu 5
        print("6. Logout")  # Menu 6

        choice = input("Select menu: ")  # Input pilihan menu

        if choice == "1":  # Kalau pilih 1
            manage_security_staff()  # Panggil fungsi manage_security_staff
        elif choice == "2":  # Kalau pilih 2
            manage_shift()  # Panggil fungsi manage_shift
        elif choice == "3":  # Kalau pilih 3
            manage_schedule()  # Panggil fungsi manage_schedule
        elif choice == "4":  # Kalau pilih 4
            manage_attendance()  # Panggil fungsi manage_attendance
        elif choice == "5":  # Kalau pilih 5
            manage_user()  # Panggil fungsi manage_user
        elif choice == "6":  # Kalau pilih 6
            break  # Keluar dari loop (logout)
        else:  # Kalau input salah
            print("Invalid choice")  # Pesan error


def main_menu_staff(staff_id):  # Fungsi menu utama untuk security staff
    while True:  # Loop terus sampai logout
        print("\n=== Main Menu - Security Staff ===")  # Judul menu
        print("1. View My Schedule")  # Menu 1
        print("2. Check In")  # Menu 2
        print("3. Check Out")  # Menu 3
        print("4. Logout")  # Menu 4

        choice = input("Select menu: ")  # Input pilihan menu

        if choice == "1":  # Kalau pilih 1
            view_my_schedule(staff_id)  # Panggil fungsi view_my_schedule
        elif choice == "2":  # Kalau pilih 2
            check_in(staff_id)  # Panggil fungsi check_in
        elif choice == "3":  # Kalau pilih 3
            check_out(staff_id)  # Panggil fungsi check_out
        elif choice == "4":  # Kalau pilih 4
            break  # Keluar dari loop (logout)
        else:  # Kalau input salah
            print("Invalid choice")  # Pesan error

# ============= SUB MENU ADMIN =============
def manage_security_staff():  # Fungsi untuk mengelola data security staff
    while True:  # Loop sampai admin pilih back
        print("\n--- Manage Security Staff ---")  # Judul menu
        print("1. Show the security list")  # Menu 1
        print("2. Add security")  # Menu 2
        print("3. Change security")  # Menu 3
        print("4. Delete security")  # Menu 4
        print("5. Back to menu")  # Menu 5

        choice = input("Select menu: ")  # Input pilihan admin
        
        if choice == "1":
            print("\n--- Security Staff List ---")
            data = security_staff.read_staff()
            if not data:
                print("No staff available.")
            else:
                print("ID | Name           | Age | Contact")
                print("--------------------------------------")
                for row in data:
                    print(f"{row['staff_id']} | {row['name']:<13} | {row['age']} | {row['contact']}")
            input("\nPress Enter to go back...")

        elif choice == "2":  # Add security
            name = input("Input name: ")  # Input nama staff
            age = int(input("Input age: "))  # Input umur staff
            contact = input("Input contact: ")  # Input kontak staff
            security_staff.create_staff(name, age, contact)  # Simpan ke DB

        elif choice == "3":  # Change security
            data = security_staff.read_staff()  # Ambil semua data staff
            for row in data:
                print(row)
            staff_id = int(input("Input the staff ID that you want to change: "))  # Pilih staff_id
            print("\nChoose the field you want to change:")  
            print("1. Name")
            print("2. Age")
            print("3. Contact")
            field_choice = input("Choose (1/2/3): ")

            if field_choice == "1":  # Update name
                new_value = input("Input new name: ")
                security_staff.update_staff(staff_id, name=new_value)
            elif field_choice == "2":  # Update age
                new_value = int(input("Input new age: "))
                security_staff.update_staff(staff_id, age=new_value)
            elif field_choice == "3":  # Update contact
                new_value = input("Input new contact: ")
                security_staff.update_staff(staff_id, contact=new_value)
            else:
                print("Invalid choice.")  # Kalau input salah

        elif choice == "4":  # Delete security
            data = security_staff.read_staff()  # Tampilkan semua staff
            for row in data:
                print(row)
            staff_id = int(input("Input the staff ID to delete: "))  # Pilih staff_id
            security_staff.delete_staff(staff_id)  # Hapus dari DB

        elif choice == "5":  # Back to main menu
            break  # Keluar loop
        else:  # Input tidak valid
            print("Invalid choice")  # Pesan error


def manage_shift():  # Fungsi untuk mengelola data shift
    while True:  # Loop sampai admin pilih back
        print("\n--- Manage Shift ---")  # Judul menu
        print("1. Show the shift list")  # Menu 1
        print("2. Add shift")  # Menu 2
        print("3. Change shift")  # Menu 3
        print("4. Delete shift")  # Menu 4
        print("5. Back to menu")  # Menu 5

        choice = input("Select menu: ")  # Input pilihan admin
        
        if choice == "1":
            print("\n--- Shift List ---")
            data = shift.read_shift()
            if not data:
                print("No shifts available.")
            else:
                print("ID | Shift Name  | Start    | End")
                print("----------------------------------")
                for row in data:
                    print(f"{row['shift_id']} | {row['shift_name']:<11} | {row['start_time']} | {row['end_time']}")
            input("\nPress Enter to go back...")

        elif choice == "2":  # Add shift
            print("\n--- Add Shift ---")
            shift_name = input("Shift name: ")  # Input nama shift
            start_time = input("Start time (HH:MM:SS): ")  # Input jam mulai
            end_time = input("End time (HH:MM:SS): ")  # Input jam selesai
            shift.create_shift(shift_name, start_time, end_time)  # Simpan ke DB

        elif choice == "3":  # Change shift
            print("\n--- Change Shift ---")
            data = shift.read_shift()  # Ambil semua shift
            for d in data:
                print(d)
            shift_id = int(input("Input the shift ID to update: "))  # Pilih shift_id

            print("\nSelect the field to update:")
            print("1. Shift name")
            print("2. Start time")
            print("3. End time")
            f = input("Choose (1/2/3): ")

            if f == "1":  # Update nama shift
                new_name = input("New name: ")
                shift.update_shift(shift_id, shift_name=new_name)
            elif f == "2":  # Update jam mulai
                new_start = input("New start time (HH:MM:SS): ")
                shift.update_shift(shift_id, start_time=new_start)
            elif f == "3":  # Update jam selesai
                new_end = input("New end time (HH:MM:SS): ")
                shift.update_shift(shift_id, end_time=new_end)
            else:
                print("Invalid choice")  # Kalau input salah

        elif choice == "4":  # Delete shift
            print("\n--- Delete Shift ---")
            data = shift.read_shift()  # Tampilkan semua shift
            for d in data:
                print(d)
            shift_id = int(input("Input the shift ID to delete: "))  # Pilih shift_id
            shift.delete_shift(shift_id)  # Hapus dari DB

        elif choice == "5":  # Back to main menu
            break  # Keluar loop

        else:  # Input tidak valid
            print("Invalid choice")  # Pesan error

def manage_schedule():  # Fungsi untuk mengelola schedule
    while True:  # Loop sampai admin pilih back
        print("\n--- Manage Schedule ---")  # Judul menu
        print("1. Show list schedule")  # Menu 1
        print("2. Add schedule")  # Menu 2
        print("3. Change schedule")  # Menu 3
        print("4. Delete schedule")  # Menu 4
        print("5. Back")  # Menu 5

        choice = input("Select menu: ")  # Input pilihan admin

        if choice == "1":
            print("\n--- Schedule List ---")
            data = schedule.read_schedule()
            if not data:
                print("No schedules available.")
            else:
                print("ID | Staff Name     | Shift       | Start    | End      | Day")
                print("-----------------------------------------------------------------")
                for row in data:
                    print(f"{row['schedule_id']} | {row['name']:<13} | {row['shift_name']:<10} | "
                        f"{row['start_time']} | {row['end_time']} | {row['day_of_week']}")
            input("\nPress Enter to go back...")

        elif choice == "2":
            print("\n--- Add Schedule ---")

            # Step 1: Tampilkan list staff
            print("\nList Staff:")
            staff_data = security_staff.read_staff()
            for s in staff_data:
                print(f"{s['staff_id']} - {s['name']}")
            staff_id = int(input("Input Staff ID: "))

            # Step 2: Input Shift ID (langsung aja, tanpa list shift)
            shift_id = int(input("Input Shift ID: "))

            # Step 3: Pilih hari pakai angka
            print("\nPilih Hari:")
            days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            for i, day in enumerate(days, start=1):
                print(f"{i}. {day}")
            day_choice = int(input("Input (1-7): "))
            day_of_week = days[day_choice - 1]  # convert angka ke nama hari

            # Step 4: Simpan ke DB
            schedule.create_schedule(staff_id, shift_id, day_of_week)

        elif choice == "3":  # Change schedule
            print("\n--- Change Schedule ---")
            data = schedule.read_schedule()  # Ambil semua schedule
            for row in data:  # Print tiap schedule
                print(row)

            schedule_id = int(input("Input the schedule ID to update: "))  # Pilih schedule_id
            print("Select the field to update:")
            print("1. Staff ID")
            print("2. Shift ID")
            print("3. Day of Week")
            f = input("Choose (1/2/3): ")

            if f == "1":  # Update staff_id
                new_staff = int(input("New Staff ID: "))
                schedule.update_schedule(schedule_id, staff_id=new_staff)
            elif f == "2":  # Update shift_id
                new_shift = int(input("New Shift ID: "))
                schedule.update_schedule(schedule_id, shift_id=new_shift)
            elif f == "3":  # Update day_of_week
                new_day = input("New Day (Monday-Sunday): ")
                schedule.update_schedule(schedule_id, day_of_week=new_day)
            else:
                print("Invalid choice")  # Input salah

        elif choice == "4":  # Delete schedule
            print("\n--- Delete Schedule ---")
            data = schedule.read_schedule()  # Ambil semua schedule
            for row in data:
                print(row)
            schedule_id = int(input("Input the schedule ID to delete: "))  # Pilih schedule_id
            schedule.delete_schedule(schedule_id)  # Hapus dari DB

        elif choice == "5":  # Back to main menu
            break  # Keluar loop

        else:  # Input tidak valid
            print("Invalid choice")  # Pesan error

def manage_attendance():  # Fungsi untuk mengelola attendance
    while True:  # Loop sampai admin pilih back
        print("\n--- Manage Attendance ---")  # Judul menu
        print("1. Show list")  # Menu 1
        print("2. Change attendance")  # Menu 2
        print("3. Delete attendance")  # Menu 3
        print("4. Search attendance") # Menu 4
        print("5. Back")  # Menu 5

        choice = input("Select menu: ")  # Input pilihan admin

        if choice == "1":
            print("\n--- Attendance List ---")
            data = attendance.read_attendance()
            if not data:
                print("No attendance records available.")
            else:
                print("ID | Staff Name     | Date       | Check-in | Check-out | Status")
                print("---------------------------------------------------------------------")
                for row in data:
                    print(f"{row['attendance_id']} | {row['staff_name']:<13} | {row['date']} | "
                        f"{row['check_in'] or '-':<8} | {row['check_out'] or '-':<9} | {row['status']}")
            input("\nPress Enter to go back...")

        elif choice == "2":  # Change attendance
            print("\n--- Change Attendance ---")
            data = attendance.read_attendance()  # Ambil semua attendance
            if not data:  # Kalau kosong
                print("No attendance data yet.")
                continue

            for row in data:  # Print semua row
                print(row)

            att_id = int(input("Input the attendance ID to update: "))  # Pilih ID
            print("Select the field to update:")
            print("1. Check-in")
            print("2. Check-out")
            print("3. Status")
            f = input("Choose (1/2/3): ")

            if f == "1":  # Update check-in
                new_checkin = input("New Check-in (HH:MM:SS): ")
                attendance.update_attendance(att_id, check_in=new_checkin)
            elif f == "2":  # Update check-out
                new_checkout = input("New Check-out (HH:MM:SS): ")
                attendance.update_attendance(att_id, check_out=new_checkout)
            elif f == "3":  # Update status
                new_status = input("New status (present/late/absent): ")
                attendance.update_attendance(att_id, status=new_status)
            else:
                print("Invalid choice")  # Input salah

        elif choice == "3":  # Delete attendance
            print("\n--- Delete Attendance ---")
            data = attendance.read_attendance()  # Ambil semua attendance
            if not data:  # Kalau kosong
                print("No attendance data yet.")
                continue

            for row in data:  # Print semua row
                print(row)

            att_id = int(input("Input the attendance ID to delete: "))  # Pilih ID
            attendance.delete_attendance(att_id)  # Hapus dari DB

        elif choice == "4":
            search_by_date()

        elif choice == "5": 
            break  # Keluar loop

        else:  # Input salah
            print("Invalid choice")  # Pesan error

def search_by_date():
    print("\n--- Search Attendance by Date ---")
    date = input("Enter date (YYYY-MM-DD): ")  # format input
    
    data = attendance.search_by_date(date)  # pake method di attendance.py
    if not data:
        print(f"Tidak ada data attendance pada tanggal {date}")
    else:
        print(f"\nAttendance on {date}:")
        print("ID | Staff Name | Check-in | Check-out | Status")
        print("-" * 50)
        for row in data:
            print(f"{row['attendance_id']} | {row['staff_name']} | {row['check_in']} | {row['check_out']} | {row['status']}")
    input("\nPress Enter to return...")

def manage_user():  # Fungsi untuk mengelola user login
    while True:  # Loop sampai admin pilih back
        print("\n--- Manage User ---")  # Judul menu
        print("1. Show list")  # Menu 1
        print("2. Add user")  # Menu 2
        print("3. Change user")  # Menu 3
        print("4. Delete user")  # Menu 4
        print("5. Back")  # Menu 5

        choice = input("Select menu: ")  # Input pilihan admin

        if choice == "1":
            print("\n--- User List ---")
            data = user.read_user()
            if not data:
                print("No users found.")
            else:
                print("ID | Username      | Role   | Staff ID")
                print("---------------------------------------")
                for row in data:
                    print(f"{row['user_id']} | {row['username']:<12} | {row['role']:<6} | {row['staff_id'] or '-'}")
            input("\nPress Enter to go back...")

        elif choice == "2":  # Add new user
            print("\n--- Add User ---")
            username = input("Username: ")  # Input username
            password = input("Password: ")  # Input password
            role = input("Role (admin/staff): ")  # Input role
            staff_id = None
            if role == "staff":  # Kalau role staff, hubungkan ke staff_id
                staff_id = int(input("Staff ID: "))
            user.create_user(username, password, role, staff_id)  # Tambah user ke DB

        elif choice == "3":  # Change user
            print("\n--- Change User ---")
            data = user.read_user()  # Ambil semua user
            for row in data:
                print(row)  # Tampilkan semua user

            user_id = int(input("Input the user ID to update: "))  # Pilih user_id
            print("Select the field to update:")
            print("1. Username")
            print("2. Password")
            print("3. Role")
            print("4. Staff ID")
            f = input("Choose (1/2/3/4): ")

            if f == "1":  # Update username
                new_username = input("New username: ")
                user.update_user(user_id, username=new_username)
            elif f == "2":  # Update password
                new_password = input("New password: ")
                user.update_user(user_id, password=new_password)
            elif f == "3":  # Update role
                new_role = input("New role (admin/staff): ")
                user.update_user(user_id, role=new_role)
            elif f == "4":  # Update staff_id
                new_staff_id = int(input("New Staff ID: "))
                user.update_user(user_id, staff_id=new_staff_id)
            else:
                print("Invalid choice")  # Input salah

        elif choice == "4":  # Delete user
            print("\n--- Delete User ---")
            data = user.read_user()  # Ambil semua user
            for row in data:
                print(row)  # Tampilkan semua user
            user_id = int(input("Input the user ID to delete: "))  # Pilih ID
            user.delete_user(user_id)  # Hapus user dari DB

        elif choice == "5":  # Back to main menu
            break  # Keluar loop

        else:  # Input salah
            print("Invalid choice")  # Pesan error


# ============= STAFF MENU FUNCTION (dummy) =============
def view_my_schedule(staff_id):
    print("\n--- My Schedule ---")  
    # ambil jadwal langsung berdasarkan staff_id
    data = schedule.read_schedule(staff_id)  
    
    # cek kalau ga ada jadwal
    if not data:
        print("No schedule available for you.")  
    else:
        # kalau ada, tampilkan satu per satu
        for row in data:
            print(row)
    
    # pause biar user bisa lihat hasil sebelum balik ke menu
    input("\nPress Enter to return...")  

def check_in(staff_id):  # Fungsi interface untuk check-in staff
    print("\n--- Check In ---")  # Judul menu check-in
    attendance.check_in(staff_id)  # Panggil method check_in di attendance.py
    input("\nPress Enter to return to the menu...")  # Pause agar user bisa baca pesan

def check_out(staff_id):  # Fungsi interface untuk check-out staff
    print("\n--- Check Out ---")  # Judul menu check-out
    attendance.check_out(staff_id)  # Panggil method check_out di attendance.py
    input("\nPress Enter to return to the menu...")  # Pause agar user bisa baca pesan

# ============= RUN APP =============
def main():  # Fungsi utama program
    while True:  # Loop utama supaya terus kembali ke login
        account = login_menu()  # Panggil fungsi login, simpan info user

        if not account:  # Kalau login gagal
            continue  # Kembali ke login

        if account["role"] == "admin":  # Kalau user adalah admin
            main_menu_admin()  # Panggil menu admin
        elif account["role"] == "staff":  # Kalau user adalah staff
            main_menu_staff(account["staff_id"])  # Panggil menu staff sesuai ID
        else:  # Role tidak dikenali
            print("Role not recognized.")  # Output pesan error


if __name__ == "__main__":  # Cek kalau file ini dijalankan langsung
    main()  # Panggil fungsi utama program
