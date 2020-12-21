import time
def timer(t):
  if t == 0:
    print("finished!")
    return
  else:
    print("remaining time:",t)
    time.sleep(1)
    return timer(t-1)
timer(5)