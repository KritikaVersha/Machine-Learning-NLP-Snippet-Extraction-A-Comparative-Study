# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 17:09:39 2014

@author: abhishek
"""
from funcs import requests,BeautifulSoup,GetDrugPage,ItemToStringList
import re, time, csv


with open('wikidata/med_wiki_dic.txt','r') as f:
    med_wiki_dic_saved = eval(f.read())


#with open("final_med_list.txt") as f:
#    content2 = f.readlines()
#print(content2)
#medict_wiki = {}

#%%
wiki_struct_infotable = {}
wiki_main = {}
wiki_name = {}

#%%
#with open('final_medict_wiki.csv','r') as f:
#    medread = csv.reader(f)
#    for row in medread:
#        medict_wiki[row[0]] = row[1]
#%%
for medurl in med_wiki_dic_saved.keys():
    medname = med_wiki_dic_saved[medurl]
    try:
        response = requests.get(medurl)
        soup = BeautifulSoup(response.content)
        #print(soup)
        
        #%% Scrape Main Name
        mname = soup.find("h1", id="firstHeading").next.text
        wiki_name[medname] = mname
        
        #%% Scrape Info Table
        InfoTable = {}
        mytab = soup.find("table", {"class":"infobox"})
        for grow in mytab.find_all('tr'):
            try:
                item=grow.find("th",{"scope":"row"},{"style":"text-align:left"})
                key = ("".join(ItemToStringList(item)))
                value = item.find_next("td").text.split()            
                InfoTable[key] = value
            except:
                pass
        wiki_struct_infotable[medname] = InfoTable
        
        
        #%% Scrape Main Data
        MainData = []
        mydiv = soup.find("table", {"class":"infobox"})
        toc = mydiv.find_next("div",{"id" : "toc"})
        for sib in mydiv.find_next_siblings("p"):
            if sib.next.next == toc:
                break
            else:
                MainData.append(''.join(ItemToStringList(sib)))
        wiki_main[medname] = ''.join(MainData)       
    except:
        pass
#%%
        
f = open('wiki_struct_infotable.txt','w')
f.write(str(wiki_struct_infotable))
f.close()

f = open('wiki_name.txt','w')
f.write(str(wiki_name))
f.close()

f = open('wiki_main.txt','w')
f.write(str(wiki_main))
f.close()














