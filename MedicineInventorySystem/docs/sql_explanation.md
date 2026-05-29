# SQL Explanation

## Create Tables
- create_tables.sql defines all tables with primary and foreign keys.

## Insert Scripts
- load_data.sql inserts at least 10 rows per table with realistic values.

## Views
- v_prescription_details combines patients, prescriptions, and medicines.
- v_bill_summary summarizes bills with patient names.

## Triggers
- bills_before_insert and bills_before_update calculate total = subtotal + tax - discount.
- prescription_item_after_insert decreases medicine stock after a prescription item is added.

## Queries
- Medicines near expiry
- Most used medicines
- Patient prescription history
- Total medicines sold in 2023
- Medicines with low quantity
- Bills with highest totals
- Update example for price changes
- Delete example for cleanup
