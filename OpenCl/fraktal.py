# I found this example for PyCuda here:
# http://wiki.tiker.net/PyCuda/Examples/Mandelbrot
#
# An improved sequential/pure Python code was contributed
# by CRVSADER//KY <crusaderky@gmail.com>.
#
# I adapted it for PyOpenCL. Hopefully it is useful to someone.
# July 2010, HolgerRapp@gmx.net

import time
#from time import time
import numpy as np
import pyopencl as cl
from six.moves import range

# set width and height of window, more pixels take longer to calculate
w = 4096
h = 4096


def calc_fractal_opencl(q, maxiter):
	ctx = cl.create_some_context()
	queue = cl.CommandQueue(ctx)

	output = np.empty(q.shape, dtype=np.uint16)

	mf = cl.mem_flags
	q_opencl = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=q)
	output_opencl = cl.Buffer(ctx, mf.WRITE_ONLY, output.nbytes)

	prg = cl.Program(ctx, """
	#pragma OPENCL EXTENSION cl_khr_byte_addressable_store : enable
	__kernel void mandelbrot(__global float2 *q,
					 __global ushort *output, ushort const maxiter)
	{
		int gid = get_global_id(0);
		float nreal, real = 0;
		float imag = 0;
		output[gid] = 0;
		for(int curiter = 0; curiter < maxiter; curiter++) {
			nreal = real*real - imag*imag + q[gid].x;
			imag = 2* real*imag + q[gid].y;
			real = nreal;
			if (real*real + imag*imag > 4.0f)
				 output[gid] = curiter;
		}
	}
	""").build()
	gpu_start_time = time.time()
	prg.mandelbrot(queue, output.shape, None, q_opencl,
				   output_opencl, np.uint16(maxiter))

	cl.enqueue_copy(queue, output, output_opencl).wait()
	gpu_end_time = time.time()
	print("GPU Time: {0} s".format(gpu_end_time - gpu_start_time))
	return output

def calc_fractal_cpu(q, maxiter):
	# calculate z using numpy, this is the original
	# routine from vegaseat's URL
	output = np.resize(np.array(0,), q.shape)
	z = np.zeros(q.shape, np.complex64)
	gpu_start_time = time.time()
	for it in range(maxiter):
		z = z*z + q
		done = np.greater(abs(z), 2.0)
		q = np.where(done, 0+0j, q)
		z = np.where(done, 0+0j, z)
		output = np.where(done, it, output)
	gpu_end_time = time.time()
	print("CPU Time: {0} s".format(gpu_end_time - gpu_start_time))
	return output

# choose your calculation routine here by uncommenting one of the options
calc_fractal = calc_fractal_opencl
#calc_fractal = calc_fractal_cpu

if __name__ == '__main__':
	from PIL import Image
	class Mandelbrot(object):
		def __init__(self):
			self.create_image()
		def draw(self, x1, x2, y1, y2, maxiter=30):
			# draw the Mandelbrot set, from numpy example
			xx = np.arange(x1, x2, (x2-x1)/w)
			yy = np.arange(y2, y1, (y1-y2)/h) * 1j
			q = np.ravel(xx+yy[:, np.newaxis]).astype(np.complex64)

			output = calc_fractal(q, maxiter)
			
			self.mandel = (output.reshape((h, w)) /
						   float(output.max()) * 255.).astype(np.uint8)

		def create_image(self):
			""""
			create the image from the draw() string
			"""
			# you can experiment with these x and y ranges
			self.draw(-2.13, 0.77, -1.3, 1.3)
			self.im = Image.fromarray(self.mandel)
			self.im.putpalette([i for rgb in ((j, 0, 0) for j in range(255))
								for i in rgb])
			self.im.save("Fraktal.png")

	# test the class
	test = Mandelbrot()