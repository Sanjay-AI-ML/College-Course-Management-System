"""Data persistence module for College Course Management System."""

import json
import os
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).resolve().parent / "data"
COURSES_FILE = DATA_DIR / "courses.json"
STUDENTS_FILE = DATA_DIR / "students.json"


def ensure_data_dir():
    """Create data directory if it doesn't exist."""
    DATA_DIR.mkdir(exist_ok=True)


def save_courses(courses_data):
    """Save courses to JSON file."""
    ensure_data_dir()
    try:
        with open(COURSES_FILE, 'w') as f:
            json.dump(courses_data, f, indent=2)
        print(f"✓ Saved {len(courses_data)} courses to {COURSES_FILE}")
        return True
    except Exception as e:
        print(f"✗ Error saving courses: {e}")
        return False


def load_courses():
    """Load courses from JSON file."""
    ensure_data_dir()
    try:
        if COURSES_FILE.exists():
            with open(COURSES_FILE, 'r') as f:
                data = json.load(f)
            print(f"✓ Loaded {len(data)} courses from {COURSES_FILE}")
            return data
        else:
            print(f"No course file found, starting fresh")
            return []
    except Exception as e:
        print(f"✗ Error loading courses: {e}")
        return []


def save_students(students_data):
    """Save students to JSON file."""
    ensure_data_dir()
    try:
        with open(STUDENTS_FILE, 'w') as f:
            json.dump(students_data, f, indent=2)
        print(f"✓ Saved {len(students_data)} students to {STUDENTS_FILE}")
        return True
    except Exception as e:
        print(f"✗ Error saving students: {e}")
        return False


def load_students():
    """Load students from JSON file."""
    ensure_data_dir()
    try:
        if STUDENTS_FILE.exists():
            with open(STUDENTS_FILE, 'r') as f:
                data = json.load(f)
            print(f"✓ Loaded {len(data)} students from {STUDENTS_FILE}")
            return data
        else:
            print(f"No student file found, starting fresh")
            return []
    except Exception as e:
        print(f"✗ Error loading students: {e}")
        return []


def create_backup():
    """Create timestamped backup of all data."""
    ensure_data_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = DATA_DIR / f"backup_{timestamp}"
    
    try:
        backup_dir.mkdir(exist_ok=True)
        
        if COURSES_FILE.exists():
            with open(COURSES_FILE, 'r') as src:
                backup_courses = backup_dir / "courses.json"
                with open(backup_courses, 'w') as dst:
                    dst.write(src.read())
        
        if STUDENTS_FILE.exists():
            with open(STUDENTS_FILE, 'r') as src:
                backup_students = backup_dir / "students.json"
                with open(backup_students, 'w') as dst:
                    dst.write(src.read())
        
        print(f"✓ Backup created: {backup_dir}")
        return backup_dir
    except Exception as e:
        print(f"✗ Error creating backup: {e}")
        return None


class Validator:
    """Input validation for course and student data."""
    
    @staticmethod
    def validate_course(course_id, name, credits, semester, max_students):
        """Validate course data."""
        errors = []
        
        if not course_id or not isinstance(course_id, str):
            errors.append("Course ID is required and must be a string")
        elif len(course_id) < 2:
            errors.append("Course ID must be at least 2 characters")
        
        if not name or not isinstance(name, str):
            errors.append("Course name is required")
        elif len(name) < 3:
            errors.append("Course name must be at least 3 characters")
        
        if not isinstance(credits, int) or credits <= 0 or credits > 10:
            errors.append("Credits must be between 1 and 10")
        
        if not isinstance(semester, int) or semester < 1 or semester > 8:
            errors.append("Semester must be between 1 and 8")
        
        if not isinstance(max_students, int) or max_students <= 0:
            errors.append("Max students must be a positive integer")
        
        return errors
    
    @staticmethod
    def validate_student(student_id, name, email=None):
        """Validate student data."""
        errors = []
        
        if not student_id or not isinstance(student_id, str):
            errors.append("Student ID is required")
        elif len(student_id) < 2:
            errors.append("Student ID must be at least 2 characters")
        
        if not name or not isinstance(name, str):
            errors.append("Student name is required")
        elif len(name) < 2:
            errors.append("Student name must be at least 2 characters")
        
        if email and "@" not in email:
            errors.append("Invalid email format")
        
        return errors
    
    @staticmethod
    def validate_enrollment(student_id, course_id):
        """Validate enrollment data."""
        errors = []
        
        if not student_id or not isinstance(student_id, str):
            errors.append("Valid student ID required")
        
        if not course_id or not isinstance(course_id, str):
            errors.append("Valid course ID required")
        
        return errors
