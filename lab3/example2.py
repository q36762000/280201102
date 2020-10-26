num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
num3 = int(input("Enter a number:"))

if num1 < num2 and num3:
  print(num1)
elif num2 < num1 and num3:
  print(num2)
else:
  print(num3)