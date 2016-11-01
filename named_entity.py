from nltk.tag import StanfordNERTagger
import os
import re
from pprint import pprint
from util import tokenize

os.environ["CLASSPATH"] = r"C:\Users\Sophie\Downloads\stanford-ner-2014-06-16"
os.environ["STANFORD_MODELS"] = r"C:\Users\Sophie\Downloads\stanford-ner-2014-06-16\classifiers"
os.environ["JAVA_HOME"] = r"C:\Program Files (x86)\Java\jre1.8.0_60\bin"

st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz') 
re_remove_front = re.compile(r'^@\S+: ')

        
# tokenized_sents = [[word_tokenize(sent) for sent in sent_tokenize(filecontent)] for filename in filelist]
# st.tag_sents(tokenized_sents)


def test():
    mmdd = '1004'
    hh = '10'
    txt_input =os.path.join('search_matthew','2016%s' % mmdd, '2016%s_%s.txt' % (mmdd, hh))
    fr = open(txt_input)  
    
    tokenized_batch = []
    for line in fr.readlines():
        txt = re_remove_front.sub('', line[20:]).lower() 
        tokenized_batch.append(tokenize(txt))
    tags_batch = st.tag_sents(tokenized_batch)
    #pprint(tags_batch)

    all_locs_freq = {}
    for i, tags in enumerate(tags_batch):
        line_locs = []
        for j, (term, tag) in enumerate(tags):
            if tag == 'LOCATION':
                if j>0 and tags[j-1][1] == 'LOCATION':
                    line_locs[-1].append(term)
                else:
                    line_locs.append([term])
        if line_locs:
            print i
            print line_locs
            
        for line_loc in line_locs:
            loc = ' '.join(line_loc)
            if loc in all_locs_freq:
                all_locs_freq[loc] += 1
            else:
                all_locs_freq[loc] = 1
        
    freq_sorted = sorted(all_locs_freq.items(), key=lambda x: x[1], reverse=True)
    pprint(freq_sorted)
                

    
    #print idx
#     fr = open(txt_input) 
#     for i, line in enumerate(fr.readlines()):
#         if i in idx:
#             txt = re_remove_front.sub('', line[20:]).lower() 
#             print i
#             print txt.strip('\n')
        
                

            
if __name__ == "__main__":
    test()