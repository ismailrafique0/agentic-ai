class Student:
    def __init__(self, id, name, program, semester, marks, grade=""):
        self.id = id
        self.name = name
        self.program = program
        self.semester = semester
        self.marks = marks
        self.grade = grade

    def get_details(self):
        return {
            "id": self.id,
            "name": self.name,
            "program": self.program,
            "semester": self.semester,
            "marks": self.marks,
            "grade": self.grade,
        }