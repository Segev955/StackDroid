import csv
import hashlib
import os
import random
import sys
import hashlib
# Define folder where the log files are located
source_folder = 'drebin/samples/'
dest_folder = 'drebin'

# List of all the files
# dataset = [x for x in os.listdir(source_folder) if x.endswith(".apk")]
def rnd_mal_ben():
    if(random.random()>0.5):
        return "mal"
    return "ben"

def makeCsv(l,folder,csvname):
    f = open(f'{folder}/{csvname}', 'w',newline='')
    writer = csv.writer(f)
    print(l)
    writer.writerows(l)
    print(writer)
    f.close()

def csvnames(csvname):
    l = []
    datamal= [x for x in os.listdir("mal")]
    databen = [x for x in os.listdir("ben")]
    for x in datamal:
        l.append([x,1])
    for x in databen:
        l.append([x,0])

    makeCsv(l,dest_folder,csvname)


if __name__ == '__main__':

    csvnames('malben.csv')
    print(f"csvsaved.")
