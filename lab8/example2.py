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
def print_primes_between(num1, num2):
  for k in range(num1, num2):
    if is_prime(k):
      print(k)
def main():
  num1 = int(input("begin:"))
  num2 = int(input("end:"))
  print_primes_between(num1, num2)

main()