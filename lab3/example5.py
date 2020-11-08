month = str(input("Enter month: "))
day = int(input("Enter day: "))

if month == "january" or month == "february" or month == "december" and day >= 21 or month == "march" and day < 20:
  print("You are in winter season.")
elif month == "march" and day >= 20 or month == "april" or month == "may" or month == "june" and day < 21:
  print("You are in spring season.")
elif month == "june" and day >=21 or month == "july" or month == "august" or month == "september" and day < 22:
  print("You are in summer season.")
elif month == "september" and day >= 22 or month == "october" or month == "november" or month == "december" and day < 21:
  print("You are in fall season.")