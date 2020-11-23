nums = int(input("how many fibonacci numbers: "))
a1 = 1
a2 = 1
while nums < 2:
  nums = int(input("enter a number: "))
if nums >= 2:
  list_fib = [a1, a2]
  for i in range(3, nums+1):
    a3 = a1 + a2
    list_fib.append(a3)    
    a1 = a2
    a2 = a3
print(list_fib)