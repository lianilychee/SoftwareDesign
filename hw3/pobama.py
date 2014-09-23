# API call business
# API key bSJDOQnZGZxXHSpHjCTnh1Oxf

import time
from pattern.web import Twitter
from pattern.en import sentiment

query = str(raw_input("enter search query: "))
# username = str(raw_input("enter username: "))

def search(query):

	t = Twitter()
	i = None
	for j in range(1):
		for tweet in t.search(query, start = i, count = 1):
			# print tweet
			# print "author: " + tweet.author
			print "text: " + tweet.text
			# print "date: " + tweet.date
			# i = tweet.id

	test = sentiment (tweet.text)
	print test
	print test[0]


search(query);


# def stream():
# 	print "hello world"

# 	from pattern.web import Twitter

# 	s = Twitter().stream('#fail')
# 	for i in range(10):
# 		time.sleep(1) 
# 		s.update(bytes=1024)
# 		print s[-1].text if s else ''

# stream()