
from rembg import remove
from PIL import Image

input_path = 'cl.jpg' #nome immagine da cui rimuove il background
output_path = 'image_output.png' #nome immagine in output

input = Image.open(input_path)
output = remove(input)
output.save(output_path)