import random
def get_rand_list(x, y, n):
  k = random.sample(range(x,y), n)
  return k
def get_overlap(first, second):
  list = []
  for i in first:
    for k in second:
      if i == k:
        list.append(i)
  return list
def main():
  x = int(input("begin:"))
  y = int(input("end:"))
  n = int(input("N:"))
  first = get_rand_list(x, y, n)
  second = get_rand_list(x, y, n)
  list = get_overlap(first, second)
  print(first)
  print(second)
  print(list)

main()