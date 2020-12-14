def dec_to_binary(a):
  output = ""
  while a != 0:
    if a % 2 == 1:
      output += "1"
    else:
      output += "0"
    a = a // 2
  output = output[::-1]
  return output

def binary_to_dec(a):
  output = 0
  a = str(a)
  while a != "":
    for i in range(len(a)):
      if a[-1] == "1":
        output += 2**i
      a = a[:-1]
  return output

print(dec_to_binary(8362))
print(binary_to_dec(10000010101010))