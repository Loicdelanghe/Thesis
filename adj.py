import re
from nltk.tokenize import RegexpTokenizer

Adjectieven = "ADJ("
adj_pre = "ADJ(prenom,"
adj_nom = "ADJ(nom,"
adj_postnom = "ADJ(postnom,"
adj_vrij = "ADJ(vrij,"


Adjectieven_cnt = 0
adj_pre_cnt = 0
adj_nom_cnt = 0
adj_postnom_cnt = 0
adj_vrij_cnt = 0


if __name__ == "__main__":
    path='/users/Loicd/Python/Thesis/Data_thesis/pos_tags_elsschot/10_tankpos.txt'
    f=open(path)
    mylist = f.readlines()
    f.close()



    lin=[]

    for item in mylist:
        lin.append(item)

    Adjectieven_cnt = sum([Adjectieven_cnt+1 for item in lin if Adjectieven in item])
    adj_pre_cnt = sum([adj_pre_cnt+1 for item in lin if adj_pre in item])
    adj_nom_cnt = sum([adj_nom_cnt+1 for item in lin if adj_nom in item])
    adj_postnom_cnt = sum([adj_postnom_cnt+1 for item in lin if adj_postnom in item])
    adj_vrij_cnt = sum([adj_vrij_cnt+1 for item in lin if adj_vrij in item])

    print("Adjectieven: ",Adjectieven_cnt)
    print("adj_pre: ",adj_pre_cnt)
    print("adj_nom: ",adj_nom_cnt)
    print("adj_postnom: ",adj_postnom_cnt)

    print("adj_vrij: ",adj_vrij_cnt)
