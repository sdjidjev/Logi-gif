import numpy as np
import cv2

new_filename = "horse"
f1 = open(new_filename+'_1.txt', 'w')
f2 = open(new_filename+'_2.txt', 'w')
f3 = open(new_filename+'_3.txt', 'w')
f4 = open(new_filename+'_4.txt', 'w')
f1.write("v2.0 raw\n")
f2.write("v2.0 raw\n")
f3.write("v2.0 raw\n")
f4.write("v2.0 raw\n")
frequency = (512.0/32.0)

def write_image(filename, time):
	im = cv2.imread(filename)
	imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	# print imgray
	hex_imgray_1 = []
	hex_imgray_2 = []
	hex_imgray_3 = []
	hex_imgray_4 = []
	print imgray
	for row in range(1,32): # NW Corner
		string=""
		for i in range(1,32):
			if imgray[row][i] >= 255/2:
				imgray[row][i] = 1
			else:
				imgray[row][i] = 0
			string+=str(int(imgray[row][i]))
		string+="0"
		hex_imgray_1.append(hex(int(string, 2))[2:]+"\n")
		# print hex(int(string, 2))[2:]
	# frames = int(float(time)*float(frequency))
	hex_imgray_1.append("0\n")
	for row in range(0,32): # NE Corner
		string=""
		for i in range(32,64):
			if imgray[i][row] >= 255/2:
				imgray[i][row] = 1
			else:
				imgray[i][row] = 0
			string+=str(int(imgray[i][row]))
		hex_imgray_2.append(hex(int(string, 2))[2:]+"\n")
		# print hex(int(string, 2))[2:]
	# frames = int(float(time)*float(frequency))
	for row in range(32,64): # SW Corner
		string=""
		for i in range(0,32):
			if imgray[i][row] >= 255/2:
				imgray[i][row] = 1
			else:
				imgray[i][row] = 0
			string+=str(int(imgray[i][row]))
		hex_imgray_3.append(hex(int(string, 2))[2:]+"\n")
		# print hex(int(string, 2))[2:]
	# frames = int(float(time)*float(frequency))
	for row in range(32,64): # SECorner
		string=""
		for i in range(32,64):
			if imgray[i][row] >= 255/2:
				imgray[i][row] = 1
			else:
				imgray[i][row] = 0
			string+=str(int(imgray[i][row]))
		hex_imgray_4.append(hex(int(string, 2))[2:]+"\n")
		# print hex(int(string, 2))[2:]
	# frames = int(float(time)*float(frequency))
	for frame in range(0,time):
		for hex_val in hex_imgray_1:
			f1.write(hex_val)
		for hex_val in hex_imgray_3:
			f2.write(hex_val)
		for hex_val in hex_imgray_2:
			f3.write(hex_val)
		for hex_val in hex_imgray_4:
			f4.write(hex_val)

for i in range(0,11):
	# print "ball_resized_"+str(i)+".png"
	# print i
	write_image(new_filename+"_resized_"+str(i)+".png",4)
for i in range(0,11):
	# print "ball_resized_"+str(i)+".png"
	# print i
	write_image(new_filename+"_resized_"+str(i)+".png",4)
f1.close()
f2.close()
f3.close()
f4.close()

