import time

start_time = time.time()
j = 0
for i in range(1,10000):
    j-= 1

end_time = time.time()

print(end_time-start_time)