import re
from nltk.tokenize import RegexpTokenizer

dialectwoorden = "dial)"
naamwoorden = "N(soort"
eigen = "N(eigen"
eigen_2 = "SPEC(deeleigen"

#dubbele eigennamen bv. Frank Peeters ==> telt als één eigennaam
dialect_cnt = 0
naamwoorden_cnt = 0
eigen_cnt = 0
eigen_2_cnt = 0


if __name__ == "__main__":
    path='/users/Loicd/Python/Thesis/Data_thesis/pos_tags_claus/15_slaappos.txt'
    f=open(path)
    mylist = f.readlines()
    f.close()



    lin=[]

    for item in mylist:
        lin.append(item)

    dialect_cnt = sum([dialect_cnt+1 for item in lin if dialectwoorden in item])
    naamwoorden_cnt = sum([naamwoorden_cnt+1 for item in lin if naamwoorden in item])
    eigen_cnt = sum([eigen_cnt+1 for item in lin if eigen in item])
    eigen_2_cnt = sum([eigen_2_cnt+1 for item in lin if eigen_2 in item])

    print("dialects: ",dialect_cnt)
    print("naam soort: ",naamwoorden_cnt)
    print("eigennamen: ",eigen_cnt)
    print("eigennamen SPEC: ",eigen_2_cnt)
