num_input = int(input("number of items: "))
list_items = []
list_output = []

for i in range(num_input):
  a = input("input: ")
  list_items.append(a)

for i in list_items:
  if i not in list_output:
    list_output.append(i)

print(list_output)