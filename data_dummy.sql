-- ====================================
--         MENGISI DATA DUMMY
-- ====================================
use db_security_shift;
-- ====================================
-- Data dummy untuk security_staff
insert into security_staff(name, gender, age, contact) values
('Budi Santoso', 'male', 35, '081234567890'),
('Andi Wijaya', 'male', 30, '081234567891'),
('Rudi Hartono', 'male', 33, '081234567892'),
('Agus Pratama', 'male', 29, '081234567893');

-- ====================================
-- Data dummy untuk shift
insert into shift(shift_name, start_time, end_time) values
('Morning', '07:00:00', '19:00:00'),
('Night',   '19:00:00', '07:00:00');

-- ====================================
-- Data dummy untuk schedule
insert into schedule (staff_id, shift_id, day_of_week) values
-- ===== MONDAY =====
(1, 1, 'monday'),   -- Budi masuk shift Morning
(2, 2, 'monday'),   -- Andi masuk shift Night

-- ===== TUESDAY =====
(3, 1, 'tuesday'),  -- Joko masuk shift Morning
(4, 2, 'tuesday'),  -- Rudi masuk shift Night

-- ===== WEDNESDAY =====
(1, 1, 'wednesday'), -- Budi masuk shift Morning
(3, 2, 'wednesday'), -- Joko masuk shift Night

-- ===== THURSDAY =====
(2, 1, 'thursday'), -- Andi masuk shift Morning
(4, 2, 'thursday'), -- Rudi masuk shift Night

-- ===== FRIDAY =====
(1, 1, 'friday'),   -- Budi masuk shift Morning
(2, 2, 'friday'),   -- Andi masuk shift Night

-- ===== SATURDAY =====
(3, 1, 'saturday'), -- Joko masuk shift Morning
(4, 2, 'saturday'), -- Rudi masuk shift Night

-- ===== SUNDAY =====
(1, 1, 'sunday'),   -- Budi masuk shift Morning
(4, 2, 'sunday');   -- Rudi masuk shift Night

-- ====================================
-- Data dummy untuk attendance
insert into attendance (staff_id, date, check_in, check_out, status) values
-- Monday (2025-09-08)
(1, '2025-09-08', '07:02:00', '19:01:00', 'present'),   -- Budi hadir shift pagi
(2, '2025-09-08', '19:05:00', '07:01:00', 'late'),      -- Andi telat masuk shift malam

-- Tuesday (2025-09-09)
(3, '2025-09-09', '07:00:00', '19:00:00', 'present'),   -- Joko hadir shift pagi
(4, '2025-09-09', '19:00:00', '07:00:00', 'present'),   -- Rudi hadir shift malam

-- Wednesday (2025-09-10)
(1, '2025-09-10', '07:10:00', '19:00:00', 'late'),      -- Budi telat masuk shift pagi
(3, '2025-09-10', '19:00:00', '07:00:00', 'present'),   -- Joko hadir shift malam

-- Thursday (2025-09-11)
(2, '2025-09-11', '07:00:00', '19:00:00', 'present'),   -- Andi hadir shift pagi
(4, '2025-09-11', '19:00:00', '07:00:00', 'present'),   -- Rudi hadir shift malam

-- Friday (2025-09-12)
(1, '2025-09-12', '07:00:00', '19:00:00', 'present'),   -- Budi hadir shift pagi
(2, '2025-09-12', '19:15:00', '07:00:00', 'late'),      -- Andi telat shift malam

-- Saturday (2025-09-13)
(3, '2025-09-13', '07:00:00', '19:00:00', 'present'),   -- Joko hadir shift pagi
(4, '2025-09-13', '19:00:00', '07:00:00', 'present'),   -- Rudi hadir shift malam

-- Sunday (2025-09-14)
(1, '2025-09-14', '07:00:00', '19:00:00', 'present'),   -- Budi hadir shift pagi
(4, '2025-09-14', '19:00:00', null, 'absent');          -- Rudi absen shift malam

-- ====================================
-- Data dummy untuk user
insert into user (username, password, role, staff_id) values
('admin', 'admin123', 'admin', null),  -- akun admin utama
('budi', 'budi123', 'staff', 1),       -- akun untuk staff Budi
('andi', 'andi123', 'staff', 2),       -- akun untuk staff Andi
('joko', 'joko123', 'staff', 3),       -- akun untuk staff Joko
('rudi', 'rudi123', 'staff', 4);       -- akun untuk staff Rudi

use db_security_shift;
select * from security_staff;
select * from attendance;
use db_security_shift;
select * from schedule;
select * from shift;
select * from user;

use db_security_shift;
DELETE FROM shift 
WHERE shift_id BETWEEN 4 AND 5;
