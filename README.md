[![Underdevelopment](https://img.shields.io/badge/Build-UnderDevelopment-red.svg)](https://raw.githubusercontent.com/hyperium/hyper/master/LICENSE)  [![Passing](https://img.shields.io/circleci/project/github/RedSparr0w/node-csgo-parser/master.svg)](https://raw.githubusercontent.com/hyperium/hyper/master/LICENSE)

# Wallpapers from /r/wallpaper:

This Script will download all the Images (First page of hot section) from /r/Wallpaper subreddit to a local folder every 24 hours.
It will also automate a Slideshow change of Wallpapers from that local storage. Wallpaper will change every 30 Minutes.
This works only on Gnome Based Desktops.

### Libraries Required:
glob, urllib2, json, getpass
```shell
sudo pip install glob urllib2 json getpass
```
### To Install
```shell
git clone https://github.com/tsarjak/WallpapersFromReddit.git
```


### To run the code
In terminal:
```shell
#In Home Directory or the Directory in which you cloned/downloaded/installed the script
cd ~/WallpapersFromReddit
python wallpaper.py --subreddit <your choice of subreddit> 
```
#### Example : 
```shell
python wallpaper.py --subreddit earthporn
```
#### --Subreddit part is optional - By default it will fetch images from /r/wallpaper
#### You can see the progress of the download after above execution

### After First run, you might want to run the app in background (This is possible even on first run!)

```shell
nohup python wallpaper.py &
```
##### nohup command is used to keep the script running in background, even when the terminal is closed

### Add the script to run it as startup application

##### Goto "Startup Applications"
##### Click "Add" -> Click "Custom Command" -> Enter command as "nohup python ~/wallpaper.py &", enter name and other details and save


#### Custom Preferences and more Subreddits comming soon! :)
