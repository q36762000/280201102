x1 = int(input("enter an integer: "))
x2 = int(input("enter an integer: "))
matching_digits = 0

while x1 > 0:
  if str(x1 % 10) in list(str(x2)):
    matching_digits += 1
  x1 = x1 // 10

print(matching_digits)
