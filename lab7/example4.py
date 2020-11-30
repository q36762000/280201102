password = input("enter a password:")
valid = True
if len(password) != 8:
  valid = False
if password.lower() == password:
  valid = False
if password.upper() == password:
  valid = False
count = 0
for i in range(10):
  if str(i) in password:
    count += 1
if count == 0:
  valid = False
if valid:
  print("Your password is valid.")
else:
  print("Your password is not valid.")