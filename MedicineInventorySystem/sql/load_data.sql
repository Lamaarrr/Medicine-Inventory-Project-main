USE medicine_inventory_db;

INSERT INTO Patients (full_name, phone, gender, age) VALUES
('Ahmed Hassan', '01011112222', 'Male', 28),
('Mona Adel', '01033334444', 'Female', 34),
('Sara Ali', '01055556666', 'Female', 22),
('Omar Khaled', '01077778888', 'Male', 41),
('Nour Said', '01099990000', 'Female', 30),
('Hany Mostafa', '01111112222', 'Male', 55),
('Dina Samir', '01133334444', 'Female', 27),
('Youssef Magdy', '01155556666', 'Male', 19),
('Laila Tarek', '01177778888', 'Female', 46),
('Khaled Nabil', '01199990000', 'Male', 37);

INSERT INTO Medicines (medicine_name, quantity, expiry_date, price) VALUES
('Paracetamol 500mg', 120, '2026-01-10', 20.00),
('Amoxicillin 500mg', 80, '2025-08-15', 45.00),
('Ibuprofen 400mg', 60, '2025-12-20', 30.00),
('Cough Syrup', 45, '2025-06-05', 55.00),
('Vitamin C 1000mg', 200, '2026-03-12', 25.00),
('Metformin 500mg', 70, '2025-09-18', 60.00),
('Aspirin 81mg', 90, '2026-02-28', 18.00),
('Omeprazole 20mg', 50, '2025-11-02', 65.00),
('Antihistamine 10mg', 85, '2025-07-25', 35.00),
('Insulin 100IU', 40, '2025-05-30', 120.00);

INSERT INTO Prescriptions (patient_id, prescription_date) VALUES
(1, '2023-01-10'),
(2, '2023-02-14'),
(3, '2023-03-20'),
(4, '2023-04-05'),
(5, '2023-05-11'),
(6, '2023-06-22'),
(7, '2023-07-15'),
(8, '2023-08-19'),
(9, '2023-09-03'),
(10, '2023-10-27');

INSERT INTO Prescription_Items (prescription_id, medicine_id, quantity, dosage) VALUES
(1, 1, 2, '1 tablet twice daily'),
(1, 5, 1, '1 tablet daily'),
(2, 2, 1, '1 capsule every 8 hours'),
(2, 4, 1, '10 ml twice daily'),
(3, 3, 2, '1 tablet after meals'),
(3, 9, 1, '1 tablet daily'),
(4, 6, 1, '1 tablet twice daily'),
(4, 8, 1, '1 capsule daily'),
(5, 7, 2, '1 tablet daily'),
(5, 1, 1, '1 tablet daily'),
(6, 10, 1, 'As directed'),
(6, 5, 1, '1 tablet daily'),
(7, 2, 1, '1 capsule every 8 hours'),
(7, 3, 1, '1 tablet after meals'),
(8, 4, 1, '10 ml twice daily'),
(8, 9, 2, '1 tablet daily'),
(9, 8, 1, '1 capsule daily'),
(9, 6, 1, '1 tablet twice daily'),
(10, 1, 2, '1 tablet twice daily'),
(10, 7, 1, '1 tablet daily');

INSERT INTO Bills (prescription_id, subtotal, tax, discount, total) VALUES
(1, 65.00, 3.25, 0.00, 0.00),
(2, 100.00, 5.00, 0.00, 0.00),
(3, 95.00, 4.75, 0.00, 0.00),
(4, 125.00, 6.25, 5.00, 0.00),
(5, 56.00, 2.80, 0.00, 0.00),
(6, 145.00, 7.25, 10.00, 0.00),
(7, 75.00, 3.75, 0.00, 0.00),
(8, 125.00, 6.25, 0.00, 0.00),
(9, 125.00, 6.25, 5.00, 0.00),
(10, 58.00, 2.90, 0.00, 0.00);
