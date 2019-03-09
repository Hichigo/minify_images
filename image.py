from PIL import Image
import os

selfDir = os.path.dirname(os.path.abspath(__file__))

imageIn = os.path.join(selfDir, 'imgFull')
imageOut = os.path.join(selfDir, 'imgLite')
thumbOut = os.path.join(selfDir, 'imgThumb')

def scale_images(input_image_path, output_image_path, width=None, height=None):

	exts = ('.jpg', '.JPG', '.jpeg', '.JPEG', '.png')
	outImage = ''

	for path, subdirs, files in os.walk(input_image_path): # look all folders
		for name in files: # look all files in folder
			if name.endswith(exts): # check exist extensions
				path_image = os.path.join(path, name)
				outImagePath = path.replace(input_image_path, output_image_path)
				outImage = os.path.join(outImagePath, name)

				if not os.path.exists(outImagePath): # check not exist path
					os.makedirs(outImagePath) # create path

				original_image = Image.open(path_image)
				w, h = original_image.size
				
				# if (w, h) <= (width, height): #check size image
				# 	print('The picture has little!')
				# 	continue

				if width and height:
					max_size = (width, height)
				elif width:
					max_size = (width, h)
				elif height:
					max_size = (w, height)
				else:
					# No width or height specified
					raise RuntimeError('Width or height required!')

				original_image.thumbnail(max_size, Image.ANTIALIAS)
				original_image.save(outImage)

				# just debug information
				scaled_image = Image.open(outImage)
				s_width, s_height = scaled_image.size
				print('w: {wide} h: {height} --> w: {newwide} h: {newheight}'.format(wide=w, height=h, newwide=s_width, newheight=s_height))

if __name__ == '__main__':
	scale_image(input_image_path=imageIn, output_image_path=imageOut, width=1000, height=1000)