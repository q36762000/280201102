def pass_level(password):
  level = 0
  if len(password) < 8 or " " in password:
    level = 0
    return level
  alphabetic = False
  numeric = False
  special = False
  level = 1
  for i in password:
    if i.upper() != i or i.lower() != i:
      alphabetic = True
      if numeric == True or special == True:
        level += 1
        numeric = False
        special = False
    elif i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      numeric = True
      if alphabetic == True or special == True:
        level += 1
        alphabetic = False
        special = False
    else:
      special = True
      if alphabetic == True or numeric == True:
        level += 1
        alphabetic = False
        numeric = False
  return level
def main():
  password = str(input("password:"))
  print("security level:", pass_level(password))

main()