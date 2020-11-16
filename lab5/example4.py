static_password = "abc123"
password = input("enter password: ")
x = "help"

while password != static_password:
  if password == x:
    print(static_password[0])
  else:
    print("Wrong")
  password = input("enter password: ")
print("Welcome")