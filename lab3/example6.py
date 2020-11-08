print("Write the parameters for represented quadratic equation : (ax**2 + b*x + c)")
a = float(input("Type a: "))
b = float(input("Type b: "))
c = float(input("Type c: "))

discriminant = b**2-(4*a*c)

x1 = (-b+discriminant**(1/2))/(2*a)
x2 = (-b-discriminant**(1/2))/(2*a)

if discriminant > 0:
  print("Roots of quadratic equation are", x1, "and", x2, ".")
elif discriminant == 0:
  print("Root of quadratic equation is", x1, ".")
elif discriminant < 0:
  print("Quadratic equation does have two complex roots.")