"""
Create a function that takes an list of student dictionaries and returns a list of their top notes.
If student does not have notes then let's assume their top note is equal to 0.
Examples

get_student_top_notes() ➞ [5, 5, 4]
"""

students = [
  {
    "id": 1,
    "name": "Jacek",
    "notes": [5, 3, 4, 2, 5, 5]
  },
  {
    "id": 2,
    "name": "Ewa",
    "notes": [2, 3, 3, 3, 2, 5]
  },
  {
    "id": 3,
    "name": "Zygmunt",
    "notes": [2, 2, 4, 4, 3, 3]
  },
  # {
  #   "id": 4,
  #   "name": "Zygmunt",
  # },
  {
    "id": 3,
    "name": "Zygmunt",
    "notes": []
  }
]


def get_student_top_notes(students):
    top_notes = []
    for student in students:
        if student['notes']:
            top_notes.append(max(student['notes']))
        else:
            top_notes.append(0)

    return top_notes


def test_get_students_top_notes_one_student():
    return_value = get_student_top_notes(students)
    assert return_value == [5, 5, 4, 0]


def get_student_top_notes_one_line(students):
    return [max(i['notes']) if i['notes'] else 0 for i in students]