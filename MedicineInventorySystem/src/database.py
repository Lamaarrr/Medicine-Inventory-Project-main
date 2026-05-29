import mysql.connector
import sqlite3
import os
import re

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "medicine_inventory_db"
}

BASE_DIR = os.path.dirname(__file__)
SQL_DIR = os.path.normpath(os.path.join(BASE_DIR, "..", "sql"))
SQLITE_DB = os.path.join(BASE_DIR, "medicine_inventory.db")


class SQLiteCursorWrapper:
    def __init__(self, cur):
        self._cur = cur

    def _convert_placeholders(self, query):
        return query.replace("%s", "?")

    def execute(self, query, params=None):
        if params is None:
            return self._cur.execute(query)
        query = self._convert_placeholders(query)
        return self._cur.execute(query, params)

    def executemany(self, query, seq_of_params):
        query = self._convert_placeholders(query)
        return self._cur.executemany(query, seq_of_params)

    def fetchall(self):
        rows = self._cur.fetchall()
        return [dict(row) for row in rows]

    def fetchone(self):
        row = self._cur.fetchone()
        return dict(row) if row is not None else None

    @property
    def lastrowid(self):
        return self._cur.lastrowid

    def close(self):
        try:
            self._cur.close()
        except Exception:
            pass


class SQLiteConnectionWrapper:
    def __init__(self, conn):
        self._conn = conn

    def cursor(self, dictionary=False):
        self._conn.row_factory = sqlite3.Row
        cur = self._conn.cursor()
        return SQLiteCursorWrapper(cur)

    def commit(self):
        return self._conn.commit()

    def close(self):
        return self._conn.close()


def _init_sqlite_db():
    if os.path.exists(SQLITE_DB):
        return

    conn = sqlite3.connect(SQLITE_DB)
    conn.execute("PRAGMA foreign_keys = ON;")
    cur = conn.cursor()

    cur.executescript(r"""
    CREATE TABLE IF NOT EXISTS Patients (
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        phone TEXT NOT NULL,
        gender TEXT NOT NULL,
        age INTEGER NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Medicines (
        medicine_id INTEGER PRIMARY KEY AUTOINCREMENT,
        medicine_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        expiry_date TEXT NOT NULL,
        price REAL NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Prescriptions (
        prescription_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER NOT NULL,
        prescription_date TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
    );

    CREATE TABLE IF NOT EXISTS Prescription_Items (
        prescription_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        prescription_id INTEGER NOT NULL,
        medicine_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        dosage TEXT NOT NULL,
        FOREIGN KEY (prescription_id) REFERENCES Prescriptions(prescription_id) ON DELETE CASCADE,
        FOREIGN KEY (medicine_id) REFERENCES Medicines(medicine_id)
    );

    CREATE TABLE IF NOT EXISTS Bills (
        bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
        prescription_id INTEGER NOT NULL UNIQUE,
        subtotal REAL NOT NULL,
        tax REAL NOT NULL,
        discount REAL NOT NULL,
        total REAL NOT NULL,
        FOREIGN KEY (prescription_id) REFERENCES Prescriptions(prescription_id) ON DELETE CASCADE
    );
    """)

    load_path = os.path.join(SQL_DIR, "load_data.sql")
    if os.path.exists(load_path):
        with open(load_path, "r", encoding="utf-8") as f:
            sql = f.read()
        sql = re.sub(r"USE\s+\w+;", "", sql, flags=re.I)
        try:
            cur.executescript(sql)
        except Exception:
            for line in sql.splitlines():
                line = line.strip()
                if line.upper().startswith("INSERT INTO") and line.endswith(";"):
                    try:
                        cur.execute(line)
                    except Exception:
                        pass

    conn.commit()
    cur.close()
    conn.close()



    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Exception:
        _init_sqlite_db()
        conn = sqlite3.connect(SQLITE_DB, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return SQLiteConnectionWrapper(conn)
    
    
