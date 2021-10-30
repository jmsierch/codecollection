import sys
import os
from PIL import Image

# Grab the first and second arguments
print('')
print('Hello. This is a program to convert JPG files to PNG.')
print('')
print('Let us begin by verifying user inputs...')
print('Number of Arguments: ', len(sys.argv))
originalFolder = sys.argv[1]
destinationFolder = sys.argv[2]
print('Arguments are: ', str(sys.argv))

# Check if new exists, if not create it
print('')
print('Now let us see if the desired destination folder exists. If not we will create it.')
check_folder = os.path.isdir(destinationFolder)
if not check_folder:
	os.makedirs(destinationFolder)
	print('A new folder was created called: ', destinationFolder)
else:
	print(destinationFolder, 'folder already exists.')
print('')

# Loop through the folder and convert images to PNG
print('Now each JPG image present will be converted to PNG in your desired folder.')
print('')

from PIL import Image
c=1
for filename in os.listdir(originalFolder):
    if filename.endswith('.jpg'):
    	img = Image.open(filename)
    	name = 'img' + str(c) + '.png'
    	imgConvert = img.convert('RGB')
    	imgConvert.save(name)
    	c+=1
    	print(os.path.join(destinationFolder, filename))
    	continue
    else:
    	continue

# Save images to new folder
print('')
print('All JPG images have been converted to PNG and placed in destination folder.')
print('Goodbye!')
