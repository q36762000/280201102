num = int(input("enter a positive integer: "))
while num < 0:
  num = int(input("please enter a positive integer:"))  

i_times_num = 0
for i in range(1,11):
  i_times_num += num 
  print(num, "x", i, "=", i_times_num) 
