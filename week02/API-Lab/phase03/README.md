# Phase 03 - JSON & Python API Integration

## Task 11: Create a JSON Student Record

**JSON Object:**
```json
{
  "name": "Ali",
  "marks": 85,
  "program": "BSCS"
}
```

**Python Dictionary:**
```python
student = {
    "name": "Ali",
    "marks": 85,
    "program": "BSCS"
}

print(student["name"])      # Ali
print(student["marks"])     # 85
print(student["program"])   # BSCS
```

## Task 12: Work With a JSON Array

```python
students = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Sara"},
    {"id": 3, "name": "Ahmed"}
]

for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}")
```
