import tweepy
import csv

####input your credentials here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

#creating an OAuthHandler instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#If your app creater in twitter developer has a callback, uncomment below line
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret,callback_url)

auth.set_access_token(access_token, access_token_secret)
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# Open/Create a file to append data
csvFile = open(r'C:\Users\goura\OneDrive\Desktop\MaharanaJayanti.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
#search for hashtags in a tweet
for tweet in tweepy.Cursor(api.search,q="#handwara_encounter",count=20,
                           lang="en",
                           since="2017-05-12").items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])


