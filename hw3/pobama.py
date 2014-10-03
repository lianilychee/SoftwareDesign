#encoding: utf-8

import time
import datetime
import codecs
from pattern.web import Twitter
import tweetpony
from common import get_api
from indicoio import sentiment as sent

# Twitter API keys
consumer_key = 'zOWZuCJyqFw26egZTrY0ZL32G'
consumer_secret = '7pPxVemHiEzarzPqwUEZrnNpUPk9mWRvmIiBGXtyQtcdI6i0UG'
access_token = '2508360470-zhIFODzznC0PdcAEa0oS6sY6p3Y9Wc8K1e6ZalO'
access_token_secret = 'Ahx7aUjNcPaT6zBE8FfbVMAiilSh1fDM9g0Zhv9bPnHSE'
api = tweetpony.API(consumer_key, consumer_secret, access_token, access_token_secret)

user = api.user

# Log file definition
time = str(datetime.datetime.now())
timeClipped = time[0:19]
fileSave = codecs.open( str(timeClipped) +'.txt','w','utf-8' )

# Pull down author follower count.
def findFollows(author):
	'''

	'''
	api = get_api()
	if not api:
		return
	username = author
	if username == "":
		username = api.user.screen_name
	try:
		user = api.get_user(screen_name = username)
	except tweetpony.APIError as err:
		print "Twitter returned error #%i: %s" % (err.code, err.description)
	else:
		follows = user.followers_count
		return follows


#  Pull down tweets and generate sentiment.
def search():

	query = str(raw_input("enter search query: "))
	t = Twitter()
	# i = None
	chances = 0
	fileSave.write(query + "\n")

	allChances = 0
	for tweet in t.search(query, start = None, count = 5):
		
		print tweet.text

		# Calc tweet sentiment
		sent_int = sent(tweet.text)
		sent_str = str(sent_int)
		# print sent_str

		# Calc author's follower count
		follows_int = findFollows(tweet.author)
		follows_str = str(sent_int)
		# print follows_str

		# Calc chances; make cumulative
		chances = follows_int * sent_int
		print str(chances) + "\n"

		# File save
		save = sent_str + "\n" + follows_str + "\n \n"
		fileSave.write(save)

		allChances = allChances + chances

		print "OVERALL: " + str(allChances)

if __name__ == "__main__":
	search()
# print __name__