# import time
#
# time1=time.time()
# #for i in range(1000):
#  #    print("a")
# time2=float(10)
# # print(time1,time2,time2-time1)
# while float(time.time()) == time2+time1():
#     print("10 secs")
# #    time2 = time.time()


import time

now = time.time()
future = now + 10
while time.time() < future:
    # do stuff
    pass
print("The game stop")