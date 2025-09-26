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
INSERT INTO schedule (staff_id, shift_id, day_of_week) VALUES
-- Monday
(1, 1, 'Monday'),
(2, 1, 'Monday'),
(3, 2, 'Monday'),
(4, 2, 'Monday'),

-- Tuesday
(17, 1, 'Tuesday'),
(18, 1, 'Tuesday'),
(1, 2, 'Tuesday'),
(2, 2, 'Tuesday'),

-- Wednesday
(3, 1, 'Wednesday'),
(4, 1, 'Wednesday'),
(17, 2, 'Wednesday'),
(18, 2, 'Wednesday'),

-- Thursday
(1, 1, 'Thursday'),
(2, 1, 'Thursday'),
(3, 2, 'Thursday'),
(4, 2, 'Thursday'),

-- Friday
(17, 1, 'Friday'),
(18, 1, 'Friday'),
(1, 2, 'Friday'),
(2, 2, 'Friday'),

-- Saturday
(3, 1, 'Saturday'),
(4, 1, 'Saturday'),
(17, 2, 'Saturday'),
(18, 2, 'Saturday'),

-- Sunday
(1, 1, 'Sunday'),
(2, 1, 'Sunday'),
(3, 2, 'Sunday'),
(4, 2, 'Sunday');

-- ====================================
-- Data dummy untuk attendance
INSERT INTO attendance (staff_id, date, check_in, check_out, status) VALUES
-- Monday (2025-09-22)
(1, '2025-09-22', '07:02:00', '19:01:00', 'present'),   
(2, '2025-09-22', '19:05:00', '07:01:00', 'late'),      
(3, '2025-09-22', NULL, NULL, 'absent'),                
(4, '2025-09-22', '07:00:00', '19:02:00', 'present'),   

-- Tuesday (2025-09-23)
(17, '2025-09-23', '07:01:00', '19:00:00', 'present'),  
(18, '2025-09-23', '19:00:00', '07:02:00', 'present'),  
(1, '2025-09-23', NULL, NULL, 'absent'),                
(2, '2025-09-23', '07:10:00', '19:05:00', 'late'),      

-- Wednesday (2025-09-24)
(3, '2025-09-24', '07:00:00', '19:00:00', 'present'),
(4, '2025-09-24', '19:02:00', '07:01:00', 'present'),
(17, '2025-09-24', '07:20:00', '19:15:00', 'late'),
(18, '2025-09-24', NULL, NULL, 'absent'),

-- Thursday (2025-09-25)
(1, '2025-09-25', '07:00:00', '19:00:00', 'present'),
(2, '2025-09-25', '19:01:00', '07:00:00', 'present'),
(3, '2025-09-25', '07:15:00', '19:10:00', 'late'),
(4, '2025-09-25', '19:02:00', '07:02:00', 'present'),

-- Friday (2025-09-26)
(17, '2025-09-26', NULL, NULL, 'absent'),
(18, '2025-09-26', '19:01:00', '07:00:00', 'present'),
(1, '2025-09-26', '07:01:00', '19:00:00', 'present'),
(2, '2025-09-26', '19:20:00', '07:05:00', 'late'),

-- Saturday (2025-09-27)
(3, '2025-09-27', NULL, NULL, 'absent'),
(4, '2025-09-27', '19:00:00', '07:02:00', 'present'),
(17, '2025-09-27', '07:00:00', '19:00:00', 'present'),
(18, '2025-09-27', '19:15:00', '07:10:00', 'late'),

-- Sunday (2025-09-28)
(1, '2025-09-28', '07:02:00', '19:00:00', 'present'),
(2, '2025-09-28', '19:00:00', '07:02:00', 'present'),
(3, '2025-09-28', '07:01:00', '19:01:00', 'present'),
(4, '2025-09-28', NULL, NULL, 'absent');

-- ====================================
-- Data dummy untuk user
insert into user (username, password, role, staff_id) values
('admin', 'admin123', 'admin', null),  -- akun admin utama
('budi', 'budi123', 'staff', 1),       -- akun untuk staff Budi
('andi', 'andi123', 'staff', 2),       -- akun untuk staff Andi
('rudi', 'rudi123', 'staff', 3),       -- akun untuk staff Rudi
('agus', 'agus123', 'staff', 4);       -- akun untuk staff Agus
('bambang', 'bambang123', 'staff', 17); -- akun untuk staff Bambang
('rizky', 'rizky123', 'staff', 18); -- akun untuk staff Rizky

use db_security_shift;
select * from security_staff;
select * from attendance;
use db_security_shift;
select * from schedule;
select * from shift;
select * from user;

use db_security_shift;
DELETE FROM schedule;
WHERE shift_id BETWEEN 4 AND 5;

use db_security_shift;
INSERT INTO security_staff (name, age, contact)
VALUES 
('Bambang susanto', 32, '081234567891'),
('Rizky abdullah', 29, '081234567892');

use db_security_shift;
TRUNCATE TABLE attendance;
