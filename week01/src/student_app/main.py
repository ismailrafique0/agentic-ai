import json
import os
from src.student_app.config import APP_NAME, DEBUG, MAX_STUDENTS
from src.student_app.logger import logger
from src.student_app.models.student import Student
from src.student_app.services.calculator import calculate_grade
from src.student_app.utils.validation import validate_name, validate_marks
from src.student_app.reports.student_report import display_report

def load_student_data():
    json_path = os.path.join(os.path.dirname(__file__), "../../data/student.json")
    try:
        with open(json_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error("student.json file not found.")
        return None

def main():
    logger.info("Application started")
    print(f"Starting: {APP_NAME}")
    print(f"Debug Mode: {DEBUG}")
    print(f"Max Students Allowed: {MAX_STUDENTS}")
    print()

    data = load_student_data()
    if not data:
        print("Error: Could not load student data.")
        return

    name = data.get("name")
    marks = data.get("marks")

    if not validate_name(name):
        logger.warning("Invalid or empty student name in JSON record.")
        print("Error: Name cannot be empty.")
        return

    if not validate_marks(marks):
        logger.warning(f"Invalid marks in JSON record: {marks}")
        print("Error: Marks must be between 0 and 100.")
        return

    grade = calculate_grade(marks)
    student = Student(
        id=data.get("id"),
        name=name,
        program=data.get("program"),
        semester=data.get("semester"),
        marks=marks,
        grade=grade
    )

    display_report(student)
    logger.info("Application finished successfully.")

if __name__ == "__main__":
    main()