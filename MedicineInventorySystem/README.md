# Medicine Inventory Management System

A beginner-friendly DBMS graduation project that manages patients, medicines, prescriptions, and billing using MySQL and a simple Flask web app.

## Technologies Used
- MySQL
- Python (Flask)
- HTML, CSS

## Folder Structure
```
MedicineInventorySystem/
│
├── README.md
├── report.docx
├── presentation.pptx
├── video_link.txt
│
├── sql/
│   ├── create_tables.sql
│   ├── load_data.sql
│   ├── queries.sql
│   ├── triggers.sql
│   └── views.sql
│
├── src/
│   ├── app.py
│   ├── database.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── medicines.html
│   │   ├── patients.html
│   │   ├── prescriptions.html
│   │   └── bills.html
│   │
│   ├── static/
│   │   └── style.css
│   │
│   └── requirements.txt
│
└── docs/
    ├── ERD.png
    ├── schema.png
    ├── database_explanation.md
    ├── sql_explanation.md
    ├── flask_explanation.md
    ├── project_structure.md
    ├── erd_explanation.md
    └── setup_guide.md
```

## Database Setup
1. Create a MySQL database and user.
2. Open MySQL and run the scripts in this order:
   1) sql/create_tables.sql
   2) sql/triggers.sql
   3) sql/views.sql
   4) sql/load_data.sql
3. (Optional) Run sql/queries.sql to test queries.

## Configure the App
1. Open src/database.py and update your MySQL credentials.
2. Install dependencies:
   ```
   pip install -r src/requirements.txt
   ```
3. Run the Flask app:
   ```
   python src/app.py
   ```
4. Open http://127.0.0.1:5000 in your browser.

## Screenshots
- Home Page: (add screenshot)
- Medicines Page: (add screenshot)
- Patients Page: (add screenshot)
- Prescriptions Page: (add screenshot)
- Bills Page: (add screenshot)

## Notes
- docs/ERD.png and docs/schema.png are placeholders. Replace them with exported images from your ERD tool.
- For beginner-friendly explanations, see the markdown files in docs/.
