# Here i am learning about API and how to handle API in local code using the library called "requests"
# requests allows your code to act like a web browser, communicating with websites and APIs to fetch or send data
# Requests is a popular library used to send HTTP requests to web servers

# API is application programming interface that is a set of rules and protocols that allows different software applications to communicate and exchange data with each other.

# we can access any data which is online and is in API form using requests library
# Here i am accessing the data of music bands from itunes APIs
import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Put band's name")

# this line accessing the Data using itunes API and sys.argv[1] is refering to the band name entered by user
req = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# here json() is used because this is a json() file data but in output because of python requests it will give us as pythonic syntax 
# print(req.json()) 


# the data potrait using "print(req.json())" can be very hard to understand and work with so python have another library to format those datas in a readale format
# "json" library is a lightweight data interchange format inspired by JavaScript object literal syntax (although it is not a strict subset of JavaScript). 

print(json.dumps(req.json(), indent = 2 )) # it only dumps the whole data to your face not in a clear way to see exact what you want to see


# by using loop can it can be access for particuler key and value to show them and only them, not others

songName = req.json()

# to use efficiently we gotta know the key name for sure then it will iterate through that key only
for songs in songName["results"]:
    print(songs["trackName"])