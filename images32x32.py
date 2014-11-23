import numpy as np
import cv2
import os

new_filename = 'loading' # enter filename of gif
frame_time = 0.01 # time (in seconds) for each frame
max_frames = 4096
f = open(new_filename+'.txt', 'w')
f.write("v2.0 raw\n")
one_loop = 5
frequency = (4096.0/32.0) # number frames allowed

def write_image(filename, frames):
	im = cv2.imread(filename)
	imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	hex_imgray = []
	for row in range(0,len(imgray)):
		string=""
		for i in range(0,len(imgray[row])):
			if imgray[i][row] >= 255/2:
				imgray[i][row] = 1
			else:
				imgray[i][row] = 0
			string+=str(int(imgray[i][row]))
		hex_imgray.append(hex(int(string, 2))[2:]+"\n")
	# frames = int(float(time)/float(frequency))
	for frame in range(0,frames):
		for hex_val in hex_imgray:
			f.write(hex_val)
num_frames = 0
while(os.path.isfile(new_filename+"_resized_"+str(num_frames)+".png")):
	num_frames += 1

for j in range(0,num_frames):
	write_image(new_filename+"_resized_"+str(j)+".png",int((float(frequency)/float(num_frames))))

f.close()

