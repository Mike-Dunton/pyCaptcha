###########################################################################
#The purpose of this file is to test different methods of image comparison
#
#Author: Michael Dunton 07-07-2013
###########################################################################

from PIL import Image
import math

#Images to compare
file1 = open('/home/dunton/pyCaptcha/2013-07-08/19:07:45.978650')
file2 = open('/home/dunton/pyCaptcha/2013-07-08/19:08:07.360427')
im1 = Image.open(file1)
im2 = Image.open(file2)
buffer1 = im1.load()
buffer2 = im2.load()

changePixels = 0
for x in xrange(0, 319):
    for y in xrange(0, 239):
         pixdiff = abs(buffer1[x,y][1] - buffer2[x,y][1])
         if (pixdiff > 10):
             changePixels += 1
print '\n Num Pixels changed  ' +str(changePixels)

