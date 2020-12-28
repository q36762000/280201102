def mult(n):
  if n == 1:
    return 3
  else:
    return 3 + mult(n-1)
print(mult(5))