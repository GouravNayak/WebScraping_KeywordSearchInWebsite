import searchtweets
import json
import csv


from searchtweets import collect_results
urlfilterString = "twitter.com"
premium_search_args = searchtweets.load_credentials(filename ="twittercredentials.yaml",
                              yaml_key = "search_tweets_api_premium_30days_gourav",
                              env_overwrite = False)

#for building queries: https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/premium-operators'
query = ' '
query = query + str("#QuarantineLife OR #QuarantineRoutine OR #FamilyQuarantine")
query = query + str(" OR My Quarantine Routine OR ")
query = query + str("\"My Quarantine Routine!\"")
#query = query + str(" -(Like Follow)")
#query = query + str(" -meme ")

query = query + str(" lang:en")
rule = searchtweets.gen_rule_payload(query,
                                     from_date="2020-06-01",  # Feb 1
                                     to_date="2020-06-22",  #15June
                                     results_per_call=100)
print(rule)

tweets = collect_results(rule, max_results=500, result_stream_args=premium_search_args)

#removing duplicate tweets
unique_tweets = {each['text']: each for each in tweets}.values()
print(len(unique_tweets))
with open(r'C:\Users\goura\OneDrive\Documents\COVID Gamification\TwitterData\premiumtwitterresults_June.csv', 'w', encoding="utf-8") as csvfile:
    csvWriter = csv.writer(csvfile)

    for tweet in unique_tweets:
        if('extended_tweet' in tweet and 'entities' in tweet and len(tweet['entities']['urls'])>0):
            if("twitter.com" in tweet['entities']['urls'][0]['expanded_url']):
                csvWriter.writerow([tweet['created_at'], tweet['extended_tweet']['full_text'].encode(errors='ignore').decode('utf-8'),
                                    tweet['user']['screen_name'],
                                    tweet['entities']['urls'][0]['expanded_url']])


print(json.dumps(tweets, indent=2))