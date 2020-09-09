import cv2
import image_slicer
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


number_of_tiles = 8
num_of_cols = 4
num_of_rows = 2

tiles = image_slicer.slice("images/laka.jpg",number_of_tiles)

im = Image.open("images/toledo.png")
im = np.asarray(im)

parts = [im[x:x+num_of_cols,y:y+num_of_rows] for x in range(0,im.shape[0],num_of_cols) for y in range(0,im.shape[1],num_of_rows)]
print(parts[0])