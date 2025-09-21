import time

n = 100000

# Use list = list + [x]
start_time = time.time()
l = []
for i in range(n):
    l = l + [i * 2]
print(time.time() - start_time)

# Use list += [x]
start_time = time.time()
l = []
for i in range(n):
    l += [i * 2]
print(time.time() - start_time)

# Use list.append(x)
start_time = time.time()
l = []
for i in range(n):
    l.append(i * 2)
print(time.time() - start_time)
