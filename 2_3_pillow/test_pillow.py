#!/usr/bin/python3

from PIL import Image

im = Image.new("RGB", (128,128),"red")
im.save("red.jpg")


im_copy = im.resize((256,256),resample=0,box=None)

im_copy.save('red_resize.jpg')
