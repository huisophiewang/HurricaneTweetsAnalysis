import tweepy
import json
import time
import os
import datetime

access_token = "84530015-pBpdPD8QCsJksYTosHvIjicAtAC8t8FhVdxGreCt7"
access_token_secret = "JGZ4KNFiqPtYm1E5wAlXLMhzpqtA49Dk4ucXeYZ256PT5"
consumer_key = "uGR6NQOLUIXmzSSuJFSFhbY3i"
consumer_secret = "AeRZnA0ziRlNYSSQIjLyh84uObw9b2iiTghDPZukIwhjwsbH1H"

dir = 'search_test'

def query_api_test(api, max_id=None):
    # national hurricane center
    NHC = ['NWS', 'NWSNHC', 'NHC_Atlantic']
    # state emergency management Florida
    FLEMD = ['fema','FLSERT', 'FloridaStorms']
    # other EMD
    EMD = ['GeorgiaEMA','SCEMD']
    q_str = r'from:NWS since:2016-09-29 until:2016-09-30' 
    #q_str = r'HurricaneMatthew OR "Hurricane Matthew" until:2016-09-29' 
    
    if not max_id:
        tweets = api.search(q_str, count=100, include_entities=True)
    else:
        tweets = api.search(q_str, count=100, max_id=max_id, include_entities=True
                            )      
    return tweets

# one cursor call generates multiple api.search calls
def query_by_cursor(api, max_id=None):
    if not max_id:
        tweets = tweepy.Cursor(api.search,
                               q=r'HurricaneMatthew OR "Hurricane Matthew" since:2016-09-29 until:2016-09-30',
                               count=100,
                               include_entities=True).items()
    else:
        tweets = tweepy.Cursor(api.search,
                               q=r'HurricaneMatthew OR "Hurricane Matthew" since:2016-09-29 until:2016-09-30',
                               count=100,
                               max_id = max_id,
                               include_entities=True).items()        
    return tweets


            
def test():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    tweets = query_api_test(api)
    print len(tweets)
    for tweet in tweets:
        #print json.dumps(tweet._json, indent=4, sort_keys=True)
        print '%s %d %s' % (tweet._json['created_at'], tweet._json['id'], tweet._json['text'].encode('ascii', 'ignore'))
    
if __name__ == '__main__':
    test()