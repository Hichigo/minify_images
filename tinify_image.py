# Need internet connection
# Need API key (https://tinypng.com/developers/reference/python)

import tinify
import os

from tinify_image_key import *

tinify.key = my_api_key

selfDir = os.path.dirname(os.path.abspath(__file__))

imageIn = os.path.join(selfDir, 'imgFull')
imageOut = os.path.join(selfDir, 'imgLite')
thumbOut = os.path.join(selfDir, 'imgThumb')


def tinify_mp(width=None, height=None):
	exts = ('.jpg', '.JPG', '.jpeg', '.JPEG', '.png')
	outImage = ''

	for path, subdirs, files in os.walk(imageIn): # look all folders
		for i, name in enumerate(files): # look all files in folder
			if name.endswith(exts): # check exist extensions
				path_image = os.path.join(path, name)
				outImagePath = path.replace(imageIn, imageOut)
				outImage = os.path.join(outImagePath, name)

				if not os.path.exists(outImagePath): # check not exist path
					os.makedirs(outImagePath) # create path

				source = tinify.from_file(path_image)
				resized = source.resize(
					method="cover",
					width=1920,
					height=1080
				)
				resized.to_file(outImage)

				print(i, name)

if __name__ == '__main__':
	tinify_mp(width=1920, height=1080)