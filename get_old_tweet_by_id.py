from TwitterAPI import TwitterAPI
import tweepy
import json

#Variables that contains the user credentials to access Twitter API 
access_token = "84530015-pBpdPD8QCsJksYTosHvIjicAtAC8t8FhVdxGreCt7"
access_token_secret = "JGZ4KNFiqPtYm1E5wAlXLMhzpqtA49Dk4ucXeYZ256PT5"
consumer_key = "uGR6NQOLUIXmzSSuJFSFhbY3i"
consumer_secret = "AeRZnA0ziRlNYSSQIjLyh84uObw9b2iiTghDPZukIwhjwsbH1H"

def method1(tweet_id):
    api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
    
    #r = api.request('statuses/show/:%d' % 210462857140252672)
    #r = api.request('statuses/show/:%d' % 782662364499935232)
    r = api.request('statuses/show/:%s' % tweet_id)
    print r.text
    print json.dumps(json.loads(r.text), indent=4, sort_keys=True)
    
def method2(tweet_id):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweet = api.get_status(tweet_id)
    print tweet
    print json.dumps(tweet._json, indent=4, sort_keys=True)
    #print(api.get_status('782662364499935232').text)
    #print api.get_direct_message('782662364499935232')
    
if __name__ == '__main__':
    id = '260259931658256385'
    #method1(id)
    method2(id)