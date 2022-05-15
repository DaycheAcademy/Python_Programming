
import time

temp = {key: val for key, val in zip(range(1, 10000000), range(1, 30000000, 3))}

print(len(temp))

sumVal = 0
start_time = time.time()
for v in temp.values():
    sumVal += v ** 2 / 3.7658758
end_time = time.time()
print('time lapse: ', abs(end_time - start_time))



sumVal = 0
start_time = time.time()
for k in temp:
    sumVal += temp[k] ** 2 / 3.7658758
end_time = time.time()
print('time lapse: ', abs(end_time - start_time))

# ===================================








