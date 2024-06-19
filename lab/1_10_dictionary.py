def get_student_details():

  name = input("Enter student name: ")
  roll_no = int(input("Enter roll number: "))
  total_mark = int(input("Enter total marks: "))
  return {"name": name, "roll_no": roll_no, "total_mark": total_mark}

def highest_score(students):
  highest_scorer = None
  for student in students.values():
    if highest_scorer is None or student["total_mark"] > highest_scorer["total_mark"]:
      highest_scorer = student
  return highest_scorer

def main():
  num_students = int(input("Enter the number of students: "))
  students = {}

  for i in range(num_students):
    print(f"\nEnter details for student {i+1}:")
    student_details = get_student_details()
    students[i+1] = student_details  # Use student ID (i+1) as key for uniqueness

  highest_scorer = highest_score(students)
  if highest_scorer:
    print("\nDetails of the student with the highest marks:")
    print(f"Name: {highest_scorer['name']}")
    print(f"Roll Number: {highest_scorer['roll_no']}")
    print(f"Total Marks: {highest_scorer['total_mark']}")
  else:
    print("No student data found.")

main()
