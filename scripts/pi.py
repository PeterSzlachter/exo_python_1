import math
import time

start = time.time()
for i in range(1,100):
    for j in range(1,100):
        if abs(math.pi-i/j) > 0 and abs(math.pi-i/j) < 0.01 :
            print(i/j)
            print(i)
            print(j)

print("total time", time.time()-start)