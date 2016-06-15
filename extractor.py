import sys
import os
# python extractor.py file_name


def get_os_file_name(file_name):
    file_loc = os.path.normpath(os.path.join(os.path.dirname(__file__),file_name))

    return file_loc



def main(file_name):

    total_views = 0
    total_bytes = 0
    #get location
    file_name = get_os_file_name(file_name)
    #open the file
    with open(file_name,'r') as f:
        for line in f:
            project_name, t_n, t_v, t_b = line.split(' ')
            total_views += int(t_v)
            total_bytes += int(t_b)


    print total_views, total_bytes

    #extract summary

    #write to file







if __name__=="__main__":
    if len(sys.argv)<=1:
        print "python extractor.py input_file_name"
        sys.exit()
    #print sys.argv
    main(sys.argv[1])