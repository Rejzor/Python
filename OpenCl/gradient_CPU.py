import Image
import numpy as np
import sys
from time import time

def cpu_gradient():
	if len(sys.argv) != 3:
		print "USAGE: " + sys.argv[0] + " <inputImageFile> <outputImageFile>"
		return 1

	gpu_start_time = time()
	im = Image.open(sys.argv[1])
	if im.mode != "RGBA":
		im = im.convert("RGBA")
	pixels = im.load()
	for i in range(im.size[0]):
		for j in range(im.size[1]):
			
			RGBA= pixels[i,j]
			RGBA2=RGBA[0],RGBA[1],0,0
			pixel=RGBA[0]+RGBA2[0],RGBA[1]+RGBA2[1],RGBA[2],RGBA[3]

			final_pixels=list(pixel)
			if final_pixels[0]>255:	
			  	final_pixels[0]=255
			elif final_pixels[1]>255:
			  	final_pixels[1]=255
			pixel_fn=tuple(RGBA2)
			pixels[i,j]=pixel_fn
	im.save("CPU_"+sys.argv[2])
	gpu_end_time = time()
	print("CPU Time: {0} s".format(gpu_end_time - gpu_start_time))
cpu_gradient()
