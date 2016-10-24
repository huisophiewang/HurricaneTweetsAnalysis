import os
import json
import re
import string

regex = re.compile(r'http\S+')

def write_to_txt(mmdd,hh):
    json_input =os.path.join('search_matthew','2016%s' % mmdd, '2016%s_%s.json' % (mmdd, hh))
    fr = open(json_input)  
    
    txt_output = os.path.join('search_matthew','2016%s' % mmdd, '2016%s_%s.txt' % (mmdd, hh))
    #txt_output = "evacuation.txt"
    #txt_output = "stay.txt"
    fw = open(txt_output, 'a')
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
        
#         #if txt.startswith('RT @'):
#         if "retweeted_status" in json_dict:
#             continue
#         #if (json_dict['place'] or json_dict['coordinates']) and ('evacuation' in txt or 'evacuate' in txt):
#         #if 'evacuation' in txt or 'evacuate' in txt:
#         #if 'stay' in txt and not 'stay safe' in txt:
#         #if "Nikki Haley" in txt:
#         if "Pat McCrory" in txt:
#             outline = r'%s @%s: %s' % (created_at, user, txt)
#             print outline

        outline = r'%s @%s: %s' % (created_at, user, txt)
        print outline
        fw.write(outline + '\n')
    fr.close()
    fw.close()

    
if __name__ == '__main__':
    dates = ['0929', '0930', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010']
    dates = ['1013', '1014', '1015', '1016']
    for dt in dates:
        hrs = ['%02d' % h for h in range(24)]
        #hrs = ['00']
        for hr in hrs:
            write_to_txt(dt, hr)