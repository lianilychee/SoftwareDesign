#encoding: utf-8

# API call business
# API key bSJDOQnZGZxXHSpHjCTnh1Oxf


import time
import datetime
# import codecs
from pattern.web import Twitter
import tweetpony
from common import get_api
from indicoio import sentiment as sent

# Twitter API keys; user definition
consumer_key = 'zOWZuCJyqFw26egZTrY0ZL32G'
consumer_secret = '7pPxVemHiEzarzPqwUEZrnNpUPk9mWRvmIiBGXtyQtcdI6i0UG'
access_token = '2508360470-zhIFODzznC0PdcAEa0oS6sY6p3Y9Wc8K1e6ZalO'
access_token_secret = 'Ahx7aUjNcPaT6zBE8FfbVMAiilSh1fDM9g0Zhv9bPnHSE'
api = tweetpony.API(consumer_key, consumer_secret, access_token, access_token_secret)
user = api.user

# Log file definition
# time = str(datetime.datetime.now())
# timeClipped = time[0:19]
# fileSave = codecs.open( str(timeClipped) +'.txt','w','utf-8' )

# Pull down author follower count.
def findFollows(author):
	api = get_api()
	if not api:
		return
	username = author
	if username == "":
		username = api.user.screen_name
	try:
		user = api.get_user(screen_name = username)
	except tweetpony.APIError as err:
		print "Oh no! The user's profile could not be loaded. Twitter returned error #%i and said: %s" % (err.code, err.description)
	else:
		follows = user.followers_count
		return follows

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

			author = tweet.author
			print author
			print findFollows(author)

search()
