# API call business

print "hello world"

from pattern.web import Twitter

s = Twitter().stream('#fail')
for i in range(10):
	time.sleep(1) 
	s.update(bytes=1024)
	print s[-1].text if s else ''