import numpy as np
from collections import Counter



def tokenizer(mylist):
   txt2=mylist.lower()
   table=str.maketrans("!?.()",5*" ")
   mylist=txt2.translate(table)
   mylist=mylist.split()
   return mylist

def extract(mylist):
    cnt=Counter(mylist)
    output=dict()
    pers_vnw=["ik","jij","je","zij","hij","wij","jullie","u"]
    for key, value in cnt.items():
     if key in pers_vnw:
      output[key]=value
    return output

def normalize(output,mylist):
    count=len(mylist)
    norm=count/1000
    final_count=dict()
    for key,value in output.items():
        final_count[key]=value/norm
    return final_count



if __name__ == "__main__":
    path='/users/Loicd/python/Thesis/Data_thesis/Claustokenize/14geruchtenToken.txt'
    f=open(path)
    mylist = f.read()
    mylist=tokenizer(mylist)
    counts=extract(mylist)
    re=normalize(counts,mylist)

    print(normalize(counts,mylist))
    ans=0
    for key, value in re.items():
        ans+=value
    print(ans)
