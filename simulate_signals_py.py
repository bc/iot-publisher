from helper_functions import *
import zmq
import random
import sys
import time

port = "555"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)
shouldSleep=False
f = open("sample_streams.txt", "r")
emgs = f.readlines()
counter = 10;
earlier = now()
while True:
    messagedata = emgs[counter%77670] 
    socket.send_string(messagedata)
    counter += 1
    if shouldSleep:
	    time.sleep(0.0007)
    if counter % 1000 == 0:
    	elapsed = (now() - earlier)/1000.0
    	print("delta is" + str(elapsed) + "per 1k messages; " + str(1000.0/elapsed) + " Hz")
    	earlier = now()
