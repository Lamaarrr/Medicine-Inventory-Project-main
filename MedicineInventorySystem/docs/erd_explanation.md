# ERD Explanation

## Entities
- Patients
- Medicines
- Prescriptions
- Prescription_Items
- Bills

## Cardinality
- Patients to Prescriptions: one-to-many.
- Prescriptions to Prescription_Items: one-to-many.
- Medicines to Prescription_Items: one-to-many.
- Prescriptions to Bills: one-to-one.

## Participation
- Every prescription must belong to one patient.
- Every prescription item must reference one prescription and one medicine.
- Every bill must reference one prescription.

## Relationship Types
- Strong relationships are implemented with foreign keys.
- The junction table Prescription_Items handles the many-to-many relationship between Prescriptions and Medicines.
