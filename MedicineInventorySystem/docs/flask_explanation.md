# Flask Explanation

## Database Connection
- src/database.py contains a single function to open a MySQL connection.
- Update the host, user, password, and database name before running the app.

## Routes and Pages
- / : dashboard with quick counts and latest records.
- /medicines : add and search medicines.
- /patients : add and list patients.
- /prescriptions : add a prescription with one medicine item.
- /bills : view bills and totals.

## Project Flow
- The user adds patients and medicines.
- A prescription is created for a patient and one medicine item.
- A bill is created with subtotal, tax, and discount.
- The total is calculated by a trigger in MySQL.
