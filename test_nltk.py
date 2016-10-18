import re
import os
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk import bigrams
from pprint import pprint


re_remove_front = re.compile(r'^@\S+: ')

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

def main():
    count_all = Counter()
    stop_terms = stopwords.words('english') + list(string.punctuation)
    # use lower case
    stop_terms += ['rt', 'in', 'matthew', 'hurricane', '#matthew']
    dt = '0929'
    fp = os.path.join("search_matthew", "20160929", "20160929_00.txt")
    fr = open(fp)
    for line in fr.readlines():
        line = re_remove_front.sub('', line[20:])
        #print line
        terms = preprocess(line)
        terms_filtered = [term for term in terms if term.lower() not in stop_terms]
        count_all.update(terms_filtered)
    pprint(count_all.most_common(20))

if __name__ == '__main__':
    #tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
    #print(preprocess(tweet))
    
    main()
    
    



