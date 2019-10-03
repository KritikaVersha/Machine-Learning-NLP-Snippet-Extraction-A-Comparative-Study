import os
import csv
import bz2
from bz2 import decompress
#from bs4 import BeautifulSoup
import  tarfile
from xml.etree import cElementTree as ET
import json,time,urllib
#import nltk


#################### Extracting and Cleaning the Document File
document_list=[]
count=1;
filepath = "C:/TEMP/kmversha/Desktop/fdocuments"
for data_file in (os.listdir(filepath)):
    for urls in (os.listdir("C:/TEMP/kmversha/Desktop/fdocuments/"+data_file)):
        #document_list.append("C:/TEMP/kmversha/Desktop/fdocuments/"+data_file+"/"+urls)
        extension=append("C:/TEMP/kmversha/Desktop/fdocuments/"+data_file+"/"+urls)
        with open(extension, 'r') as f:
            document_list.append(f.read())
            print count
            count=count+1
            soup = BeautifulSoup(f.read())
            for script in soup(["script", "style"]):
                # Cleaning the html file and extracting text
                script.extract()
                text = soup.get_text()
                lines = (line.strip() for line in text.splitlines())
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                text = '\n'.join(chunk for chunk in chunks if chunk)
                document_list.append(text)


#################### Extracting and Cleaning the Tag Details
tree = ET.ElementTree(file='C:/TEMP/kmversha/Desktop//taginfo.xml')
root = tree.getroot()
tag_list=[]
print root
for docs in root.findall('document'):
    name=[]
    weight=[]
    detail=[]
    d_count={}
    for info in docs:
        detail.append(info.text)
        for n in info.findall('./tag/name'):
            name.append(n.text)
        for w in info.findall('./tag/weight'):
            weight.append(w.text)
        for d in range(len(name)):
            d_count[name[d]]=weight[d]
    tag_weight=json.dumps(d_count, ensure_ascii=True)
    tag_list.append(detail+[tag_weight])
print len(tag_list)        
print len(document_list)


#################### Creating the training set
with open("C:/TEMP/kmversha/Desktop//Training_Set.csv",'wb') as csv_out:
    csvwriter = csv.writer(csv_out)
    for i in range(len(tag_list)):
        csvwriter.writerow(document_list[i]+tag_list[i])

