import json
import os


def load_data(file_path: str):
    """
    Load JSON data from file and convert each value list into a set.

    :param file_path: Path of the JSON file to load.
    :return: Dictionary with keys mapping to sets.
    """
    loaded_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for key, value in data.items():
        loaded_dict[key] = set(value)

    return loaded_dict


verify = input("Do you want to work with preloaded data? [y/n] ").casefold()

courses_dict = load_data(r"College_Data\college_course.json")
students_dict = load_data(r"College_Data\student_details.json")

course_abbr = {
    "CS101": "Intro to Computer Science",
    "CS202": "Advanced Computer Science",
    "MATH201": "Calculus II",
    "PHYS150": "General Physics I",
    "ENG202": "English Literature",
    "BIO105": "Biology Basics",
    "HIST300": "World History",
    "CHEM110": "General Chemistry",
    "PSY250": "Introduction to Psychology",
    "ART180": "Fundamentals of Art",
}

if verify == 'n':
    for key in courses_dict:
        courses_dict[key] = set()

    for key in students_dict:
        students_dict[key] = set()


def get_integer(prompt: str) -> int:
    """
    Prompt user for numeric input until a valid integer is provided.
    """
    while True:
        value = input(prompt)
        if value.isnumeric():
            return int(value)
        print("Please enter a valid number.")


def get_input(variable: str) -> str:
    """
    Get a course or student name from the user,
    automatically formatting it based on its type.

    :param variable: 'course' or 'student'
    """
    user_value = input(f"Enter {variable}: ")

    if "course" in variable.lower():
        return user_value.upper()
    elif "student" in variable.lower():
        return user_value.casefold()

    return user_value


def input_choice():
    """
    Get a numeric choice from the user (used in menus).
    """
    return get_integer("Choose an option: ")


def choice_list(variable: str):
    """
    Present either student list or course list and return the chosen one.

    :param variable: 'course' or 'student'
    """
    if variable == "course":
        index_map = {
            i + 1: course
            for i, course in enumerate(courses_dict)
        }

        for idx, course in index_map.items():
            print(f"{idx}: {course}")

        chosen = input_choice()
        return index_map.get(chosen)

    elif variable == "student":
        index_map = {
            i + 1: student
            for i, student in enumerate(students_dict)
        }

        for idx, student in index_map.items():
            print(f"{idx}: {student}")

        chosen = input_choice()
        return index_map.get(chosen)

    return None


def dump_data(path: str, data: dict):
    """
    Save a dictionary of sets into JSON format.

    :param path: File name to save.
    :param data: Dictionary with sets as values.
    """
    os.makedirs("College_Data", exist_ok=True)

    final_path = os.path.join("College_Data", path)

    serializable = {key: list(values) for key, values in data.items()}

    with open(final_path, 'w', encoding='utf-8') as f:
        json.dump(serializable, f, indent=2)
