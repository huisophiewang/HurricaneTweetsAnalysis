import os

def process(mmdd, hh):
    txt_input =os.path.join('search_matthew','2016%s' % mmdd, '2016%s_%s.txt' % (mmdd, hh))
    fr = open(txt_input)  
    
    count = 0
    for line in fr.readlines():
        txt = line[20:]
        if "Pat McCrory" in txt:
        #if "Nikki Haley" in txt:
            count += 1
            #print line.strip('\n')
    #print count
    return count

if __name__ == '__main__':
    dates = ['0929', '0930', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010']
    #dates = ['1016']
    dates = ['0929', '0930', '1001', '1002', '1003', '1004', 
             '1005', '1006', '1007', '1008', '1009', '1010',
             '1011', '1012', '1013', '1014', '1015', '1016']
    for dt in dates:
        print "========"
        print dt[:2] + '/' + dt[-2:]
        hrs = ['%02d' % h for h in range(24)]
        #hrs = ['00']
        daily_count = 0
        for hr in hrs:
            daily_count += process(dt, hr)
        print daily_count