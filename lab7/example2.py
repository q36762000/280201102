book = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
count = 0
book_dict = {}
d = []
for i in book:
  for k in i:
    if k not in d:
      d.append(k)
      count += 1
  book_dict[i] = (len(i), count)
  count = 0
  d = []
print(book_dict)