const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | 
						  CLK_ADDRESS_CLAMP | 
						  CLK_FILTER_NEAREST;

__kernel void gradient(read_only image2d_t srcImg,
                              write_only image2d_t dstImg)
{

	int2 coord = (int2) (get_global_id(0), get_global_id(1));

	uint4 pixel = read_imageui(srcImg, sampler, coord);
	uint4 pixel2 = (uint4)(coord.x, coord.y,0,0);
	pixel=pixel + pixel2;
	if(pixel.x > 255) pixel.x=255;
	if(pixel.y > 255) pixel.y=255;
	
		
	// Write the output value to image
	write_imageui(dstImg, coord, pixel);
}