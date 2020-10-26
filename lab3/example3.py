gpa = input("What is your gpa? :")
num_lectures = int(input("Number of your lectures? :"))
gpa = float(gpa)

if gpa < 2.0 and num_lectures < 47:
  print("Not enough number of lectures and GPA")
elif gpa < 2.0 and num_lectures >= 47:
  print("Not enough GPA!")
elif gpa >= 2.0 and num_lectures < 47:
  print("Not enough number of lectures!")
else:
  print("GRADUATED!!!")