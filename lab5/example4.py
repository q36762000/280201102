password = "asd125"
pasw = input("enter password: ")
help = "help"

if pasw == help:
  print(password[0])
else:
  while password != pasw:
    pasw = input("enter password: ")
  print("Welcome")