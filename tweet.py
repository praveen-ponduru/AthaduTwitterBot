import tweepy
import os
from datetime import date

consumer_key = os.environ('API_KEY')
consumer_secret = os.environ('API_KEY_SECRET')
access_token = os.environ('ACCESS_TOKEN')
access_token_secret = os.environ('ACCESS_TOKEN_SECRET')

client = tweepy.Client(consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret)

# Function to send the tweet
def tweet_countdown():
    today = date.today()

    # Only tweet if today is before the release date
    if today <= release_date:
        days_left = (release_date - today).days
        tweet = "JAI BABU"
        #tweet = f"{days_left} days left until the release!"
        api.update_status(status=tweet)
        print("Tweeted:", tweet)
    else:
        print("No more tweets. The release date has passed.")

# Call the function
tweet_countdown()

# Path to the image on your device
#image_path = 'path_to_your_image.jpg'

# Post the tweet with the image
#pi.update_status_with_media(status=tweet, filename=image_path)