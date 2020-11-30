numbers1 = set([2,3,4,20,5,5,15])
numbers2 = set([10,20,20,15,30,40])
intersection = []
union = list(numbers2)
for i in numbers1:
  if i in numbers2:
    intersection.append(i)
  if i not in numbers2:
    union.append(i)
print(intersection)
print(union)