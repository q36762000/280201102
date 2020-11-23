students = int(input("number of studens:"))
list1 = []
grade = []

for i in range(students):
  midterm1 = int(input("midterm 1 of student: "))
  midterm2 = int(input("midterm 2 of student: "))
  final = int(input("final exam of student: "))
  list_grades = [midterm1, midterm2, final]
  list1.append(list_grades)

for i in range(students):
  average_grade = (list1[i][0]+list1[i][1]+list1[i][2])/3
  grade.append(average_grade)
print(grade)