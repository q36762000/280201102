e_mail = input("enter an email adress: ")
e_mail1 = e_mail.lower()

a,b = e_mail1.split("@")

a = a.replace(".", "")
e_mail = a+"@"+b

print(e_mail == "ceng113@example.com")