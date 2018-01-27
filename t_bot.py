# dependencies python-twitter google-api-python-client

from __future__ import print_function

import twitter


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

CONSUMER_KEY = login_info.readline().rstrip("\r").rstrip("\n")
CONSUMER_SEC = login_info.readline().rstrip("\r").rstrip("\n")
ACCESS_TOK = login_info.readline().rstrip("\r").rstrip("\n")
ACCESS_SEC = login_info.readline().rstrip("\r").rstrip("\n")

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SEC,
                  access_token_key=ACCESS_TOK,
                  access_token_secret=ACCESS_SEC)

# get file from drive

message = "test"

status = api.PostUpdate(message)

print(status)
