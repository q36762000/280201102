def pascal_triangle(n):
  if n == 1:
    print("1")
    return [1]
  else:
    x = pascal_triangle(n-1)
    y = [1]
    k = "1"
    for i in range(len(x)):
      if i == len(x)-1:
        y.append(x[i])
        k = k + " " + str(x[i])
        break
      y.append(x[i]+x[i+1])
      k = k + " " + str(x[i]+x[i+1])
    print(k)
    return y
pascal_triangle(10)