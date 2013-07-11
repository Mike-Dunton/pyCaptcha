###########################################################################
#Python program to capture an image from url every x seconds and save it to
#a file with now() as the file name
#
#Author: Michael Dunton 07-07-2013
###########################################################################
import ConfigParser, urllib2 ,os, math, time, cStringIO
from datetime import date, datetime
from PIL import Image


def getConfig():
    """Gets the Items from the Config File"""
    config = ConfigParser.ConfigParser()
    config.readfp(open('config.cfg'))
    configList = config.items('one')
    return dict(configList)


def compareImages(im1, im2, pixelDiff):
    """Compares two images pixel by pixel"""
    buffer1 = im1.load()
    buffer2 = im2.load()
    changedPixels = 0
    for x in xrange(0, 319):
        for y in xrange(0, 239):
            changeAmount = abs(buffer1[x,y][1] - buffer2[x,y][1])
            if (changeAmount > int(pixelDiff)):
                changedPixels += 1
    print str(changedPixels)+ ' ' + pixelDiff
    return changedPixels

def getImage(theUrl):
    """gets an image from theUrl"""
    try:
        openedUrl = urllib2.urlopen(theUrl)
        print 'Got an image'
        fileAsString = cStringIO.StringIO(openedUrl.read())
        img = Image.open(fileAsString)
        return img
    except urllib2.URLError as e:
        print e
        return False

def saveImage(theFile, location):
    """Saves an image to location"""
    print location
       # streamJpgCapture = open(location, 'w')
       # streamJpgCapture.write(theFile.read())
    theFile.save(location)
    print 'Saved an image'
       # streamJpgCapture.close()

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
            del imageToCompare
            time.sleep(5)
            print 'Sleep 5 seconds'
        else:
            workingDir = today.isoformat()
            fullDir = c['savelocation'] + workingDir + "/"
            imageToCompare = getImage(c['url'])
            if( compareImages(baseImage, imageToCompare, pixDiff) > int(threshold)):
                saveImage(imageToCompare, fullDir + getFileName())
                baseImage = imageToCompare
            
            print 'Compared an image about to sleep'
            time.sleep(5);
    else:
        workingDir = today.isoformat()
        fullDir = c['savelocation'] + workingDir + "/"
        if not ( createSaveLocation(fullDir) ):
            imageToCompare = getImage(c['url'])
            saveImage(imageToCompare, fullDir + getFileName())
            baseImage = imageToCompare
            print 'Sleep 5 seconds'
            print 'Path Did not exist and I created it also saved first base image'
            time.sleep(5)
        else:
            print 'Path did exist did  not create'
     

