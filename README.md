# iOS Youtube-DL to Google Drive
Adds a share extension to download youtube videos, soundcloud audio, etc and upload them to Google Drive

HOW TO USE:

1. You must have Pythonista installed.  If you don't, get it in the App Store (it's free, and great)
2. Download this project.  Import it to Pythonista.  

Pythonista automatically adds a share extension called Run Pythonista Script.  Tap that, then Import to Pythonista for each file.  Or use your own method.  NOTE: Most share extensions must be enabled when used the first time.  To do so, scroll right and tap More, then enable

3. Create a directory for the files (good organization). Say SAUSAGESareTHEbest
4. Now you need an Oauth Client ID for the script. Creating one is easy.  Go to Google API Console (in browser) and create a new project.  Then create an Oauth Client ID.  Google will want you to fill out the public user consent form.  Fill the necessary blanks with anything.  Don't request any special permissions. Tap the Download icon next to the client id.  Replace client_secrets.json in Pythonista with this file.  
5.  Add the Google Drive API to the Google project
6.  
