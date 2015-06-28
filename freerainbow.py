#!/usr/bin/python
# Apply rainbow effect on a image

from PIL import Image

# Rainbow colors
colors = (
	(0xff, 0x00, 0x00), # Red
	(0xff, 0x7f, 0x00), # Orange
	(0xff, 0xff, 0x00), # Yellow
	(0x00, 0xff, 0x00), # Green
	(0x00, 0x7f, 0xff), # Blue
	(0x7f, 0x00, 0xff)) # Purple

def rainbow(img):
	global colors

	if isinstance(img, str):
		img = Image.open(img)
	img.convert('RGB')

	# The size of each piece that will put a rainbow color
	m = img.size[1]/6 

	# Generate a list of pixels, it has the size image height
	rainbow = [[i,]*m for i in colors]  
	rainbow = reduce(lambda x, y: x + y, rainbow)

	#Apply colors
	for i in range(len(rainbow)):
		for j in range(img.size[0]):
			pix = list(img.getpixel((j, i)))
			for k in range(3):
				pix[k] = (pix[k] + rainbow[i][k])/2
			img.putpixel((j, i), tuple(pix))

	return img

def main():
	import sys

	if len(sys.argv) != 3:
		print 'Usage:\n\n%s FILENAME OUTPUT' % sys.argv[0]
		sys.exit()

	openFilename = sys.argv[1]
	saveFilename = sys.argv[2]
	img = rainbow(openFilename)

	img.save(saveFilename)

if __name__ == '__main__':
	main()
