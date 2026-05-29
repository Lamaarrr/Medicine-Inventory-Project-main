USE medicine_inventory_db;

CREATE OR REPLACE VIEW v_prescription_details AS
SELECT pr.prescription_id, pr.prescription_date, p.full_name, m.medicine_name, pi.quantity, pi.dosage
FROM Prescriptions pr
JOIN Patients p ON pr.patient_id = p.patient_id
JOIN Prescription_Items pi ON pr.prescription_id = pi.prescription_id
JOIN Medicines m ON pi.medicine_id = m.medicine_id;

CREATE OR REPLACE VIEW v_bill_summary AS
SELECT b.bill_id, b.prescription_id, p.full_name, b.subtotal, b.tax, b.discount, b.total
FROM Bills b
JOIN Prescriptions pr ON b.prescription_id = pr.prescription_id
JOIN Patients p ON pr.patient_id = p.patient_id;
