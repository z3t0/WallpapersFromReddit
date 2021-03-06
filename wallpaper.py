import glob
import urllib2
import json
import os
import getpass
import time
import argparse

#URL of the wallpaper JSON
url = 'http://www.reddit.com/r/wallpaper.json' #Default url - if no subreddit specified then use this
WallpaperCount=0

#ArgParse function to enter subreddit name or to download new images right now!
def parse_args():
	parser = argparse.ArgumentParser(
		description = 'Set wallpaper from your choice of subreddit!')
	parser.add_argument(
		'--subreddit', type=str, help = 'Your choice of subreddit to download Images')
	args = parser.parse_args()
	if args.subreddit :
		return args.subreddit
	else :
		return None

#To remove non-jpg downloaded photos
def removeUnwantedPhotos(listwallpaper):
	for paths in listwallpaper:
		if os.path.getsize(paths) < 102400:
			np = "rm " + paths
			os.system(np)

#Returns a list of wallpapers from the folder
def returnwallpaper():
	username = getpass.getuser()
	listWallpaper = glob.glob("/home/"+username+"/Wallpapers/*.jpg")
	print("Wallpapers Returned : ",listWallpaper)	
	return listWallpaper
	
#Gets the list of wallpaper and sets a new wallpaper based on count
def setwallpaper(listwallpaper, count):
	filepath = "gsettings set org.gnome.desktop.background picture-uri file:" + listwallpaper[count]
	os.system(filepath)


def download(dCount):
	checkVar = 0

	#To avoid 'Too many requests error - 2 second wait and try again in case of error'
	while(checkVar==dCount):
		try:
			obj = urllib2.urlopen(url)
			data = json.load(obj)
			print("Connection Established! Hurrah!")
			checkVar += 1
		except:
			print("Request Error, Trying again!")
			time.sleep(2)
			pass
	#Directory to save the downloaded images
	username = getpass.getuser() #Gets current user to save files accordingly
	directory = "/home/"+username+"/Wallpapers/"

	#Check if Directory alredy exists, If doesn't exist, create new directory
	if not os.path.exists(directory):
		os.makedirs(directory)
		print("New directory Made!")
  
	for i in data["data"]["children"]:

	  imurl = i["data"]["url"]
	  checkUrl = str(imurl)

	  #Checking if the link extracted is actually an image
	  if "" in checkUrl:
	  	#print(checkUrl)
	  	try:

		    print imurl
	    
		    req = urllib2.Request(imurl+".jpg")
		    time.sleep(2)
		    #Get the Data in the URL
		    imgdata = urllib2.urlopen(req).read()
		    time.sleep(2)
		    print("Downloaded Image!")
		    #Create a new image file and write to it
		    fp = open((directory + "%s"+".jpg") %(dCount) ,"wb")
		    
		    fp.write(imgdata)

		    fp.close()

		    dCount = dCount + 1
	    
		except:
		    pass
        time.sleep(2)
	print dCount
  	return dCount


#Time Countdown function to check wallpaper change time or download time
def countdownDownload(timerDownload, timerupdate,count):

	stu = timerupdate
	
	listwallpaper = returnwallpaper()
	removeUnwantedPhotos(listwallpaper)
	listwallpaper = returnwallpaper()
	WallpaperCount = len(listwallpaper)
	
	setwallpaper(listwallpaper,count)
	count += 1

	#24 hour loop
	while timerDownload:
		#1 Minute Loop
	    while timerupdate:
	        time.sleep(1)
	        timerupdate -= 1
	    print("End of 15 Minutes, Wallpaper changed!")
	    
	    if(count>=WallpaperCount):
	    	count = 0

	    setwallpaper(listwallpaper,count)	
	    count += 1	

	    timerupdate = stu	
	    timerDownload = timerDownload - stu

	dCount = download()
	return dCount


#Function to fetch preferences from file
def fetchPreferences():
	Preferences = list()
	pref = open("WpPreferences.txt","r")
	for word in pref.read().split():
		Preferences.append(int(word))
	return Preferences

#Function to the Index of Latest downloaded Wallpaper
def saveToPreferences(Preferences):
	for i in range(0,5):
		Preferences[i] = str(Preferences[i])
		Preferences[i] = Preferences[i] + "\n"
	with open('WpPreferences.txt', 'w') as file:
		file.writelines(Preferences)

#To download wallpapers automatically on first run
def firstTimeDownload(Preferences):
	if Preferences[3] == 0:
		print("Downloading for the first time!")
		dCount = download(0)
		Preferences[3] = 1
		Preferences[4] = dCount
	saveToPreferences(Preferences)
	return Preferences


def main():
	Preferences = fetchPreferences()
	Preferences = firstTimeDownload(Preferences)
	Preferences = fetchPreferences()

	timerDownload = Preferences[2] * 60 * 60
	timerupdate = Preferences[1] * 60


	while(1):
		count=0
		dCount = countdownDownload(timerDownload, timerupdate,count)
		Preferences[4] = dCount
		saveToPreferences(Preferences)

if __name__ == '__main__':

	user_choice = parse_args()
	if not user_choice:
		url = 'http://www.reddit.com/r/wallpaper.json'
	else:
		url = 'http://www.reddit.com/r/' + user_choice + '.json'
	main()