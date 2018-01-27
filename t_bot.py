# dependencies python-twitter dropbox

from __future__ import print_function

import twitter
import dropbox
import random



CONSUMER_KEY = ""
CONSUMER_SEC = ""
ACCESS_TOK = ""
ACCESS_SEC = ""
login_info = None


# get login info from file
try:
    login_info = open("login_info.txt","r")
except IOError:
    print("Could not open login information")

login_str = login_info.read()

for c in ['\n','\r',' ']:
    login_str = login_str.replace(c, '')

CONSUMER_KEY, CONSUMER_SEC, ACCESS_TOK, ACCESS_SEC, DROPBOX_KEY, DROPBOX_SEC, DROPBOX_TOK = login_str.split(',')

login_info.close()

# Get twitter connection
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SEC,
                  access_token_key=ACCESS_TOK,
                  access_token_secret=ACCESS_SEC)

# get file from dropbox

dbx = dropbox.Dropbox(DROPBOX_TOK)

def getImage():
    files = dbx.files_list_folder("").entries
    # grab a random file
    choice = files[random.randint(0,len(files)-1)]

    dbx.files_download_to_file("img.jpg", '/' + choice.name)






def postMessage():
    with open("img.jpg", "rb") as f:
        message = "test"
        status = api.PostUpdate(message, media=f)


getImage()
postMessage()


