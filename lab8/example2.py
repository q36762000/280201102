def is_prime(num):
  count = 0
  for k in range(1, num+1):
    if num % k == 0:
      count += 1
  if count == 2:
    prime = True
  else:
    prime = False
  return prime
def print_primes_between(num1,num2):
  list = []
  if num1 > num2:
    a = num1
    num1 = num2
    num2 = a
  for k in range(num1, num2+1):
    if is_prime(k):
      list.append(k)
  return print(list)
print_primes_between(5,17)