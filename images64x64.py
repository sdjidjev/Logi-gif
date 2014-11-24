import numpy as np
import cv2
import os

new_filename = "dino"
f1 = open(new_filename+'_1.txt', 'w')
f2 = open(new_filename+'_2.txt', 'w')
f3 = open(new_filename+'_3.txt', 'w')
f4 = open(new_filename+'_4.txt', 'w')
f1.write("v2.0 raw\n")
f2.write("v2.0 raw\n")
f3.write("v2.0 raw\n")
f4.write("v2.0 raw\n")
frequency = (4096.0/32.0)

def write_image(filename, frames, frames_written, num, num_frames):
    im = cv2.imread(filename)
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    # print imgray
    hex_imgray_1 = []
    hex_imgray_2 = []
    hex_imgray_3 = []
    hex_imgray_4 = []
    for row in range(1,33): # NW Corner
        string=""
        for i in range(1,33):
            if imgray[row][i] >= 255/2:
                imgray[row][i] = 1
            else:
                imgray[row][i] = 0
            string+=str(int(imgray[row][i]))
        hex_imgray_1.append(hex(int(string, 2))[2:]+"\n")
    for row in range(0,32): # NE Corner
        string=""
        for i in range(32,64):
            if imgray[i][row] >= 255/2:
                imgray[i][row] = 1
            else:
                imgray[i][row] = 0
            string+=str(int(imgray[i][row]))
        hex_imgray_2.append(hex(int(string, 2))[2:]+"\n")
    for row in range(32,64): # SW Corner
        string=""
        for i in range(0,32):
            if imgray[i][row] >= 255/2:
                imgray[i][row] = 1
            else:
                imgray[i][row] = 0
            string+=str(int(imgray[i][row]))
        hex_imgray_3.append(hex(int(string, 2))[2:]+"\n")
    for row in range(32,64): # SECorner
        string=""
        for i in range(32,64):
            if imgray[i][row] >= 255/2:
                imgray[i][row] = 1
            else:
                imgray[i][row] = 0
            string+=str(int(imgray[i][row]))
        hex_imgray_4.append(hex(int(string, 2))[2:]+"\n")
    for frame in range(0,frames):
        for hex_val in hex_imgray_1:
            f1.write(hex_val)
        for hex_val in hex_imgray_3:
            f2.write(hex_val)
        for hex_val in hex_imgray_2:
            f3.write(hex_val)
        for hex_val in hex_imgray_4:
            f4.write(hex_val)

num_frames = 0
while(os.path.isfile(new_filename+"_resized_"+str(num_frames)+".png")):
    num_frames += 1
frames_written = 0
while frames_written < 4096:
    for j in range(0,num_frames):
        if frames_written >= 4096:
            break
        write_image(new_filename+"_resized_"+str(j)+".png",2,frames_written, j, num_frames)
        frames_written += 64

f1.close()
f2.close()
f3.close()
f4.close()

