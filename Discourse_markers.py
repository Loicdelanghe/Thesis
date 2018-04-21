import numpy as np
import json
from pprint import pprint
from collections import Counter



path=''

def find_bigrams(input_list):
  bigram_list = []
  for i in range(len(input_list)-1):
      bigram_list.append((input_list[i], input_list[i+1]))
  return bigram_list

def find_trigrams(input_list):
  trigram_list = []
  for i in range(len(input_list)-2):
      trigram_list.append((input_list[i], input_list[i+1],input_list[i+2]))
  return trigram_list

def tokenizer(mylist):
   mylist=mylist.lower()
   mylist=mylist.split(" ")

   ans=0
   return_list=[]
   for item in mylist:
       newitem=item.strip('\n')
       return_list.append(newitem)

   return return_list

def extractcounts(mylist,X,marker):
       index1=0
       index2=1000
       CountVector=[]

       for i in range(0,X):
           TempList=mylist[int(index1):int(index2)]
           index1=index2
           index2+=1000
           Count=0

           for item in TempList:
               if item==marker:
                   Count+=1
           if Count!=0:
            CountVector.append(Count)
           if Count==0:
            CountVector.append(0)

       return CountVector






if __name__ == '__main__':

    f=open(path)
    mylist = f.read()
    f.close()
    wordcount=len(tokenizer(mylist))
    mylist=tokenizer(mylist)
    with open('discourse_weighted_dictionary_v2.1_nl.json') as json_data:
       d = json.load(json_data)
       json_data.close()

    a={}

    print("There are",wordcount,"tokens in the text")
    wordsets=int(input("Sets of 1000 tokens?"))
    marker_list=[]


    for discourse_marker in d:
       marker_list.append(str(discourse_marker))
       a.update({discourse_marker:sum(extractcounts(mylist,wordsets,discourse_marker))})


    tuple_markers=[]
    for item in marker_list:
      b=tuple(filter(None, item.split(' ')))
      tuple_markers.append(b)

    output_dict=a




    f=open(path)
    mylist = f.read()
    mylist=tokenizer(mylist)
    f.close()





    bigrams=find_bigrams(mylist)
    bigram_count=Counter(bigrams)
    bigram_markers=dict()
    for item in tuple_markers:
        for key,value in bigram_count.items():
            if key==item:
                bigram_markers[key]=value


    trigrams=find_trigrams(mylist)
    trigram_count=Counter(trigrams)
    trigram_markers=dict()

    tuple_markers_2=[('eerder', 'heeft', 'gezegd'), ('op', 'zijn', 'beurt'), ('tegen', 'die', 'tijd'), ('in', 'de', 'plaats'),
('in', 'schril', 'contrast'), ('die', 'nog', 'steeds'),('in', 'contrast', 'hiermee'),('zo', 'lang', 'als'),('op', 'haar', 'beurt'),
('tegen', 'die', 'tijd'),('in', 'het' ,'bijzonder'),('uiteindelijk', 'van', 'de'),('eigenlijk', 'in', 'de'),('met', 'andere', 'woorden'),
('in', 'andere', 'woorden'),('met', 'uitzondering', 'van')]

    for item in tuple_markers_2:
        for key,value in trigram_count.items():
             if key==item:
                 trigram_markers[key]=value


#make sure that every marker counts only once, e.g: "maar de" can only count as "maar de" and not as "maar"
    for key2,value2 in bigram_markers.items():
        for key,value in output_dict.items():
            if key==key2[0]:
                val=value-value2
                output_dict[key]=val


    for key2,value2 in bigram_markers.items():
        for key,value in output_dict.items():
            if key==key2[1]:
                val=value-value2
                output_dict[key]=val



    for key,value in output_dict.items():
        for key3,value3 in bigram_markers.items():
            x=key3[0]+" "+key3[1]
            if key==x:
                output_dict[key]=value3



#idem but for the trigram list
    Trigram_split=[]
    for key,value in trigram_markers.items():
        Trigram_split.append(key[0])
        Trigram_split.append(key[1])
        Trigram_split.append(key[2])

    cnt=Counter(Trigram_split)
    for key,value in trigram_markers.items():
        new_key=key[0]+' '+key[1]+' '+key[2]
        output_dict[new_key]=value

    for key,value in trigram_markers.items():
        for key2,value2 in output_dict.items():
            if key[0]==key2:
                val=value2-value
                output_dict[key2]=val
            if key[1]==key2:
                val=value2-value
                output_dict[key2]=val
            if key[2]==key2:
                val=value2-value
                output_dict[key2]=val





    print(output_dict)
