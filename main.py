import PIL.Image
from argparse import ArgumentParser
from sys import stdout


ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]


def main():
	parser = ArgumentParser(description = """ASCII art generator Photo to ASCII art""")
	parser.add_argument("-img", type = str, help = "input image file name")
	parser.add_argument("-out", type = str, help = "output text file name ")
	args = parser.parse_args()
	stdout.write(str(convertor(args)))
	
def resize(image, new_width = 100):
    width, height = image.size
    new_height = new_width * height / width
    return image.resize((int(new_width), int(new_height)))

def to_greyscale(image):
    return image.convert("L")  

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str
						
def convertor(args):
	image = PIL.Image.open(args.img)	
	image = resize(image)
	greyscale_image = to_greyscale(image) 
	ascii_str = pixel_to_ascii(greyscale_image)
	img_width = greyscale_image.width
	ascii_str_len = len(ascii_str)
	ascii_img=""
	for i in range(0, ascii_str_len, img_width):
		ascii_img += ascii_str[i:i+img_width] + "\n"
	if args.out != None:
		with open(args.out, "w") as f:
			f.write(ascii_img)
		return "Your ascii art at {}".format(args.out)
	return ascii_img
	
if __name__ == "__main__":
	try:
		main()
	except FileNotFoundError:
		print("Image file not found")
	except AttributeError:
		print("""Arguments missing
type python main.py -h for more info""")
	except Exception as a:
		print(a)
		print("Create your issue with screenshot at https://github.com/gowtham758550/Ascii-Art/issues")