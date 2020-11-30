book = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
for i in book:
  book_dict[i] = (len(i), len(set(i)), (len(i)+len(set(i)))/2)
print(book_dict)