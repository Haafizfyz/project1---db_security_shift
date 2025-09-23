from database import Database  # import class Database supaya bisa koneksi dan eksekusi query

class SecurityStaff:
    def __init__(self, db: Database):
         # Simpan object Database ke atribut class, supaya semua method bisa akses database
         self.db = db

    def create_staff(self, name, age, contact):
         """Tambah data security baru"""
         query = "INSERT INTO security_staff (name, age, contact) VALUES (%s, %s, %s)" # SQL query untuk insert data baru ke tabel security_staff
         self.db.execute(query, (name, age, contact)) # Eksekusi query dengan parameter name, age, contact
         self.db.commit() # Commit perubahan ke database
         print(f"Staff {name} successfully added.")  # Cetak pesan sukses

    def read_staff(self):
         """Ambil semua data security"""  # Docstring: menjelaskan fungsi method
         query = "SELECT * FROM security_staff"  # SQL query untuk mengambil semua data di tabel security_staff
         return self.db.fetch_all(query)  # Eksekusi query dan kembalikan semua hasil sebagai list of dict

    def update_staff(self, staff_id, name=None, age=None, contact=None):
         """Update data staff, bisa pilih field mana aja"""  # Docstring: fungsi ini fleksibel, bisa update satu atau beberapa field
    
         fields = []  # List untuk menyimpan nama kolom yang akan diupdate
         values = []  # List untuk menyimpan nilai baru yang akan diupdate

         if name:  # Jika parameter name diberikan
            fields.append("name=%s")  # Tambahkan string SQL untuk kolom name
            values.append(name)       # Tambahkan nilai baru ke list values

         if age:  # Jika parameter age diberikan
            fields.append("age=%s")   # Tambahkan string SQL untuk kolom age
            values.append(age)        # Tambahkan nilai baru ke list values

         if contact:  # Jika parameter contact diberikan
            fields.append("contact=%s")  # Tambahkan string SQL untuk kolom contact
            values.append(contact)       # Tambahkan nilai baru ke list values

         if not fields:  # Jika tidak ada field yang ingin diupdate
            print("No fields to update.")  # Beri tahu user
            return  # Keluar dari fungsi

         # Buat query UPDATE dinamis berdasarkan field yang ingin diubah
         query = f"UPDATE security_staff SET {', '.join(fields)} WHERE staff_id=%s"
         values.append(staff_id)  # Tambahkan staff_id sebagai parameter terakhir untuk WHERE clause

         self.db.execute(query, tuple(values))  # Eksekusi query dengan nilai-nilai yang sudah dikumpulkan
         self.db.commit()  # Simpan perubahan ke database
         print(f"Staff with ID {staff_id} successfully updated.")  # Beri feedback ke user

    def delete_staff(self, staff_id):
         """Hapus data security"""  
         query = "DELETE FROM security_staff WHERE staff_id = %s"  # Siapkan query untuk hapus staff berdasarkan staff_id
         self.db.execute(query, (staff_id,))  # Eksekusi query dengan parameter staff_id
         self.db.commit()  # Commit perubahan ke database
         print(f"Staff with ID {staff_id} successfully deleted.")  # Cetak pesan sukses
