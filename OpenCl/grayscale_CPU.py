import sys
import Image
from time import time
#CPU Time: 0.221253871918 s,test.jpg 1920x1440
def main():
	if len(sys.argv) != 3:
		print "USAGE: " + sys.argv[0] + " <inputImageFile> <outputImageFile>"
		return 1

	# load image and convert to grayscale L = R * 299/1000 + G * 587/1000 + B * 114/1000
	gpu_start_time = time()
	im = Image.open(sys.argv[1]).convert('LA')
	if im.mode != "RGBA":
		im = im.convert("RGBA")

	im.save(sys.argv[2])
	gpu_end_time = time()
	print("CPU Time: {0} s".format(gpu_end_time - gpu_start_time))
main()