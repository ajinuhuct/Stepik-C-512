import time
start_time = time.time()
objects = [0,1,3,1,2,4,3,9]
a = set()
for obj in objects:
    a.add(id(obj))
print(len(a))
print("--- %s seconds ---" % (time.time() - start_time))

start_time2 = time.time()
objects = [0,1,3,1,2,4,3,9]
n = len(objects)
ans = n
for i in range(n):
    for j in range(i):
        if id(objects[i]) == id(objects[j]):
            ans -= 1
            break


print(ans)
print("--- %s seconds ---" % (time.time() - start_time2))