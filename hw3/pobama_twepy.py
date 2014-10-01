import tweetpony
from common import get_api

consumer_key = 'zOWZuCJyqFw26egZTrY0ZL32G'
consumer_secret = '7pPxVemHiEzarzPqwUEZrnNpUPk9mWRvmIiBGXtyQtcdI6i0UG'
access_token = '2508360470-zhIFODzznC0PdcAEa0oS6sY6p3Y9Wc8K1e6ZalO'
access_token_secret = 'Ahx7aUjNcPaT6zBE8FfbVMAiilSh1fDM9g0Zhv9bPnHSE'

def main():
	api = get_api()
	if not api:
		return
	username = raw_input("Username to lookup (leave blank for your own): ").strip()
	if username == "":
		username = api.user.screen_name
	try:
		user = api.get_user(screen_name = username)
	except tweetpony.APIError as err:
		print "Oh no! The user's profile could not be loaded. Twitter returned error #%i and said: %s" % (err.code, err.description)
	else:
		return user.followers_count

if __name__ == "__main__":
	main()