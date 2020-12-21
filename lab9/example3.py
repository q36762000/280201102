def get_evens(my_list):
  if my_list == []:
    return 0
  elif my_list[-1] % 2 == 1:
    return get_evens(my_list[:-1])
  else:
    return 1 + get_evens(my_list[:-1])
print(get_evens([0,1,2,3,4,5]))