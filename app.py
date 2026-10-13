
from flask import Flask, request, jsonify, send_from_directory
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_PATH = os.environ.get(
    "DATABASE_PATH",
    os.path.join(BASE_DIR, "data", "attendance.db")
)

os.makedirs(os.path.dirname(os.path.abspath(DATABASE_PATH)), exist_ok=True)


def get_db_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db_connection()
    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                attendance_date TEXT NOT NULL,
                course_id TEXT NOT NULL,
                status TEXT NOT NULL CHECK (status IN ('present', 'absent')),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        connection.commit()
    finally:
        connection.close()


init_db()


@app.route("/", methods=["GET"])
def home():
    return send_from_directory(
        os.path.join(BASE_DIR, "static"),
        "index.html"
    )


@app.route("/attendance", methods=["GET"])
def get_attendance():
    connection = get_db_connection()
    try:
        rows = connection.execute("""
            SELECT id, student_id, attendance_date, course_id, status
            FROM attendance
            ORDER BY id DESC
        """).fetchall()

        return jsonify({
            "success": True,
            "records": [dict(row) for row in rows]
        }), 200

    except sqlite3.Error:
        app.logger.exception("Failed to retrieve attendance records")
        return jsonify({
            "success": False,
            "message": "Could not retrieve attendance records."
        }), 500

    finally:
        connection.close()


@app.route("/attendance", methods=["POST"])
def save_attendance():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "success": False,
            "message": "Please send valid JSON data."
        }), 400

    student_id = str(data.get("student_id", "")).strip()
    attendance_date = str(data.get("attendance_date", "")).strip()
    course_id = str(data.get("course_id", "")).strip()
    status = str(data.get("status", "")).strip().lower()

    if not student_id or not attendance_date or not course_id:
        return jsonify({
            "success": False,
            "message": "Student ID, date, and course ID are required."
        }), 400

    if status not in ("present", "absent"):
        return jsonify({
            "success": False,
            "message": "Status must be present or absent."
        }), 400

    connection = get_db_connection()
    try:
        cursor = connection.execute("""
            INSERT INTO attendance (
                student_id, attendance_date, course_id, status
            )
            VALUES (?, ?, ?, ?)
        """, (student_id, attendance_date, course_id, status))

        connection.commit()

        return jsonify({
            "success": True,
            "message": "Attendance saved successfully!",
            "record": {
                "id": cursor.lastrowid,
                "student_id": student_id,
                "attendance_date": attendance_date,
                "course_id": course_id,
                "status": status
            }
        }), 201

    except sqlite3.Error:
        app.logger.exception("Failed to save attendance")
        return jsonify({
            "success": False,
            "message": "Could not save attendance."
        }), 500

    finally:
        connection.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
