#encoding: utf-8

# API call business
# API key bSJDOQnZGZxXHSpHjCTnh1Oxf


import time
import datetime
import codecs
from pattern.web import Twitter
from indicoio import sentiment as sent


def filename():
	time = datetime.datetime.now()
	fileSave = codecs.open( str(time) +'.txt','w','utf-8' )

filename()


fileSave = codecs.open('tweets.txt','w','utf-8')

def search():

	query = str(raw_input("enter search query: "))
	# username = str(raw_input("enter username: "))

	t = Twitter()
	i = None
	for j in range(1):
		for tweet in t.search(query, start = i, count = 1):
			# print "text: " + tweet.text

			test = sent(tweet.text)
			print test
			print

search()


# def stream():
# 	print "hello world"

# 	from pattern.web import Twitter

# 	s = Twitter().stream('#fail')
# 	for i in range(10):
# 		time.sleep(1) 
# 		s.update(bytes=1024)
# 		print s[-1].text if s else ''

# stream()