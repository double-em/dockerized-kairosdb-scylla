import socket
import time
import random
from datetime import timedelta, datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.17.0.5", 4242))

start_time = time.time()

start_range = 1
num_sensors = 25000
num_repeat = 35000

start_time = (datetime.now() - timedelta(days=365)).timestamp()
end_time = datetime.now().timestamp()

for x in range(1,num_repeat):
	str=""
	time.sleep(1)
	curr_epoch = int(round(random.uniform(start_time, end_time) * 1000))
	# curr_epoch = int(round(time.time() * 1000))

#	print "======================"
#	print x
#	print "Current time " + time.strftime("%X")
#	print "======================"

	for y in range(start_range,start_range+num_sensors):
		statement = "put SENSOR_%d %d %d status=good\n" %(y,curr_epoch,random.randint(1,500))
#		print statement
		s.send(statement.encode())

print("--- %s seconds ---" % (time.time() - start_time))
