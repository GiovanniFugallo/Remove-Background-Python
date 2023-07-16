
from rembg import remove
from PIL import Image

input_path = 'cl.jpg' #name of input image
output_path = 'image_output.png' #name of output image

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
