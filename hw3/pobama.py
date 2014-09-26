#encoding: utf-8

# API call business
# API key bSJDOQnZGZxXHSpHjCTnh1Oxf


import time
import datetime
import codecs
from pattern.web import Twitter
from indicoio import sentiment as sent

time = str(datetime.datetime.now())
timeClipped = time[0:19]
fileSave = codecs.open( str(timeClipped) +'.txt','w','utf-8' )


def search():

	query = str(raw_input("enter search query: "))
	# username = str(raw_input("enter username: "))

	t = Twitter()
	i = None
	for j in range(1):
		for tweet in t.search(query, start = i, count = 10):
			# print "text: " + tweet.text

			test = str(sent(tweet.text)) + "\n"
			print test

			fileSave.write(test)

search()