age = int(input("Enter your age: "))
bus_ticket = 3

if age < 6 or age > 60:
  print("Your ticket price is free.")
elif age >=6 and age < 18:
  print("Your ticket price is",bus_ticket*0.5)
else:
  print("Your ticket price is",bus_ticket)