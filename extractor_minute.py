'''
counter, timestamp, url, flag
929843609 1190146244.183 http://en.wikipedia.org/wiki/Image:M60_101st_Airborne_Division_Exercise_1972.jpg -
'''

import sys
import os
from datetime import datetime


def get_key(ts):
    time = datetime.fromtimestamp(ts)
    return time.strftime('%H:%M')



def get_os_file_name(file_name):
    #file_loc = os.path.normpath(os.path.join(os.path.dirname(__file__),file_name))
    #path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
    #file_loc = os.path.join(path,file_name)
    return file_name


# time = datetime.fromtimestamp(1190146244.183)
# time.strftime('%Y-%m-%d %H:%M:%S')
# print time.strftime('%H:%M')



def main(file_name):

    data = {}
    #create the keys

    total_views = 0
    total_bytes = 0
    #get location
    file_name = get_os_file_name(file_name)
    #open the file
    with open(file_name,'r') as f:
        for line in f:
            counter, ts, url, flag = line.split(' ')
            print ts
            key = get_key(float(ts))
            if key in data:
                data[key] += 1
            else:
                data[key] = 1

    # write to file
    with open("histogram.csv",'w')as fw:
        for key,value in data:
            fw.write("{},{}".format(key,value))


    #write to file







if __name__=="__main__":
    if len(sys.argv)<=1:
        print "python extractor_minute.py input_file_name"
        sys.exit()
    #print sys.argv
    main(sys.argv[1])