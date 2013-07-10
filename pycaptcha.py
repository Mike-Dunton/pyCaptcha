###########################################################################
#Python program to capture an image from url every x seconds and save it to
#a file with now() as the file name
#
#Author: Michael Dunton 07-07-2013
###########################################################################
import ConfigParser, urllib2 ,os, time
from datetime import date, datetime

config = ConfigParser.ConfigParser()
config.readfp(open('config.cfg'))
url = config.get("one", "URL")
rootPath = config.get("one", "SaveLocation")
waitTime = config.getint("one", "WaitTime")
workingDir = -1

def saveImage(theUrl, location):
    try:
        openedUrl = urllib2.urlopen(theUrl)
        streamJpgCapture = open(location + '/' +datetime.now().time().isoformat(), 'w')
        streamJpgCapture.write(openedUrl.read())
        streamJpgCapture.close()
        return True
    except urllib2.URLError as e:
        print e
        return False

   

while(True):
    today = date.today()
    if( workingDir == -1 ):
        workingDir = today.isoformat();
        if not os.path.exists(rootPath + workingDir):
            print'Creating Directory ' + rootPath + workingDir
            os.makedirs(rootPath + workingDir)
            print 'Saving the Image to workingDir\n'
            saveImage(url, workingDir)
            print 'Sleeping' + str(waitTime) + ' seconds'
            time.sleep(waitTime)
        else:
            print 'Todays Directory Exists\n'
            print 'Save the image to workingDir\n'
            saveImage(url, workingDir)
            print 'Sleeping' + str(waitTime) + ' seconds'
            time.sleep(waitTime);
    else:
        if(today.isoformat() > workingDir):
            #Its a new day set a new workingDir and make the folder
            workingDir = today.isoformat();
            if not os.path.exists(rootPath + workingDir):
                print 'creating new workingdir '+ rootPath + workingDir
                os.makedirs(rootPath + workingDir)
                print 'Save the image to workingDir'
                saveImage(url, workingDir)
                print ' Sleeping' + str(waitTime) + ' seconds'
                time.sleep(waitTime)
            else:
                #This should not happen.
                print 'New Days Folder already created....Thats Odd\n'
        else:
            #This case will happen 99% of the time.
            print 'WorkingFolder is set and no need to create new folder'
            print 'save the image\n'
            saveImage(url, workingDir)
            print 'Sleeping' + str(waitTime) + ' seconds'
            time.sleep(waitTime);

