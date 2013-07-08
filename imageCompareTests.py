###########################################################################
#The purpose of this file is to test different methods of image comparison
#
#Author: Michael Dunton 07-07-2013
###########################################################################

from PIL import Image
import ImageChops
import math, operator

#Images to compare
file1 = open('/home/dunton/pyCaptcha/2013-07-07/13:08:26.272077')
file2 = open('/home/dunton/pyCaptcha/2013-07-07/13:08:37.021663')
im1 = Image.open(file1)
im2 = Image.open(file2)


def diff_2011(im1, im2):
    "Calculate the root-mean-square difference between two images"
    diff = ImageChops.difference(im1, im2)
    h = diff.histogram()
    sq = (value*((idx%256)**2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares/float(im1.size[0] * im1.size[1]))
    return rms

imageDiff = diff_2011(im1, im2)
print 'RMS using ImageChops.difference and histogram '
print imageDiff

#histogram diff
h1 = im1.histogram()
h2 = im2.histogram()
rms = math.sqrt(reduce(operator.add,
        map(lambda a,b: (a-b)**2, h1, h2))/len(h1))

print '\n rms = '
print rms


buffer1 = im1.load()
buffer2 = im2.load()
changePixels = 0
for x in xrange(0, 100):
    for y in xrange(0, 75):
         pixdiff = abs(buffer1[x,y][1] - buffer2[x,y][1])
         if (pixdiff > 10):
             changePixels += 1
print '\n Num Pixels changed  ' +str(changePixels)

