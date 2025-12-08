import random
from colorama import Fore
from useful_functions import *


def add_course():
    """Add a new course to the system."""
    course_code = get_input("course")
    courses_dict.setdefault(course_code, set())

    print(Fore.GREEN, "Course added successfully.", Fore.RESET)
    return courses_dict


def remove_course():
    """Remove an existing course and detach all related students."""
    course_code = choice_list("course")
    enrolled_students = courses_dict.get(course_code)

    if enrolled_students:
        for student in enrolled_students:
            students_dict[student].discard(course_code)

        courses_dict.pop(course_code, None)

    print(Fore.GREEN, "Course removed successfully.", Fore.RESET)
    return courses_dict


def enroll_existing_student():
    """Enroll an existing student into an additional course."""
    student_name = choice_list("student")
    course_code = choice_list("course")

    if not students_dict.setdefault(student_name):
        students_dict[student_name] = {course_code}
    elif student_name in courses_dict[course_code]:
        students_dict[student_name].add(course_code)

    courses_dict[course_code].add(student_name)
    return courses_dict, students_dict


def enroll_new_student():
    """Enroll a new student into a selected course."""
    student_name = get_input("student")
    course_code = choice_list("course")

    if course_code in courses_dict:
        if not students_dict.setdefault(student_name):
            students_dict[student_name] = {course_code}
        elif student_name in courses_dict[course_code]:
            students_dict[student_name].add(course_code)

        courses_dict[course_code].add(student_name)
        return courses_dict, students_dict

    return "=" * 30


def drop_student_from_course():
    """Remove a student's enrollment from a course."""
    student_name = get_input("student")
    course_code = choice_list("course")

    if student_name in courses_dict[course_code]:
        courses_dict[course_code].discard(student_name)
        students_dict[student_name].discard(course_code)
    else:
        print(f"{student_name} is not enrolled in this course.")

    return courses_dict, students_dict


def list_student_courses():
    """List all courses a specific student is enrolled in."""
    student_name = choice_list("student")

    if student_name in students_dict:
        print(f"Courses for {student_name}:")
        return students_dict[student_name]

    print(Fore.RED,
          f"The student '{student_name}' is not enrolled.\n"
          f"Please enroll the student first.",
          Fore.RESET)
    return "=" * 30


def list_all_courses():
    """Display all available courses with full names."""
    print("Available Courses in the College:")

    for code, name in course_abbr.items():
        print(f"{code}: {name}")

    return "=" * 30


def list_course_students():
    """List all students enrolled in a specific course."""
    course_code = choice_list("course")

    if course_code in courses_dict:
        print(f"Students enrolled in {course_code}:")
        return courses_dict[course_code]

    return "=" * 30


def generate_weekly_schedule():
    """Generate a weekly schedule with 9 periods/day for all courses."""
    weekly_schedule = {
        "monday": [], "tuesday": [], "wednesday": [],
        "thursday": [], "friday": []
    }

    course_keys = set(courses_dict.keys())

    for day, periods in weekly_schedule.items():
        while len(periods) < 9:
            existing = set(periods)
            available = course_keys.symmetric_difference(existing)

            if available:
                periods.append(available.pop())
            else:
                periods.append(random.choice(list(course_keys)))

    return weekly_schedule


schedule = generate_weekly_schedule()


def student_weekly_schedule():
    """Generate a weekly timetable for a specific student."""
    student_courses = list_student_courses()

    if student_courses == "=" * 30:
        return "=" * 30

    timetable = {}

    for day, periods in schedule.items():
        free_or_course = [
            "FREE" if (period not in student_courses) else period
            for period in periods
        ]
        timetable[day] = free_or_course

    return timetable


functions_drop = {
    "Add course": add_course,
    "Remove course": remove_course,
    "Enroll new student": enroll_new_student,
    "Enroll existing student": enroll_existing_student,
    "Drop student from course": drop_student_from_course,
    "Available courses": list_all_courses,
    "Student's courses": list_student_courses,
    "Students in a course": list_course_students,
    "Weekly schedule": generate_weekly_schedule,
    "Student weekly schedule": student_weekly_schedule,
}
