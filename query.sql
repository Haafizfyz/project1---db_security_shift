-- ================================================
-- STEP 1: buat database
-- ================================================
CREATE DATABASE db_security_shift;           -- buat database baru
USE db_security_shift;                       -- aktifkan database

-- ================================================
-- STEP 2: tabel security_staff
-- menyimpan data satpam
-- ================================================
CREATE TABLE security_staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,     -- id unik satpam
    name VARCHAR(100) NOT NULL,                  -- nama satpam
    gender ENUM('male','female') NOT NULL,       -- jenis kelamin
    age INT,                                     -- umur satpam
    contact VARCHAR(20)                          -- nomor kontak satpam
);

-- ================================================
-- STEP 3: tabel shift
-- menyimpan info shift kerja
-- ================================================
CREATE TABLE shift (
    shift_id INT AUTO_INCREMENT PRIMARY KEY,     -- id unik shift
    shift_name VARCHAR(50) NOT NULL,             -- nama shift (misal: morning, night)
    start_time TIME NOT NULL,                    -- jam mulai
    end_time TIME NOT NULL                       -- jam selesai
);

-- ================================================
-- STEP 4: tabel schedule
-- menyimpan jadwal satpam berdasarkan hari
-- ================================================
CREATE TABLE schedule (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,              -- id unik jadwal
    staff_id INT NOT NULL,                                   -- satpam yang bertugas
    shift_id INT NOT NULL,                                   -- shift yang ditentukan
    day_of_week ENUM('monday','tuesday','wednesday',
                     'thursday','friday','saturday','sunday') NOT NULL, -- hari kerja
    FOREIGN KEY (staff_id) REFERENCES security_staff(staff_id),
    FOREIGN KEY (shift_id) REFERENCES shift(shift_id)
);

-- ================================================
-- STEP 5: tabel attendance
-- catatan absensi satpam
-- ================================================
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,   -- id unik absensi
    staff_id INT NOT NULL,                          -- satpam yang absen
    date DATE NOT NULL,                             -- tanggal absensi
    check_in TIME,                                  -- jam masuk
    check_out TIME,                                 -- jam keluar
    status ENUM('present','absent','late') NOT NULL, -- status absen
    FOREIGN KEY (staff_id) REFERENCES security_staff(staff_id)
);

-- ================================================
-- STEP 6: tabel user
-- akun login sistem
-- ================================================
CREATE TABLE user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,         -- id unik user
    username VARCHAR(50) NOT NULL UNIQUE,           -- username untuk login
    password VARCHAR(255) NOT NULL,                 -- password (disarankan hash)
    role ENUM('admin','staff') NOT NULL,            -- peran user
    staff_id INT,                                   -- relasi ke satpam (jika role = staff)
    FOREIGN KEY (staff_id) REFERENCES security_staff(staff_id)
);
