# College Course Management System

![Python](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white) ![JSON](https://img.shields.io/badge/storage-json-blue) ![Validation](https://img.shields.io/badge/validation-strict-green) ![Backup](https://img.shields.io/badge/backup-auto-green)

A simple and interactive Python-based College Course Management System for managing courses, student enrollments, and weekly schedules. The system is fully menu-driven.

---

## 🚀 Features

### Core Functionality
- ✅ **Course Management** — Add or remove courses
- ✅ **Student Enrollment** — Enroll new or existing students
- ✅ **Course Dropping** — Drop students from courses
- ✅ **Inquiry System** — View student courses or course-wise student lists
- ✅ **Schedule Generation** — Auto-generate weekly schedule (Mon–Fri, 9 periods/day)
- ✅ **Personalized Timetables** — Generate student-specific schedules
- ✅ **Data Persistence** — Save and load data using JSON files

### User Experience
- Menu-driven CLI interface (no GUI required)
- Color-coded terminal output (optional, via Colorama)
- Interactive prompts with validation
- Data saved automatically

---

## 📋 Quick Start

### Requirements
- Python 3.7+
- No external dependencies (built-in libraries only)
- Optional: `colorama` for colored output

### Installation & Run

```bash
git clone https://github.com/Sanjay-AI-ML/College-Course-Management-System.git
cd College-Course-Management-System

# Run the program
python main.py
```

### Workflow
1. **Start** — Choose whether to load pre-existing data or start fresh
2. **Manage** — Use the menu to add courses, enroll students, or modify schedules
3. **Generate** — Create weekly schedules or student-specific timetables
4. **Save** — Data is saved to JSON files in `College_Data/`
5. **Exit** — Close the program (data persists)

---

## 📁 Project Structure

```
College-Course-Management-System/
├── main.py                      # Entry point — menu loop and user interactions
├── interface_functions.py       # UI functions for course/student management
├── useful_functions.py          # Helper functions for schedule generation, data handling
├── requirements.txt             # Python dependencies (optional)
└── College_Data/
    ├── college_course.json      # Stores course information
    ├── student_details.json     # Stores enrolled students
    └── weekly_schedule.json     # Stores auto-generated timetables
```

---

## 🛠️ Technologies Used

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.7+ |
| **Persistence** | JSON files (zero-database setup) |
| **Output** | Colorama (optional, for colored terminal) |
| **Architecture** | Modular: main → interface_functions → useful_functions |

---

## 📊 Data Structure

### Courses (`college_course.json`)
```json
{
  "courses": [
    {
      "course_id": "CS101",
      "course_name": "Data Structures",
      "credits": 3,
      "semester": 2,
      "max_students": 60,
      "enrolled": 45
    }
  ]
}
```

### Students (`student_details.json`)
```json
{
  "students": [
    {
      "student_id": "A001",
      "student_name": "Alice Sharma",
      "courses": ["CS101", "MATH102"]
    }
  ]
}
```

### Weekly Schedule (`weekly_schedule.json`)
```json
{
  "weekly_schedule": {
    "Monday": [
      {"period": 1, "course": "CS101", "time": "09:00-10:00"},
      {"period": 2, "course": "MATH102", "time": "10:00-11:00"}
    ]
  }
}
```

---

## 🎮 Usage Examples

### Add a Course
```
Menu → 1. Add Course
Enter Course ID: CS201
Enter Course Name: Algorithms
Enter Credits: 3
Enter Semester: 3
Enter Max Students: 70
```

### Enroll a Student
```
Menu → 2. Enroll Student
Enter Student ID: A001
Enter Student Name: Alice Sharma
Select courses to enroll:
  1. CS101
  2. MATH102
  [Selection saved]
```

### View Student's Courses
```
Menu → 4. View Student Courses
Enter Student ID: A001
→ Courses: CS101 (Data Structures), MATH102 (Calculus)
```

### Generate Weekly Schedule
```
Menu → 6. Generate Schedule
[Auto-generates 5-day schedule with 9 periods/day]
[Saves to weekly_schedule.json]
```

### View Student Timetable
```
Menu → 7. View Student Timetable
Enter Student ID: A001
[Shows personalized Monday–Friday schedule for that student]
```

---

## ✨ Key Code Components

### `interface.py` / `interface_functions.py`
- Handles all user menu interactions
- Validates input (course IDs, student names, etc.)
- Displays formatted tables and timetables

### `useful_functions.py`
- `generate_weekly_schedule()` — Creates the master weekly timetable
- `get_student_timetable()` — Filters schedule for a specific student
- `save_data()` / `load_data()` — JSON I/O operations
- Data validation and error handling

### `main.py`
- Entry point with infinite menu loop
- Orchestrates interface and utility functions
- Handles startup and shutdown (data save)

---

## 🔒 Data Persistence

All data is stored locally in JSON files within `College_Data/`:
- ✅ No database server required
- ✅ Easy to inspect and edit files manually
- ✅ Portable — just copy the folder
- ✅ Version control friendly (check `.gitignore` for data files if needed)

---

## 🐛 Troubleshooting

### "Module not found" error
```bash
pip install colorama
```

### Data not saving
- Ensure `College_Data/` directory exists (auto-created on first run)
- Check file permissions (read/write access needed)
- Verify JSON files are valid (manual edit may have broken them)

### Duplicate student enrollment
- The system checks for existing student IDs before enrollment
- If a student exists, you can add more courses instead of re-enrolling

---

## 🚀 Future Enhancements

- 🎯 **GUI Version** — Tkinter or PyQt frontend
- 🎯 **Database Integration** — Replace JSON with SQLite or PostgreSQL
- 🎯 **Teacher Assignment** — Assign instructors to courses
- 🎯 **Classroom Management** — Assign rooms and manage capacity
- 🎯 **Attendance Tracking** — Mark attendance and generate reports
- 🎯 **Grade Management** — Store and display student grades
- 🎯 **Fee/Payment Tracking** — Monitor tuition and fees
- 🎯 **Report Generation** — PDF export of timetables and transcripts
- 🎯 **Multi-user Roles** — Admin, teacher, student login levels

---

## 📝 License

MIT — See LICENSE file

---

## 👤 Author

Built by [@Sanjay-AI-ML](https://github.com/Sanjay-AI-ML)

Questions or feedback? Open an issue on GitHub!
