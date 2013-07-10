###########################################################################
#Python program to capture an image from url every x seconds and save it to
#a file with now() as the file name
#
#Author: Michael Dunton 07-07-2013
###########################################################################
import ConfigParser, urllib2 ,os, math, time
from datetime import date, datetime
from PIL import Image


def getConfig():
    """Gets the Items from the Config File"""
    config = ConfigParser.ConfigParser()
    config.readfp(open('config.cfg'))
    configList = config.items('one')
    return dict(configList)


def compareImages(file1, file2, pixelDiff):
    """Compares two images pixel by pixel"""
    im1 = Image.open(file1)
    im2 = Image.open(file2)
    buffer1 = im1.load()
    buffer2 = im2.load()
    changedPixels = 0
    for x in xrange(0, 319):
        for y in xrange(0, 239):
            changeAmount = abs(buffer1[x,y][1] - buffer2[x,y][1])
            if (changeAmount > pixelDiff):
                changedPixels += 1
    return changedPixels

def getImage(theUrl):
    """gets an image from theUrl"""
    try:
        openedUrl = urllib2.urlopen(theUrl)
        print 'Got an image'
        return openedUrl
    except urllib2.URLError as e:
        print e
        return False

def saveImage(theFile, location):
    """Saves an image to location"""
    print location
    try:
        streamJpgCapture = open(location, 'w')
        streamJpgCapture.write(theFile.read())
        print 'Saved an image'
        streamJpgCapture.close()
        return True
    except IOError as (errno, strerror):
        print "I/O error({0}): {1}".format(errno, strerror)
        return False

def createSaveLocation(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    else:
        return False
def getFileName():
    """Returns the Current Time in HH MM SS"""
    fileName = datetime.now().time().replace(microsecond=0).isoformat() +".jpg"
    return fileName
###########################################################################
#To Start the program we Need to set workingDir to -1
#and must capture a base image, The image we compare against
#and grab the config
###########################################################################
c = getConfig()
baseImage = getImage(c['url'])
workingDir = -1;
fullDir = "/"
threshold = c['threshold']
pixDiff = c['pixeldiff']
while(True):
    today = date.today()
    if( workingDir != -1):
        workingDir = today.isoformat()
        fullDir = c['savelocation'] + workingDir + "/"
        if (createSaveLocation(fullDir)):
            imageToCompare = getImage(c['url'])
            saveImage(imageToCompare, fullDir + getFileName())
            baseImage = imageToCompare
            time.sleep(5)
            print 'Sleep 5 seconds'
        else:
            workingDir = today.isoformat()
            fullDir = c['savelocation'] + workingDir + "/"
            imageToCompare = getImage(c['url'])
            if( compareImages(baseImage, imageToCompare, c['pixeldiff']) > threshold):
                saveImage(imageToCompare, fullDir + getFileName())
                print 'Compared an image and Saved it about to sleep'
                time.sleep(5)
    else:
        workingDir = today.isoformat()
        fullDir = c['savelocation'] + workingDir + "/"
        if( createSaveLocation(fullDir) ):
            imageToCompare = getImage(c['url'])
            saveImage(imageToCompare, fullDir + getFileName())
            baseImage = imageToCompare
            print 'Sleep 5 seconds'
            print 'Path Did not exist and I created it also saved first base image'
            time.sleep(5)
        else:
            print 'Path did exist did  not create'
     

