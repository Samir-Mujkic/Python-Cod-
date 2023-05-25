#import time

#print(time.gmtime(0))

#print(time.localtime())

#print(time.time())

import time
from time import process_time as my_timer
import random

input("please enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("press enter to stop")

end_time = my_timer()

print("started at " + time.strftime("%X", time.localtime(start_time)))
print("ended at " + time.strftime("%X", time.localtime(end_time)))

print("your reaction time was {} seconds".format(end_time - start_time))