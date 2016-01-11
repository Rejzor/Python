const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | 
						  CLK_ADDRESS_CLAMP | 
						  CLK_FILTER_NEAREST;

__kernel void rgbaToGrayscale(read_only image2d_t srcImg,
                              write_only image2d_t dstImg)
{
	// Converts RGBA image to gray scale intensity using the following formula: 
	// I = 0.299 * R + 0.587 * G + 0.114 * B

	int2 coord = (int2) (get_global_id(0), get_global_id(1));
	int width = get_image_width(srcImg);
	int height = get_image_height(srcImg);

	if (coord.x < width && coord.y < height)
	{
		uint4 color = read_imageui(srcImg, sampler, coord);
		float luminance = 0.299 * color.x + 0.587 * color.y + 0.114 * color.z;
		color.x = color.y = color.z = (uint)luminance;
		
		// Write the output value to image
		write_imageui(dstImg, coord, color);
	}
}