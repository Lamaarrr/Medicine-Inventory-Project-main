# Database Explanation

## Tables
- Patients: stores patient information.
- Medicines: stores medicine stock, expiry dates, and prices.
- Prescriptions: header table for each prescription made for a patient.
- Prescription_Items: medicines and quantities inside each prescription.
- Bills: billing totals for each prescription.

## Relationships
- One patient can have many prescriptions.
- One prescription can contain many medicines through Prescription_Items.
- One medicine can appear in many prescriptions.
- One prescription has exactly one bill.

## Keys and Constraints
- Each table has a primary key.
- Foreign keys connect Prescriptions to Patients, Prescription_Items to Prescriptions and Medicines, and Bills to Prescriptions.
- Bills has a unique prescription_id to keep one bill per prescription.

## Normalization (3NF)
- Each table stores one subject area.
- Non-key columns depend on the primary key.
- There are no repeating groups or partial dependencies.
