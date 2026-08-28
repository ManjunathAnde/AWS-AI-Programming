import time
from time import sleep

start_time= time.time()
sleep(5) #makes the runtime sleep for 5 seconds
end_time=time.time()

final_time = end_time - start_time
print(final_time)