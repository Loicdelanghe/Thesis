import re
from nltk.tokenize import RegexpTokenizer


vz_init = "VZ(init"
vz_fin = "VZ(fin"
vz_versm = "VZ(versm"



vz_cnt = 0
_vz1_cnt = 0
vz_init__cnt = 0
vz_fin_cnt = 0
vz_versm_cnt = 0



if __name__ == "__main__":
    path='/users/Loicd/Python/Thesis/Data_thesis/pos_tags_claus/15_slaappos.txt'
    f=open(path)
    mylist = f.readlines()
    f.close()



    lin=[]

    for item in mylist:
        lin.append(item)


    vz_init__cnt = sum([vz_init__cnt+1 for item in lin if vz_init in item])
    vz_fin_cnt = sum([vz_fin_cnt+1 for item in lin if vz_fin in item])
    vz_versm_cnt = sum([vz_versm_cnt+1 for item in lin if vz_versm in item])


    print("prep: ",vz_init__cnt+vz_versm_cnt+vz_fin_cnt)

    print("prep_init : ",vz_init__cnt)
    print("prep fin : ",vz_fin_cnt)
    print("prep versm : ",vz_versm_cnt)
