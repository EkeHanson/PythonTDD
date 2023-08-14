import time


print(time.ctime(0))
print(time.ctime(1000000))
print(time.time())
print(time.ctime(time.time()))
print(time.strftime('%B %d %Y %H:%M:%S',time.localtime()))
time_tuple = (2020, 3, 20, 4, 20, 0, 0, 0, 0)
print(time.asctime(time_tuple))