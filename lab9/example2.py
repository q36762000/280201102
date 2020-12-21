my_list = [1,2,3,4,5]

def recursive(my_list):
  if  my_list == []:
    return []
  else:
    return [my_list[-1]] + recursive(my_list[:-1])

print(recursive(my_list))