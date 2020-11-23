num = int(input("enter an integer: "))
while num < 0 or num > 10:
  num = int(input("please enter a valid integer:")) 

i_times_num = 0
for i in range(1,11):
  i_times_num += num
  print(num, "x", i, "=", i_times_num)