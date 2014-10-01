#encoding: utf-8

# API call business
# API key bSJDOQnZGZxXHSpHjCTnh1Oxf


import time
import datetime
# import codecs
from pattern.web import Twitter
from pattern.web import URL, plaintext
from indicoio import sentiment as sent

# time = str(datetime.datetime.now())
# timeClipped = time[0:19]
# fileSave = codecs.open( str(timeClipped) +'.txt','w','utf-8' )



#  Pull down tweets and generate sentiment.
def search():

	query = str(raw_input("enter search query: "))
	# username = str(raw_input("enter username: "))

	t = Twitter()
	i = None
	# fileSave.write(query + "\n")
	for j in range(1):
		for tweet in t.search(query, start = i, count = 1):
			# print "text: " + tweet.text
			saveSent = str(sent(tweet.text)) + "\n"
			# print saveSent

			# fileSave.write(saveSent)

			# print tweet.author

search()
followerCount()