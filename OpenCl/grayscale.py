import pyopencl as cl
import sys
import Image
import numpy
from time import time

def gpu_grayscale():
				
	if len(sys.argv) != 3:
		print "USAGE: " + sys.argv[0] + " <inputImageFile> <outputImageFile>"
		return 1
	
	# create context and command queue
	ctx = cl.create_some_context()
	queue = cl.CommandQueue(ctx)
	
	# load image
	im = Image.open(sys.argv[1])
	if im.mode != "RGBA":
		im = im.convert("RGBA")
	imgSize = im.size
	buffer = im.tostring() # len(buffer) = imgSize[0] * imgSize[1] * 4

	
	# Create ouput image object
	clImageFormat = cl.ImageFormat(cl.channel_order.RGBA, 
								cl.channel_type.UNSIGNED_INT8)
	input_image = cl.Image(ctx,
								cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR,
								clImageFormat,
								imgSize,
								None,
								buffer)
	output_image = cl.Image(ctx,
							cl.mem_flags.WRITE_ONLY,
							clImageFormat,
							imgSize)

	# load the kernel source code
	kernelFile = open("grayscale.cl", "r")
	kernelSrc = kernelFile.read()

	# Create OpenCL program
	program = cl.Program(ctx, kernelSrc).build()
	# Call the kernel directly
	globalWorkSize = ( imgSize[0],imgSize[1] ) 
	gpu_start_time = time()
	program.rgbaToGrayscale(queue,
							globalWorkSize,
							None,
							input_image,
							output_image)
		
	# Read the output buffer back to the Host
	buffer = numpy.zeros(imgSize[0] * imgSize[1] * 4, numpy.uint8)
	origin = ( 0, 0, 0 )
	region = ( imgSize[0], imgSize[1], 1 )
	
	cl.enqueue_read_image(queue, output_image,
						origin, region, buffer).wait()
	
	# Save the image to disk
	gsim = Image.fromstring("RGBA", imgSize, buffer.tostring())
	gsim.save("GPU_"+sys.argv[2])
	gpu_end_time = time()
	print("GPU Time: {0} s".format(gpu_end_time - gpu_start_time))

def cpu_grayscale():
	if len(sys.argv) != 3:
		print "USAGE: " + sys.argv[0] + " <inputImageFile> <outputImageFile>"
		return 1

	# load image and convert to grayscale L = R * 299/1000 + G * 587/1000 + B * 114/1000
	gpu_start_time = time()
	im = Image.open(sys.argv[1]).convert('LA')
	if im.mode != "RGBA":
		im = im.convert("RGBA")

	im.save("CPU_"+sys.argv[2])
	gpu_end_time = time()
	print("CPU Time: {0} s".format(gpu_end_time - gpu_start_time))
cpu_grayscale() #CPU Time: 0.221253871918 s,test.jpg 1920x1440
gpu_grayscale()	#GPU Time: 0.172569990158 s, test.jpg 1920x1440