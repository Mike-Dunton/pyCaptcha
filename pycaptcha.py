import ConfigParser, os, time
from datetime import date

config = ConfigParser.ConfigParser()
config.readfp(open('config.cfg'))
url = config.get("one", "URL")
rootPath = config.get("one", "SaveLocation")
waitTime = config.getint("one", "WaitTime")

print url,rootPath, waitTime
workingFolder = -1

#while(true):
for n in range(0, 2):
    today = date.today()
    if( workingFolder == -1 ):
        workingFolder = today.isoformat();
        if not os.path.exists(rootPath + workingFolder):
            os.makedirs(rootPath + workingFolder)
        else:
            print 'Todays Directory Exists'
    else:
        if(today.isoformat() > workingFolder):
            workingFolder = today.isoformat();
            if not os.path.exists(rootPath + workingFolder):
                os.makedirs(rootPath + workingFolder)
            else:
                print 'New Days Folder already created....Thats Odd'
        else:
            print 'save the image'


