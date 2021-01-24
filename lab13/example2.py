def selection_sort(list):
  n = len(list)
  for left in range(n):
    min_index = left
    for right in range(left+1, n):
      if list[min_index] > list[right]:
        min_index = right
    list[left], list[min_index] = list[min_index], list[left]
  return list

my_list = [22, 8, 12, -4, 27, 30, 36, 50, 7, 68, 91, 56, 2, 85, 42, 98, 25]

def binary_search(list,item):
  if len(list) == 0:
    return False
  mid = len(list) // 2
  if list[mid] == item:
    return mid
  else:
    if item < list[mid]:
      return binary_search(list[:mid],item)
    else:
      return mid + binary_search(list[mid:],item)
print(binary_search(selection_sort(my_list), 85))