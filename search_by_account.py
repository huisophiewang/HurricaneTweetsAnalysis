import tweepy
from pprint import pprint
import json
import time
import os
import logging
import datetime
  
#Variables that contains the user credentials to access Twitter API 
access_token = "84530015-pBpdPD8QCsJksYTosHvIjicAtAC8t8FhVdxGreCt7"
access_token_secret = "JGZ4KNFiqPtYm1E5wAlXLMhzpqtA49Dk4ucXeYZ256PT5"
consumer_key = "uGR6NQOLUIXmzSSuJFSFhbY3i"
consumer_secret = "AeRZnA0ziRlNYSSQIjLyh84uObw9b2iiTghDPZukIwhjwsbH1H"

logging.basicConfig(filename='search_by_account.log',level=logging.INFO, format='%(asctime)s %(message)s')
dir = "search_gov_account"

def query_api(api, account, date, max_id=None):
    # max count allowed is 100
    since_dt = datetime.datetime.strptime(date, "%Y%m%d").date()
    until_dt = since_dt + datetime.timedelta(days=1)
    q_str = r'from:%s since:%s until:%s' % (account, since_dt, until_dt)
    #q_str = r'from:NHC_Atlantic since:2016-09-29'
    
    if not max_id:
        tweets = api.search(q_str, count=100, include_entities=True)
    else:
        tweets = api.search(q_str, count=100, max_id=max_id, include_entities=True)    
    return tweets

def write_to_json(tweets):  
    for tweet in tweets:
        #print json.dumps(tweet._json, indent=4, sort_keys=True)
        print '%s %d' % (tweet._json['created_at'], tweet._json['id'])
        crt = tweet._json['created_at']
        year = crt[-4:]
        month = "%02d" % time.strptime(crt[4:7],'%b').tm_mon
        date = crt[8:10]
        #hour = crt[11:13]
        account_name = tweet._json['user']['screen_name']
        file_name = year + month + date + '.json'

        f_out = open(os.path.join(dir, account_name, file_name), 'a')
        # json dumps returns a string, json dump write to file
        to_str = json.dumps(tweet._json, f_out, sort_keys=False)
        #json.dump(tweet._json, f_out, sort_keys=False)
        f_out.write(to_str + '\n')
        f_out.close()

def search(account, dt): 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
        tweets = query_api(api, account, dt)
        write_to_json(tweets)
    except tweepy.error.TweepError:
        logging.exception("search error") 
        print 'waiting...'
        time.sleep(15 * 60)
    except Exception as e:
        logging.exception("other error")     
    

            
if __name__ == '__main__':    
    # national hurricane center  
    NHC = ['NWS', 'NWSNHC', 'NHC_Atlantic', 'NOOA']
    # federal emergency management
    FED = ['fema', 'DHSgov', 'RedCross']
    # states: Florida, Georgia, South Carolina
    FL = ['FLSERT', 'FLHSMV', 'FloridaStorms', 'VolunteerFla']
    GA = ['GeorgiaEMA']
    SC = ['SCEMD']

    accounts = NHC + FED + FL + GA + SC
    #dates = ['20160928', '20160929', '20160930']
    dates = ['20161001', '20161002', '20161003', '20161004'] 
    
    for account in accounts:
        path = os.path.join(dir, account) 
        if not os.path.exists(path):
            os.makedirs(path)
        for dt in dates:
            search(account, dt)