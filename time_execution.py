import time
start_time = time.time()

x = 0
for i in range(1000000):
    x += i**2

end_time = time.time()

print("Execution time: ",end_time - start_time)
