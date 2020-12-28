def pascals_triangle_last_line(n):
  if n == 1:
    return [1]
  else:
    x = pascals_triangle_last_line(n-1)
    y = [1]
    for i in range(len(x)):
      if i == len(x)-1:
        y.append(x[i])
        break
      y.append(x[i]+x[i+1])
    return y
print(pascals_triangle_last_line(10))