book = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
count = 0
book_dict = {}
for i in book:
  len2 = len(set(i))
  book_dict[i] = (len(i), len2)
print(book_dict)