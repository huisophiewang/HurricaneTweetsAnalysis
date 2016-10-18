#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import os
import time

#Variables that contains the user credentials to access Twitter API 
access_token = "84530015-pBpdPD8QCsJksYTosHvIjicAtAC8t8FhVdxGreCt7"
access_token_secret = "JGZ4KNFiqPtYm1E5wAlXLMhzpqtA49Dk4ucXeYZ256PT5"
consumer_key = "uGR6NQOLUIXmzSSuJFSFhbY3i"
consumer_secret = "AeRZnA0ziRlNYSSQIjLyh84uObw9b2iiTghDPZukIwhjwsbH1H"

fp_out = 'test_re.json'
fp_err = 'HurricaneMatthew_error.txt'
class MyListener(StreamListener):

    def on_data(self, data):
        try:
            decoded = json.loads(data)
            print json.dumps(decoded, indent=4, sort_keys=True)
            crt = decoded['created_at']
            year = crt[-4:]
            month = "%02d" % time.strptime(crt[4:7],'%b').tm_mon
            date = crt[8:10]
            hour = crt[11:13]
            file_name = year + month + date + '_' + hour + '.json'
            print file_name
            
            #print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
            f_out = open(file_name, 'a')
            f_out.write(data)
            f_out.close()
        except Exception as e:
            f_err = open(fp_err, 'a')
            f_err.write("Data Error: %s" % str(e))
            f_err.close()
        return True

    def on_error(self, status):
        f_err = open(fp_err, 'a')
        f_err.write("Listener Error: %s" % str(status))
        f_err.close()
        return True
    
def write_to_json():
    #This handles Twitter authetification and the connection to Twitter Streaming API
    listener = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)
    stream.filter(track=['HurricaneMatthew'])
    
        
if __name__ == '__main__':

    #write_to_json()



    