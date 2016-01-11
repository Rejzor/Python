import pyopencl as cl
import sys
import Image
import numpy
from time import time

def gpu_gradient():
				
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
	kernelFile = open("gradient.cl", "r")
	kernelSrc = kernelFile.read()

	# Create OpenCL program
	program = cl.Program(ctx, kernelSrc).build()
	# Call the kernel directly
	globalWorkSize = ( imgSize[0],imgSize[1] ) 
	gpu_start_time = time()
	program.gradient(queue,
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
			RGBA2=i,j,0,0
			pixel=RGBA[0]+RGBA2[0],RGBA[1]+RGBA2[1],RGBA[2]+RGBA2[2],RGBA[3]+RGBA2[3]

			final_pixels=list(pixel)
			if final_pixels[0]>255:	
			  	final_pixels[0]=255
			elif final_pixels[1]>255:
			  	final_pixels[1]=255
			pixel=tuple(final_pixels)
			pixels[i,j]=pixel
	im.save("CPU_"+sys.argv[2])
	gpu_end_time = time()
	print("CPU Time: {0} s".format(gpu_end_time - gpu_start_time))
cpu_gradient()
gpu_gradient()