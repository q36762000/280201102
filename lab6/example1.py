e_mail = input("enter an email address: ")
e_mail = e_mail.lower()

a,b = e_mail.split("@")

a = a.replace(".", "")
e_mail = a+"@"+b

print(e_mail == "ceng113@example.com")