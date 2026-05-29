from flask import Flask, render_template, request, redirect, url_for
from database import get_connection

app = Flask(__name__)


def fetch_all(query, params=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params or ())
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def fetch_one(query, params=None):
    rows = fetch_all(query, params)
    return rows[0] if rows else None


def execute(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    conn.commit()
    last_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return last_id


@app.route("/")
def index():
    patients_count = fetch_one("SELECT COUNT(*) AS count FROM Patients")["count"]
    medicines_count = fetch_one("SELECT COUNT(*) AS count FROM Medicines")["count"]
    prescriptions_count = fetch_one("SELECT COUNT(*) AS count FROM Prescriptions")["count"]
    bills_count = fetch_one("SELECT COUNT(*) AS count FROM Bills")["count"]

    latest_medicines = fetch_all(
        "SELECT medicine_name, quantity, expiry_date FROM Medicines ORDER BY expiry_date LIMIT 5"
    )
    latest_prescriptions = fetch_all(
        "SELECT pr.prescription_id, p.full_name, pr.prescription_date "
        "FROM Prescriptions pr JOIN Patients p ON pr.patient_id = p.patient_id "
        "ORDER BY pr.prescription_date DESC LIMIT 5"
    )

    return render_template(
        "index.html",
        patients_count=patients_count,
        medicines_count=medicines_count,
        prescriptions_count=prescriptions_count,
        bills_count=bills_count,
        latest_medicines=latest_medicines,
        latest_prescriptions=latest_prescriptions,
    )


@app.route("/medicines", methods=["GET", "POST"])
def medicines():
    if request.method == "POST":
        medicine_name = request.form.get("medicine_name")
        quantity = request.form.get("quantity")
        expiry_date = request.form.get("expiry_date")
        price = request.form.get("price")
        execute(
            "INSERT INTO Medicines (medicine_name, quantity, expiry_date, price) VALUES (%s, %s, %s, %s)",
            (medicine_name, quantity, expiry_date, price),
        )
        return redirect(url_for("medicines"))

    q = request.args.get("q", "").strip()
    if q:
        rows = fetch_all(
            "SELECT * FROM Medicines WHERE medicine_name LIKE %s ORDER BY medicine_name",
            (f"%{q}%",),
        )
    else:
        rows = fetch_all("SELECT * FROM Medicines ORDER BY medicine_name")

    return render_template("medicines.html", medicines=rows, q=q)


@app.route("/patients", methods=["GET", "POST"])
def patients():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        gender = request.form.get("gender")
        age = request.form.get("age")
        execute(
            "INSERT INTO Patients (full_name, phone, gender, age) VALUES (%s, %s, %s, %s)",
            (full_name, phone, gender, age),
        )
        return redirect(url_for("patients"))

    rows = fetch_all("SELECT * FROM Patients ORDER BY full_name")
    return render_template("patients.html", patients=rows)


@app.route("/prescriptions", methods=["GET", "POST"])
def prescriptions():
    patients_list = fetch_all("SELECT patient_id, full_name FROM Patients ORDER BY full_name")
    medicines_list = fetch_all(
        "SELECT medicine_id, medicine_name, price, quantity FROM Medicines ORDER BY medicine_name"
    )

    if request.method == "POST":
        patient_id = request.form.get("patient_id")
        medicine_id = request.form.get("medicine_id")
        quantity = int(request.form.get("quantity"))
        dosage = request.form.get("dosage")
        prescription_date = request.form.get("prescription_date")

        prescription_id = execute(
            "INSERT INTO Prescriptions (patient_id, prescription_date) VALUES (%s, %s)",
            (patient_id, prescription_date),
        )

        execute(
            "INSERT INTO Prescription_Items (prescription_id, medicine_id, quantity, dosage) VALUES (%s, %s, %s, %s)",
            (prescription_id, medicine_id, quantity, dosage),
        )

        price_row = fetch_one("SELECT price FROM Medicines WHERE medicine_id = %s", (medicine_id,))
        subtotal = float(price_row["price"]) * quantity
        tax = round(subtotal * 0.05, 2)
        discount = 0.00

        execute(
            "INSERT INTO Bills (prescription_id, subtotal, tax, discount, total) VALUES (%s, %s, %s, %s, %s)",
            (prescription_id, subtotal, tax, discount, 0.00),
        )

        return redirect(url_for("prescriptions"))

    rows = fetch_all(
        "SELECT pr.prescription_id, p.full_name, pr.prescription_date "
        "FROM Prescriptions pr JOIN Patients p ON pr.patient_id = p.patient_id "
        "ORDER BY pr.prescription_date DESC"
    )

    return render_template(
        "prescriptions.html",
        prescriptions=rows,
        patients=patients_list,
        medicines=medicines_list,
    )


@app.route("/bills")
def bills():
    rows = fetch_all(
        "SELECT b.bill_id, b.prescription_id, p.full_name, b.subtotal, b.tax, b.discount, b.total "
        "FROM Bills b JOIN Prescriptions pr ON b.prescription_id = pr.prescription_id "
        "JOIN Patients p ON pr.patient_id = p.patient_id "
        "ORDER BY b.total DESC"
    )
    return render_template("bills.html", bills=rows)


if __name__ == "__main__":
    app.run(debug=True)
