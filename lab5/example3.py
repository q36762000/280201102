x1 = int(input("enter an integer: "))
x2 = int(input("enter an integer: "))
matching_digits = 0

for a in list(str(x1)):
  for b in set(str(x2)):
    if a == b:
      matching_digits += 1

print(matching_digits)
