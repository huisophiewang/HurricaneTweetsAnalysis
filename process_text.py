import os
import json
import re
import string

regex = re.compile(r'http\S+')

def write_to_txt(mmdd,hh):
    json_input =os.path.join('search_matthew','2016%s' % mmdd, '2016%s_%s.json' % (mmdd, hh))
    #json_input = os.path.join('stream_data','2016%s_%s.json' % (mmdd, hh))
    fr = open(json_input)  
    
#     txt_output = os.path.join('2016%s' % mmdd, '2016%s_%s.txt' % (mmdd, hh))
#     #txt_output = os.path.join('stream_data', '2016%s_%s.txt' % (mmdd, hh))
#     fw = open(txt_output, 'a')
    count = 0
    total = 0
    for line in fr.readlines():
        if not line:
            continue
        total += 1
        json_dict = json.loads(line)
        txt = json_dict['text'].encode('ascii','ignore')
        txt = regex.sub('', txt)
        txt = string.replace(txt, '\n', ' ')
        user = json_dict['user']['screen_name']
        created_at = json_dict['created_at'][:-11]
        if (json_dict['place'] or json_dict['coordinates']) and ('evacuation' in txt or 'evacuate' in txt):
            count += 1
            print '-----------'
            print txt
            print json_dict['coordinates']
            print json_dict['user']['geo_enabled']
            print json_dict['place']
            
    print count   
    print total
    print float(count)/total     
        #outline = r'%s @%s: %s' % (created_at, user, txt)
        #print outline
#         fw.write(outline+ '\n')    
#     fr.close()
#     fw.close()

    
if __name__ == '__main__':
    #dates = ['1001', '1002', '1003', '1004', '1005']
    dates = ['1005']
    for dt in dates:
        hrs = ['%02d' % h for h in range(24)]
        hrs = ['23']
        for hr in hrs:
            write_to_txt(dt, hr)