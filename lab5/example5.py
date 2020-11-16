nums = int(input("how many fibonacci numbers: "))
a1 = 1
a2 = 1
a3 = 0
while nums <= 0:
  nums = int(input("enter a valid number: "))
if nums == 1:
  list_fib = [a1]
elif nums == 2:
  list_fib = [a1, a2]
elif nums > 2:
  list_fib = [a1, a2]
  for i in range(3, nums+1):
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    list_fib.append(a3)
print(list_fib)
