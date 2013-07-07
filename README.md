read ini from text file
	numMinWait
	saveLocation
	url

start
	now = date()

	if( currDate.isSet())
		if(now > currDate)
			create new folder for saves with now.mmddyyyy as name
			currDate = now.mmddyyy
			save image to urrDateFolder with filename now.
		else
			save image to currDateFolder with filename now.
	else
		if(now.mmddyyyy is a folder in save location) //we started the application on the same day we stopped it 
			currDate = now
			save image to currDateFolder with filename now.
		else
			currDate = now
			create new folder currDatefolder for saves
			save image to currDateFolder with filename now.
	sleep(numMinWait)
end



TODO
Get percentage of change in picture from last picture
	if change is sanifigant
		save it. 	
		increase capture rate


