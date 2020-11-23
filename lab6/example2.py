students = int(input("number of studens:"))
list1 = []

for i in range(students):
  midterm1 = int(input("midterm 1 of student: "))
  midterm2 = int(input("midterm 2 of student: "))
  final = int(input("final exam of student: "))
  list_grades = [midterm1, midterm2, final]
  list1.append(list_grades)
print(list1)