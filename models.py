from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AttendanceSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.String(30))
    hour = db.Column(db.String(30))
    subject = db.Column(db.String(100))
    teacher = db.Column(db.String(100))

    created_at = db.Column(db.String(50))

class AttendanceRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    session_id = db.Column(db.Integer)

    student_name = db.Column(db.String(200))

    status = db.Column(db.String(20))
    late_time = db.Column(db.String(20))
