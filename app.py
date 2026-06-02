from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from models import db, AttendanceSession, AttendanceRecord

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# ---------------- STUDENTS ----------------

students = [
    # Paste your complete 70-student list here
    "1. ABHAY M A","2. ABHIJITH M S","3. ABINAND E G","4. ABINAND P","5. ADARSH P",
    "6. ADITHYAN S","7. AFRA SHERIN K","8. AJENYA K","9. AJMAL REHMAN A","10. AKHILESH G",
    "11. AKSHAY KRISHNA K","12. AKSHOBH S","13. AMALJITH HARI N","14. AMARJITH HARAN N",
    "15. AMRITHAGIRI P S","16. ANJANADAS P K","17. ANSHIJA A","18. ANUPAMA S","19. APARNA P S",
    "20. ARUN S","21. ARYA KRISHNA","22. ASHISH K P","23. ASHISH P","24. ATHUL P",
    "25. AVANI C S","26. CHARUTHA A H","27. FARSANA V K","28. HAFIS MOHAMMED O K",
    "29. HANAN O K","30. INDRAPRASAD K","31. IVIN G THOLATH","32. JISHNU J NAIR",
    "33. JOJITH P","34. K P MANU KRISHNA","35. MAHITHA PRADOSH",
    "36. MOHAMMED AMEEN Y","37. MOHAMMED SAJAD S","38. MOHAMMED YASIR S",
    "39. MUHAMMED RISHAL M C","40. MUHAMMED BASITH M","41. MUHAMMED RAEES P J",
    "42. MUHAMMED SHAMIL K P","43. MUHAMMED SHANU P","44. MUHAMMED SIRAJ V",
    "45. MUHAMMED SWALIH C","46. NANDAKUMAR K P","47. N ARCHANA",
    "48. NAVANEETH KRISHNAN A","49. NAVEEN P","50. P P ANOOP","51. RAHUL R",
    "52. RATNA K P","53. ROHITH BABU C","54. RUBIN RAJ C",
    "55. SABIQUE SHAMEEM N","56. SAI KIRAN V","57. SAJIN T S","58. SARATH S",
    "59. SONA R KISHAN","60. SREELAKSHMI S","61. SREESANTH M","62. SRUTHY S",
    "63. SUBEESH KRISHNA O K","64. SURJITH H","65. VAISAKH T U",
    "66. VARSHA P","67. VYSAKH B","68. YADHU KRISHNAN A","69. GOKUL" , "70. HARISUDAN"

]

# ---------------- TEACHER ----------------

teachers = {
    "Unknown":"Renjusha Miss",
    "Unknown":"Aiswarya Miss",
    "Unknown":"Nimisha Miss",
    "Digital electronics and computer architecture": "Rajitha Miss",
    "Unknown":"Sruthy Miss"
}

# ---------------- TIMETABLE ----------------

timetable = {
    "Monday":["1st","2nd","3rd","4th","5th","6th"],
    "Tuesday":["1st","2nd","3rd","4th","5th","6th"],
    "Wednesday":["1st","2nd","3rd","4th","5th","6th"],
    "Thursday":["1st","2nd","3rd","4th","5th","6th"],
    "Friday":["1st","2nd","3rd","4th","5th","6th"]
}

# ---------------- TIME SLOTS ----------------

slots_mon_thu = [
    ("09:30","10:20"),
    ("10:20","11:10"),
    ("11:20","12:10"),
    ("12:10","13:00"),
    ("13:40","14:30"),
    ("14:40","15:30")
]

slots_fri = [
    ("09:30","10:15"),
    ("10:15","11:00"),
    ("11:10","11:50"),
    ("11:50","12:30"),
    ("14:00","14:45"),
    ("14:45","15:30")
]

# ---------------- CLASS DETECTION ----------------

def detect_class():

    now = datetime.now()

    day = now.strftime("%A")

    current_time = now.time()

    slots = slots_fri if day == "Friday" else slots_mon_thu

    if day not in timetable:
        return "Special Class", None, None

    for i, (start, end) in enumerate(slots):

        start_time = datetime.strptime(start,"%H:%M").time()
        end_time = datetime.strptime(end,"%H:%M").time()

        if start_time <= current_time <= end_time:

            subject = timetable[day][i]

            teacher = teachers[subject]

            return f"Hour {i+1}", subject, teacher

    return "Special Class", None, None

# ---------------- HOME ----------------

@app.route("/")
def home():

    hour, subject, teacher = detect_class()

    return render_template(
        "index.html",
        students=students,
        hour=hour,
        subject=subject,
        teacher=teacher
    )

# ---------------- SAVE ATTENDANCE ----------------

@app.route("/save", methods=["POST"])
def save_attendance():

    hour, subject, teacher = detect_class()

    now = datetime.now()

    session = AttendanceSession(
        date=now.strftime("%d-%m-%Y"),
        hour=hour,
        subject=subject,
        teacher=teacher,
        created_at=now.strftime("%d-%m-%Y %I:%M %p")
    )

    db.session.add(session)
    db.session.commit()

    present_students = request.form.getlist("present")
    late_students = request.form.getlist("late")

    for student in students:

        if student in present_students:

            record = AttendanceRecord(
                session_id=session.id,
                student_name=student,
                status="Present",
                late_time=""
            )

        elif student in late_students:

            record = AttendanceRecord(
                session_id=session.id,
                student_name=student,
                status="Late",
                late_time=datetime.now().strftime("%I:%M %p")
            )

        else:

            record = AttendanceRecord(
                session_id=session.id,
                student_name=student,
                status="Absent",
                late_time=""
            )

        db.session.add(record)

    db.session.commit()

    return redirect(
        url_for(
            "attendance_view",
            id=session.id
        )
    )

# ---------------- HISTORY ----------------

@app.route("/history")
def history():

    sessions = AttendanceSession.query.order_by(
        AttendanceSession.id.desc()
    ).all()

    return render_template(
        "history.html",
        sessions=sessions
    )

# ---------------- VIEW ATTENDANCE ----------------

@app.route("/attendance/<int:id>")
def attendance_view(id):

    session = AttendanceSession.query.get_or_404(id)

    records = AttendanceRecord.query.filter_by(
        session_id=id
    ).all()

    return render_template(
        "view_attendance.html",
        session=session,
        records=records
    )

if __name__ == "__main__":
    app.run(debug=True)