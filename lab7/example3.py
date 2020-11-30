employees = {}
for i in range(5):
  name = input("name:")
  salary = int(input("salary:"))
  employees[name] = salary

salaries = sorted(employees.values())
itr = 0
for a in salaries:
  if itr >= 2:
    for b in employees.keys():
      if employees[b] == a:
        print(b)
        print(employees[b])
  itr = itr +1