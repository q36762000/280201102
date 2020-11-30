n = int(input("identity matrix: "))
value = 0
for i in range(n):
  list_value = ""
  for a in range(n):
    if i == a:
      value = 1
    list_value += str(value) + " " 
    value = 0
  print(list_value)