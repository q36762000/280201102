num_of_ints = int(input("how many integers: "))
even = 0
odd = 0

for i in range(num_of_ints):
  x = int(input("enter an integer: "))
  if x % 2 == 0:
    even += 1
  else:
    odd += 1

percent = even / num_of_ints * 100
print(percent)