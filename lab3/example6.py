print("Write the parameters for represented quadratic equation : (ax**2 + b*x + c)")
a = float(input("Type a: "))
b = float(input("Type b: "))
c = float(input("Type c: "))

discriminant = b**2-(4*a*c)

x1 = (-b+discriminant**(1/2))/(2*a)
x2 = (-b-discriminant**(1/2))/(2*a)

i1 = -b/(2*a)
i2 = discriminant**(1/2)/(2*a)
complex_root_1 = print(i1, "+", i2, "i")
complex_root_2 = print(i1, "-", i2, "i")

if discriminant > 0:
  print("Roots of quadratic equation are", x1, "and", x2, ".")
elif discriminant == 0:
  print("Root of quadratic equation is", x1, ".")
elif discriminant < 0:
  print("Equation has two complex roots: ", complex_root_1, "and", complex_root_2, ".")