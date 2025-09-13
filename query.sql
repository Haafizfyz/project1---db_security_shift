-- membuat database baru bernama db_security_shift
create database db_security_shift;

-- memilih database yang akan digunakan
use db_security_shift;


-- membuat tabel security_staff untuk menyimpan data satpam
create table security_staff (
    staff_id int auto_increment primary key,  -- ID unik satpam (auto increment)
    name varchar(100) not null,               -- Nama satpam (maks 100 karakter)
    gender enum('male','female') not null,    -- Jenis kelamin (hanya male atau female)
    age int,                                  -- Umur satpam
    contact varchar(20)                       -- Nomor kontak satpam
);


-- membuat tabel shift untuk menyimpan info shift kerja
create table shift(
    shift_id int auto_increment primary key,   -- ID unik shift
    shift_name varchar(50) not null,           -- Nama shift (contoh: pagi, malam)
    start_time time not null,                  -- Jam mulai shift
    end_time time not null                     -- Jam selesai shift
);


-- membuat tabel schedule untuk menyimpan jadwal satpam masuk shift tertentu
create table schedule(
    schedule_id int auto_increment primary key,                    -- ID unik jadwal
    staff_id int not null,                                         -- ID satpam (relasi ke tabel security_staff)
    shift_id int not null,                                         -- ID shift (relasi ke tabel shift)
    date DATE not null,                                            -- Tanggal jadwal
    foreign key (staff_id) references security_staff(staff_id),    -- Relasi ke tabel security_staff
    foreign key (shift_id) references shift(shift_id)              -- Relasi ke tabel shift
);


-- membuat tabel attendance untuk mencatat absensi satpam
create table attendance(
    attendance_id int auto_increment primary key,                 -- ID unik absensi
    staff_id int not null,                                        -- ID satpam (relasi ke tabel security_staff)
    date DATE not null,                                           -- Tanggal absensi
    check_in time,                                                -- Waktu masuk
    check_out time,                                               -- Waktu pulang
    status ENUM('present','late','absent') not null,              -- Status kehadiran
    foreign key (staff_id) references security_staff(staff_id)    -- Relasi ke tabel security_staff
);


-- membuat tabel user untuk menyimpan akun login sistem
create table user(
    user_id int auto_increment primary key,                      -- ID unik user
    username varchar(50) unique not null,                        -- Username (harus unik)
    password varchar(255) not null,                              -- Password (disimpan dalam bentuk hash)
    role ENUM('admin','staff') not null,                         -- Role user (admin atau staff)
    staff_id int null,                                           -- Relasi ke tabel security_staff jika role = staff
    foreign key (staff_id) references security_staff(staff_id)   -- Relasi opsional ke security_staff
);