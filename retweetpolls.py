import tweepy

# read in keys.py file
from keys import Consumer_API_key, Consumer_API_secret_key, Access_token, Access_secret
 
# Authenticate to Twitter
auth = tweepy.OAuthHandler(Consumer_API_key, Consumer_API_secret_key)
auth.set_access_token(Access_token, Access_secret)

# Create API object
api = tweepy.API(auth)
'''
# To test access to Twitter
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
api.update_status("This is an API access test tweet.")
'''
# Search for all poll objects within the past 16 hours and retweet them 
# (you can change this timeframe to whatever suits you)
# if you only want the most recent poll object, put a 1 in the items() argument
# code taken from https://github.com/0xGrimnir/Simple-Retweet-Bot/blob/master/retweet.py
for poll in tweepy.Cursor(api.search, q='from:tamalefencer within_time:16h card_name:poll2choice_text_only OR card_name:poll3choice_text_only OR card_name:poll4choice_text_only').items():
	try:
		print('Attempting to retweet.')
		poll.retweet()
		print('Successfully retweeted.')

	except tweepy.TweepError as error:
		print('Error. Retweet not successful. Reason: ')
		print(error.reason)

	except StopIteration:
		break

