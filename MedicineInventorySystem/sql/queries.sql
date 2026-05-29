USE medicine_inventory_db;

SELECT *
FROM Medicines
WHERE expiry_date <= DATE_ADD(CURDATE(), INTERVAL 30 DAY)
ORDER BY expiry_date;

SELECT m.medicine_name, SUM(pi.quantity) AS total_used
FROM Prescription_Items pi
JOIN Medicines m ON pi.medicine_id = m.medicine_id
GROUP BY m.medicine_id
ORDER BY total_used DESC;

SELECT p.full_name, pr.prescription_id, pr.prescription_date
FROM Patients p
JOIN Prescriptions pr ON p.patient_id = pr.patient_id
WHERE p.patient_id = 1
ORDER BY pr.prescription_date DESC;

SELECT m.medicine_name, SUM(pi.quantity) AS total_sold
FROM Prescription_Items pi
JOIN Prescriptions pr ON pi.prescription_id = pr.prescription_id
JOIN Medicines m ON pi.medicine_id = m.medicine_id
WHERE YEAR(pr.prescription_date) = 2023
GROUP BY m.medicine_id
ORDER BY total_sold DESC;

SELECT *
FROM Medicines
WHERE quantity < 20
ORDER BY quantity ASC;

SELECT b.bill_id, b.prescription_id, b.total
FROM Bills b
ORDER BY b.total DESC
LIMIT 5;

UPDATE Medicines
SET price = price * 1.05
WHERE medicine_id = 1;

DELETE FROM Prescription_Items
WHERE prescription_item_id = 1;
