import re
import os
import string
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk import bigrams
from pprint import pprint

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    #emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    #r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[\w][\w'\-_]+[\w])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 

def tokenize(s, lowercase=False):
    tokens = tokens_re.findall(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

def get_freq(fps):
    count_all = Counter()
    stop_terms = stopwords.words('english') + list(string.punctuation)
    # use lower case
    stop_terms += ['rt', 'in', 'matthew', 'hurricane', '#matthew', '#hurricane', '#hurricanematthew']
    re_remove_front = re.compile(r'^@\S+: ')
    terms_filtered = []
    for fp in fps:
        #fp = os.path.join("search_matthew", "20160929", file)
        fr = open(fp)
        for line in fr.readlines():
            line = re_remove_front.sub('', line[20:])
            # retweets has this field "retweeted_status", the official way to recognize retweet
            # it's easier and probabaly safe to filter using "RT @"
#             if 'evacuation' in line and not line.startswith('RT'):
#                 print line
            terms = tokenize(line)
            for term in terms:
                if term.lower() not in stop_terms:
                    terms_filtered.append(term)


    # bigram frequency
#     bigram_fd = nltk.FreqDist(nltk.bigrams(terms_filtered))
#     pprint(bigram_fd.most_common(50))
#     bigram_fd.plot(50)
    
    count_all.update(terms_filtered)
#     terms_sorted = sorted(count_all.items(), key=lambda x: x[1], reverse=True)
#     for term in terms_sorted:
#         if term[1] > 1:
#             print term

    pprint(count_all.most_common(200))
    
def get_freq_by_day(dt):
    
    folder = os.path.join("search_matthew", "2016%s" % dt)
    evening = ['2016%s_%02d.txt' % (dt, hr) for hr in range(8)]
    morning = ['2016%s_%02d.txt' % (dt, hr) for hr in range(8, 16)]
    afternoon = ['2016%s_%02d.txt' % (dt, hr) for hr in range(16, 24)]
    day = [afternoon]
    for period in day:
        fps = [os.path.join(folder, file) for file in period]
        #print fps
        get_freq(fps)
        
if __name__ == '__main__':
    #tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
    #print(preprocess(tweet))
       
#     tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
#     tweet = r"RT @weatherchannel: An 89-mph wind gust t-s was reported on Martinique in the Windward Islands earlier this evening from #Matthew. More: "
#     pprint(preprocess(tweet))

    dates = ['0929', '0930', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010']
    dates = ['1004']
    for dt in dates:
        print dt
        get_freq_by_day(dt)

    
    



