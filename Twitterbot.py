import tweepy
import time

consumer_key = 'your-consumer-key'
consumer_secret = 'your-consumer-secret'
access_token = 'your-access-token'
access_token_secret = 'your-access-token-secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def follow_back():
    for follower in tweepy.Cursor(api.get_followers).items():
        follower.follow()

def like_tweets():
    for tweet in tweepy.Cursor(api.search_tweets, q='keyword').items():
        if not tweet.favorited:
            tweet.favorite()

def schedule_tweets():
    while True:
        current_time = time.strftime('%H:%M')

        if current_time == '06:00':
            api.update_status('Good morning!')
        elif current_time == '12:00':
            api.update_status('It\'s noon!')
        elif current_time == '18:00':
            api.update_status('Good evening!')

        time.sleep(60)

def main():
    follow_back()
    like_tweets()
    schedule_tweets()

if __name__ == '__main__':
    main()