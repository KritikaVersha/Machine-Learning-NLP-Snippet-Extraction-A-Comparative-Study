import os
import csv
import bz2
from xml.etree import cElementTree as ET
import json,time,urllib
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup, Tag
#import nltk


#################### Extracting and Cleaning the Document File
document_list=[]
count=1;
filepath = "/Users/kritikaversha/Downloads/documents/00a9f3c4147462e18229d68479ad7784"
data=urllib.urlopen(filepath)
soup =BeautifulSoup(data)
para= soup.findAll('p')
for i in para:
    print (i.text).encode('utf-8')
    li=(i.findNext('li'))
    if ((li.findNext('p'))):
        j= i.findAll(True, recursive=False)
        for tags in j:
            print tags.text

#para2= soup.findAll('ul',{"":""})
#print para2
#for i in para:
#    if (i.name=='p'):
#        print (i.text).encode('utf-8')
#        j= i.findAll(True, recursive=False)
#        for tags in j:
#            print tags.text
#  
#for item in soup.contents:
#    print item

#for data_file in (os.listdir(filepath)):
#        extension='file:///Users/kritikaversha/Downloads/documents/'+data_file
#        data=urllib.urlopen(extension)
#        soup=BeautifulSoup(data)
#        print ((soup.p).text).encode('utf-8')
#        print '==================================================================================='
#    
             
