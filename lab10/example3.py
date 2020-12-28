def sum_of_list(list):
  if list == []:
    return 0
  elif str(list[0])[0] == "[":
    return sum_of_list(list[0]) + sum_of_list(list[1:])
  else:
    return list[0] + sum_of_list(list[1:])
print(sum_of_list([3,12,76,[4,56,43],[2,8],81,75]))