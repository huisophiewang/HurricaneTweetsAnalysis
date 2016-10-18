import json
import datetime

import re
# Lets create a pattern and extract some information with it
#regex = re.compile(r'http\S+')

# result = regex.search("Hello World is the easiest")
# if result:
#     print result.start(), result.end()
# 
# for result in regex.findall("Hello World, Bonjour World"):
#     print result

#print regex.sub(r"\1 Earth", "Hello World! Hello beautiful World!")
#print regex.sub(r"Earth", "This must b an April fools joke https://t.co/yxLbliw6Yw")

#print re.sub(r'http\S+', '', "This must b an April fools joke https://t.co/yxLbliw6Yw")
import nltk
nltk.download()

# from nltk.tokenize import word_tokenize
#  
# tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
# print(word_tokenize(tweet))
# ['RT', '@', 'marcobonzanini', ':', 'just', 'an', 'example', '!', ':', 'D', 'http', ':', '//example.com', '#', 'NLP']