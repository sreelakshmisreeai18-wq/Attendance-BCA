Create a modern, professional, and fully responsive College Attendance Management Website with a clean dashboard, timetable management, attendance marking system, attendance history, reporting features, and permanent database storage.

## Primary Objective

The system should allow teachers to quickly mark attendance for each class period while maintaining accurate records and preventing duplicate student classifications.

---

## Student Attendance Categories

Each student can belong to ONLY ONE category at a time:

### Present

* Student attended the class normally.

### Late Comer

* Student attended the class late.
* Late arrival time must be automatically recorded.
* Display the recorded time beside the student's name.

### Absent

* Student did not attend the class.

### Strict Validation Rules

A student cannot appear in more than one category.

Examples:

* If a student is marked Present, they must NOT appear in Late Comers or Absentees.
* If a student is marked Late Comer, they must NOT appear in Present or Absentees.
* If a student is marked Absent, they must NOT appear in Present or Late Comers.

The system must automatically prevent duplicate classification and move the student from the previous category when reassigned.

---

## Attendance Marking Interface

Display:

* Roll Number
* Student Name
* Search Box
* Quick Filters

Provide action buttons:

* Mark Present
* Mark Late
* Mark Absent

The interface should support fast attendance marking for large classrooms.

Late Comers must automatically receive a timestamp.

Display live counters:

* Present Count
* Late Count
* Absent Count
* Total Students

---

## Date, Day & Session Information

Automatically display:

* Current Date
* Current Day
* Current Time

Allow manual selection when required.

Every attendance session must store:

* Date
* Day
* Subject
* Faculty Name
* Period / Hour
* Timestamp

---

## Timetable Management

Create a timetable module.

For each day:

* Monday
* Tuesday
* Wednesday
* Thursday
* Friday

Store:

* Period Number
* Subject
* Faculty Name
* Start Time
* End Time

During attendance marking:

* User selects Period.
* Subject and Faculty should automatically populate from the timetable.
* Current class can be automatically detected from the timetable and current time.

---

## Attendance Summary

After saving attendance, generate:

* Total Students
* Present Students
* Late Comers
* Absentees
* Attendance Percentage

Display summary using dashboard cards.

---

## Attendance History Module

Create a dedicated History page.

Every attendance session must be stored permanently.

History records must display:

* Date
* Day
* Subject
* Faculty
* Period
* Total Students
* Present Count
* Late Count
* Absent Count
* Attendance Percentage

Example:

Date: 01-01-2026
Day: Thursday
Subject: Python Programming
Period: 2nd Hour

Present: 58
Late: 3
Absent: 7

View Details

---

## Detailed History View

When a history record is opened, display:

### Present Students

* Roll Number
* Name

### Late Comers

* Roll Number
* Name
* Late Arrival Time

### Absentees

* Roll Number
* Name

The detailed view should exactly reproduce the attendance that was saved for that session.

---

## Attendance Editing Feature

Provide full editing functionality.

Teachers should be able to:

* Edit attendance after saving.
* Change student status.
* Move student between Present, Late, and Absent.
* Update late arrival time.
* Add missing students.
* Remove incorrectly marked students.

After editing:

* Attendance statistics must automatically recalculate.
* History records must update immediately.

---

## Attendance Record Management

Provide options to:

* View Attendance
* Edit Attendance
* Duplicate Attendance
* Delete Attendance

Before deletion:

* Show confirmation dialog.

---

## Duplicate Prevention

Prevent duplicate attendance sessions.

The system must not allow multiple attendance records for:

* Same Date
* Same Subject
* Same Period

Provide warning if a duplicate entry is attempted.

---

## Search & Filter

History should support:

* Search by Date
* Search by Day
* Search by Subject
* Search by Faculty
* Search by Student Name
* Search by Roll Number

Filters:

* Daily
* Weekly
* Monthly
* Custom Date Range

---

## Reports

Generate:

* Daily Report
* Weekly Report
* Monthly Report
* Subject-wise Report
* Faculty-wise Report
* Student-wise Attendance Report

Export formats:

* PDF
* Excel
* CSV

---

## Dashboard

Display:

* Total Students
* Total Attendance Sessions
* Average Attendance Percentage
* Today's Attendance Status
* Today's Present Count
* Today's Late Count
* Today's Absent Count

Recent Attendance Records Table

Attendance Trend Graphs

Subject-wise Statistics

Monthly Analytics

---

## User Interface Requirements

Design Style:

* Modern College ERP Style
* Professional Dashboard
* Responsive Design
* Mobile Friendly
* Sidebar Navigation
* Top Navigation Bar
* Attractive Cards
* Searchable Tables
* Smooth Animations
* Blue and White Academic Theme
* Clean Typography
* Modern Modal Dialogs

---

## Database Requirements

Store permanently:

* Student Information
* Timetable
* Attendance Records
* Attendance History
* Late Arrival Times
* Attendance Statistics

No attendance data should be lost after logout or refresh.

---

## Additional Features

* Auto-save draft attendance.
* Confirmation before final submission.
* Undo recent changes.
* Bulk attendance actions.
* Attendance percentage calculation.
* Student attendance analytics.
* Faculty attendance analytics.
* Secure authentication and authorization.
* Audit log showing who created, edited, or deleted attendance records and when.

The final website should look like a professional college attendance portal with fast attendance marking, timetable integration, permanent attendance history, powerful editing capabilities, detailed reports, and strict validation ensuring that a student can belong to only one attendance category (Present, Late, or Absent) at any given time.
## Timetable Configuration

The timetable structure will be provided later by the user.

The system must be designed in a way that allows the administrator to easily add, edit, replace, or import the timetable at any time without modifying the source code.

The timetable module should support:

* Day-wise timetable management
* Multiple periods/hours per day
* Subject assignment
* Faculty assignment
* Start and end times for each period
* Future timetable modifications

The exact timetable data, subjects, faculty names, period timings, and class schedule will be provided later and should be configurable through the application interface.

Until the timetable is provided, use sample placeholder data for development and testing purposes.

The attendance system should automatically use the configured timetable once it is added, without requiring any code changes.

The website architecture must be flexible enough to accommodate timetable updates, subject changes, faculty changes, period changes, and academic year changes in the future.

## Student and Class Management Flexibility

The system must support student modifications at any time.

Administrators should be able to:

* Add new students
* Edit student details
* Remove students
* Transfer students between classes or sections
* Update student course selections
* Manage student enrollment changes during the academic year

All attendance records should remain intact even after student information is updated.

## SEC (Skill Enhancement Course) Support

The system must support special subjects such as **SEC**, where students can choose different SEC courses based on their preferences.

Requirements:

* Students are not restricted to a single classroom during SEC periods.
* Each student can be assigned to a different SEC course.
* Multiple SEC classes may run simultaneously during the same period.
* Attendance must be taken separately for each SEC class.
* Teachers should only see and mark attendance for students enrolled in their assigned SEC course.
* Students should automatically appear in the attendance list of their selected SEC course.
* A student must not appear in multiple SEC attendance lists for the same period.
* SEC course enrollment should be editable by administrators.

Example:

During Period 4:

* SEC Course A → Classroom A → Faculty A
* SEC Course B → Classroom B → Faculty B
* SEC Course C → Classroom C → Faculty C

Students enrolled in SEC Course A should only appear in Course A attendance.
Students enrolled in SEC Course B should only appear in Course B attendance.
Students enrolled in SEC Course C should only appear in Course C attendance.

## Dynamic Attendance Lists

Attendance lists should not be permanently fixed.

The system must dynamically generate attendance lists based on:

* Subject
* Course selection
* Section
* Class assignment
* Timetable configuration

This ensures that attendance can be taken simultaneously across multiple classes, electives, SEC courses, and special subject groups without manual student filtering.

## Future Scalability

The system should be designed to support:

* Elective subjects
* SEC courses
* Open electives
* Multiple departments
* Multiple sections
* Cross-department courses
* Semester-wise enrollment changes
* Academic year transitions

The architecture should remain flexible so that future timetable, enrollment, and course allocation changes can be handled without requiring major redesign or code modifications.
