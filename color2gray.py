import os
from PIL import Image

for file in os.listdir('origin'):
	if file.endswith('.jpg'):
		img = Image.open(os.path.join('origin', file)) #file path
		img = img.convert('L') # convert to L (Grayscale)
		img.save(os.path.join('result', file[:-4] + '_gray.jpg')) #file path
		img.close()