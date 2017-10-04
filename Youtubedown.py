import os
import urllib2
from pytube import YouTube
def download(url):
    yt = YouTube(url)
    print yt.filename
    print "Enter Downloaded File Name"
    new_filename=raw_input()
    yt.set_filename(new_filename)
    video = yt.filter('mp4')[-1]
    print "Downloading..."
    video.download(os.getcwd())
    print "Video Downloaded in",
    print os.getcwd()
    print "Done!!"
try:
    print "Enter Video Url:-"
    url=raw_input()
    try:
        download(url)
    except(ValueError):
        print "No such YouTube Video Exists"
        if(url.index('\"')==0 or url.index('\"')==-1):
            print "Try URL without Quotes"
except(urllib2.URLError):
    print "No Internet connection"
except(KeyboardInterrupt):
    print "Unusal Termination Video Not Downloaded"