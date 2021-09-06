import socket
import time
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.17.0.5", 4242))

start_time = time.time()

start_range = 1
num_sensors = 1
num_repeat = 10000

for x in range(1,num_repeat):
	str=""
	time.sleep(1)
	curr_epoch = int(round(time.time() * 1000))
#	print "======================"
#	print x
#	print "Current time " + time.strftime("%X")
#	print "======================"
	for y in range(start_range,start_range+num_sensors):
		statement = "put TEST_SENSOR %d %d status=good\n" %(curr_epoch,random.randint(1,500))
#		print statement
		s.send(statement.encode())

print("--- %s seconds ---" % (time.time() - start_time))
