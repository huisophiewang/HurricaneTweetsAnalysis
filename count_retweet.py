import os
import json
from pprint import pprint

def get_all_retweet():
    id_count = {}
    dates = ['0929', '0930', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010', '1011']
    #dates = ['0929']
    for dt in dates:
        hrs = ['%02d' % h for h in range(24)]
        #hrs = ['00']
        for hr in hrs:
            json_input =os.path.join('search_matthew','2016%s' % dt, '2016%s_%s.json' % (dt, hr))
            fr = open(json_input)  
            for line in fr.readlines():
                #print '=========================='
                json_dict = json.loads(line)
                #pprint(json_dict)
                if 'retweeted_status' in json_dict:
                    txt = json_dict['text'].encode('ascii','ignore')
                    #print txt
                    rt_id = json_dict['retweeted_status']['id']
                    ct = json_dict['retweet_count']
                    if ct < 100:
                        continue
                    if not rt_id in id_count:
                        id_count[rt_id] = [ct,txt]
                    else:
                        if id_count[rt_id] > ct:
                            #print 'yes'
                            id_count[rt_id] = (ct,txt)
    
    #high_rt = {v for k, v in id_count.iteritems() if v[0] > 100}
    res = sorted(id_count.items(), key=lambda x: x[1][0], reverse=True)
    #pprint(res)

    fw = open('rt_count.txt','a')
    for id, info in res:
        fw.write(str(info[0]) + ', ' + info[1] + '\n')
    fw.close()


    
if __name__ == '__main__':
    get_all_retweet()
