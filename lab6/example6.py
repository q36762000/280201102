n = int(input("number: "))
sum = 0
for a in range(n):
  for b in range(n):
    x = int(input(str(a+1)+ " x "+ str(b+1)+ ": "))
    if a == b:
      sum += x
print(sum)