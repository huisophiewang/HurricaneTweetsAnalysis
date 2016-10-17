import os
import json
from pprint import pprint
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import re
import pylab
import random

regex = re.compile(r'http\S+')

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    color = "hsl(0, 0%%, %d%%)" % random.randint(100, 100)
    return color
    

def word_cloud(mmdd, hh):
    #json_fp =os.path.join('2016%s' % mmdd, '2016%s_%s.json' % (mmdd, hh))
    json_fp =os.path.join('stream_data','2016%s_%s.json' % (mmdd, hh))
    
    #fp = 'test.json'
    fr = open(json_fp)  
    tweet_txt = []
    for line in fr.readlines():
        if not line:
            continue
        org_txt = json.loads(line)['text'].encode('ascii','ignore')
        processed = regex.sub('', org_txt)
        tweet_txt.append(processed)
    text_str = '\n'.join(tweet_txt)
    #print text_str
#     txt_output = os.path.join('2016%s' % mmdd, '2016%s_%s.txt' % (mmdd, hh))
#     fw = open(txt_output, 'a')
#     fw.write(text_str)
    
    words_list = ["RT", "Matthew", "Hurricane", "HurricaneMatthew"]
    ### stop words should be lowercase!!!
    remove_words = set([w.lower() for w in words_list])
    remove_words.update(set(STOPWORDS))
    wc = WordCloud(stopwords=remove_words, random_state=0) # default size 400x200
    wc.generate(text_str)
     
    #plt.imshow(wc)
    ### scale canvas, default size [8.0, 6.0]
    #plt.rcParams["figure.figsize"] = [18.0, 12.0]
    plt.imshow(wc.recolor(color_func=grey_color_func, random_state=None))
    plt.axis("off")
    plt.savefig(os.path.join('word_clouds', '2016%s' % mmdd, '2016%s_%s.jpg' % (mmdd, hh)))
    #plt.show()

    
    
if __name__ == '__main__':
    dates = ['1009', '1010']
    for dt in dates:
        output_dir = os.path.join('word_clouds', '2016%s' % dt)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        hrs = ['%02d' % h for h in range(24)]
        #hrs = ['00']
        for hr in hrs:
            word_cloud(dt, hr)


