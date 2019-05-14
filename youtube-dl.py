import console
import sys
import glob
import os
import photos
from youtube_dl import YoutubeDL
import itertools

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import driveFilePicker as dFP

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
#gauth.CommandLineAuth()

drive = GoogleDrive(gauth)


if len(sys.argv) != 2:
	raise IndexError('usage: %s url' % (sys.argv[0]))
url = sys.argv[1]
print('url: %s' % (url))

choices = (
	('Audio Only', 'wav/aac/m4a/mp3/bestaudio'),
	('Video Only', 'bestvideo'),
	('Default', 'bestvideo+bestaudio/best')
)
choice = console.alert('youtube-dl', 'Version to extract:',
	*(c[0] for c in choices))
format=choices[choice-1][1]


opts = {
	'format': format, 'playliststart': 1#, 'playlistend': 31
}#you can add other options.  See youtube-dl on github or .org

with YoutubeDL(opts) as ydl:
	ydl.download([url])
	
pythonFiles=list(itertools.chain.from_iterable(glob.glob(e) for e in [
'*.py', '*.md', '*.yaml', '*.json', 'someFile.txt'
#add extensions or files in this directory you don't want to upload to Drive
])) 

files=glob.glob('*')
numOfFiles=len(files)-len(pythonFiles)

print('Downloaded: '+str(numOfFiles)+' files')
dirId = dFP.pick(drive)

for file in files:
	if file in pythonFiles:
		continue
	if not file:
		raise IndexError('downloaded file not found')
	try:
		#upload to authenticated Google Drive instance (whipload@gmail.com)
		driveFile = drive.CreateFile({'title': os.path.basename(file), "parents": [{"kind": "drive#fileLink","id": dirId}] })  # Create GoogleDriveFile instance
		driveFile.SetContentFile(file) # Set content of the drive file from the file
		driveFile.Upload()	
	
	finally:
		os.remove(file)#remove file from Pythonista directory

#console info:	
dir=drive.CreateFile({'id': dirId}) 
dirTitle= dir['title']
if dirId=='root':
	dirTitle='root'
print(str(numOfFiles)+' files saved to '+dirTitle+' folder in Google Drive')
