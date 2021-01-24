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

print(selection_sort(my_list))