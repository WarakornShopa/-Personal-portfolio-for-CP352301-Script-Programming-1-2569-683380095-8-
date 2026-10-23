#-----Lab 5.2 - Course Enrollment & Collaboration (Set Focus)-----

python_students = {"S001", "S003", "S005", "S007", "S009"}
java_students = {"S002", "S003", "S006", "S007", "S010"}

print(f"Python Students: {python_students}")
print(f"Java Students:   {java_students}\n")

both_courses = python_students.intersection(java_students)
print(f"Students in Both Courses: {both_courses}")

all_unique_students = python_students.union(java_students)
print(f"All Unique Students: {all_unique_students}")

only_python = python_students.difference(java_students)
print(f"Students Only in Python: {only_python}")

exclusive_students = python_students.symmetric_difference(java_students)
print(f"Students in Only One Course: {exclusive_students}\n")

all_students_list = ["S001", "S003", "S005", "S001", "S002"]
print(f"Original List (with duplicates): {all_students_list}")

unique_students_list = list(set(all_students_list))
print(f"Unique List (after removing duplicates): {unique_students_list}")