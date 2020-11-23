students = int(input("number of studens: "))
list1 = []
grade = []

for i in range(students):
  print("Student", i+1,": ")
  midterm1 = int(input("midterm 1 of student: "))
  midterm2 = int(input("midterm 2 of student: "))
  final = int(input("final exam of student: "))
  print("")
  list_grades = [midterm1, midterm2, final]
  list1.append(list_grades)
  average_grade = list1[i][0]*30/100+list1[i][1]*30/100+list1[i][2]*40/100
  if average_grade > 90:
    grade.append(average_grade)

print(grade)