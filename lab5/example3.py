x1 = int(input("enter an integer: "))
x2 = int(input("enter an integer: "))
matching_digits = 0

while x1 > 0 and x2 > 0:
  if x1 % 10 == x2 % 10:
    matching_digits += 1
  x1 = x1 // 10
  x2 = x2 // 10
print(matching_digits)