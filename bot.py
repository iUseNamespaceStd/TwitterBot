import tweepy

#INSERT TOKENS TO IDENTIFY ACCOUNT
consumer_key = ' '
consumer_secret = ' '
key = ' '
secret = ' '

FILE_NAME = 'tweets_id.txt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def read_last_seen(FILE_NAME):
	file_read = open(FILE_NAME, 'r')
	last_seen_id = int(file_read.read().strip())
	file_read.close()
	return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
	file_write = open(FILE_NAME, 'w')
	file_write.write(str(last_seen_id))
	file_write.close()
	return

def reply():
	tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')
	for tweet in tweets:
		if '#notarobot' in tweet.full_text.lower():
			print(str(tweet.id) + ' - ' + tweet.full_text)
			api.update_status("@" + tweet.user.screen_name + " Hello human ", tweet.id)
			api.retweet(tweet.id)
			api.create_favorite(tweet.id)
			store_last_seen(FILE_NAME, tweet.id)

while True:
	reply()
	