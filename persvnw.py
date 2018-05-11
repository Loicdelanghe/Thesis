import re
from nltk.tokenize import RegexpTokenizer

ik = "VNW(pers,pron,nomin,vol,1,ev)"
ikzelf_ikke = "VNW(pers,pron,nomin,nadr,1,ev)"
k = "VNW(pers,pron,nomin,red,1,ev)"
wij = "VNW(pers,pron,nomin,vol,1,mv)"
wijzelf = "VNW(pers,pron,nomin,nadr,1,mv)"
we = "VNW(pers,pron,nomin,red,1,mv)"



jij = "VNW(pers,pron,nomin,vol,2v,ev)"
jijzelf = "VNW(pers,pron,nomin,nadr,2v,ev)"
je = "VNW(pers,pron,nomin,red,2v,ev)"
u_1 = "VNW(pers,pron,nomin,vol,2b,getal)"
uzelf = "VNW(pers,pron,nomin,nadr,2b,getal)"
gij = "VNW(pers,pron,nomin,vol,2,getal)"
gijzelf = "VNW(pers,pron,nomin,nadr,2,getal)"
ge = "VNW(pers,pron,nomin,red,2,getal)"



hij = "VNW(pers,pron,nomin,vol,3,ev,masc)"
hijzelf = "VNW(pers,pron,nomin,nadr,3m,ev,masc)"
ie = "VNW(pers,pron,nomin,red,3,ev,masc)"
men = "VNW(pers,pron,nomin,red,3p,ev,masc)"
zij_enk = "VNW(pers,pron,nomin,vol,3v,ev,fem)"
zijzelf_enk = "VNW(pers,pron,nomin,nadr,3v,ev,fem)"
Zij  ="VNW(pers,pron,nomin,vol,3p,mv)"
zijzelf ="VNW(pers,pron,nomin,nadr,3p,mv)"




jou = "VNW(pers,pron,obl,vol,2v,ev)"
hem = "VNW(pers,pron,obl,vol,3,ev,masc)"
hemzelf = "VNW(pers,pron,obl,nadr,3m,ev,masc)"
m = "VNW(pers,pron,obl,red,3,ev,masc)"
haar = "VNW(pers,pron,obl,vol,3,getal,fem)"
haarzelf = "VNW(pers,pron,obl,nadr,3v,getal,fem)"
r_dr = "VNW(pers,pron,obl,red,3v,getal,fem)"
hun = "VNW(pers,pron,obl,vol,3p,mv)"
henzelf = "VNW(pers,pron,obl,nadr,3p,mv)"
jullie = "VNW(pers,pron,stan,nadr,2v,mv)"
het = "VNW(pers,pron,stan,red,3,ev,onz)"
ze_enk = "VNW(pers,pron,stan,red,3,ev,fem)"
ze_mv = "VNW(pers,pron,stan,red,3,mv)"
mijnsgelijke = "VNW(pers,pron,gen,vol,1,ev)"
ons_gelijke = "VNW(pers,pron,gen,vol,1,mv)"
uws_gelijke = "VNW(pers,pron,gen,vol,2,getal)"
zijns_gelijke = "VNW(pers,pron,gen,vol,3m,ev)"
haars_gelijke = "VNW(pers,pron,gen,vol,3v,getal)"
huns_gelijke = "VNW(pers,pron,gen,vol,3p,mv)"





mij = "VNW(pr,pron,obl,vol,1,ev)"
mezelf = "VNW(pr,pron,obl,nadr,1,ev)"
me = "VNW(pr,pron,obl,red,1,ev)"
ons = "VNW(pr,pron,obl,vol,1,mv)"
onszelf = "VNW(pr,pron,obl,nadr,1,mv)"
je_pr = "VNW(pr,pron,obl,red,2v,getal)"
jezelf = "VNW(pr,pron,obl,nadr,2v,getal)"
u_enk_o = "VNW(pr,pron,obl,vol,2,getal)"
uzelf = "VNW(pr,pron,obl,nadr,2,getal)"







ik_cnt=ikzelf_ikke_cnt=k_cnt=wij_cnt=wijzelf_cnt=we_cnt=jij_cnt=jijzelf_cnt=je_cnt=u_1_cnt=uzelf_cnt=gij_cnt=gijzelf_cnt=ge_cnt=hij_cnt=hijzelf_cnt=ie_cnt=men_cnt=zij_enk__cnt=zijzelf_enk_cnt=Zij_cnt=zijzelf_cnt=jou_cnt=hem_cnt=hemzelf_cnt=m_cnt=haar_cnt=haarzelf_cnt=r_dr_cnt=hun_cnt=henzelf_cnt=jullie_cnt=het_cnt=ze_enk_cnt=ze_mv_cnt=mijnsgelijke_cnt=onsgelijke_cnt=uwssgelijke_cnt=zijnsgelijke_cnt=haarsgelijke_cnt=huns_gelijke_cnt=0
mij_cnt=mezelf_cnt=me_cnt=ons_cnt=onszelf_cnt=je_pr_cnt=jezelf_cnt=u_enk_o_cnt=uzelf_cnt=0

if __name__ == "__main__":
    path='/users/Loicd/Python/Thesis/Data_thesis/pos_tags_claus/verdriet1POS.txt'
    path2 = 'Data_thesis/1983_Het_verdriet_van_Belgie.txt'
    f=open(path)
    mylist = f.readlines()
    f.close()
    words=open(path2,encoding="latin1")
    words=words.read()

    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(words)
    lin=[]

    for item in mylist:
        lin.append(item)

    ik_cnt = sum([ik_cnt+1 for item in lin if ik in item])
    ikzelf_ikke_cnt = sum([ikzelf_ikke_cnt+1 for item in lin if ikzelf_ikke in item])
    k_cnt = sum([k_cnt+1 for item in lin if k in item])
    wij_cnt = sum([wij_cnt+1 for item in lin if wij in item])
    wijzelf_cnt = sum([wijzelf_cnt+1 for item in lin if wijzelf in item])
    we_cnt = sum([we_cnt+1 for item in lin if we in item])

    jij_cnt = sum([jij_cnt+1 for item in lin if jij in item])
    jijzelf_cnt = sum([jijzelf_cnt+1 for item in lin if jijzelf in item])
    je_cnt = sum([je_cnt+1 for item in lin if je in item])
    u_1_cnt = sum([u_1_cnt+1 for item in lin if u_1 in item])
    uzelf_cnt = sum([uzelf_cnt+1 for item in lin if uzelf in item])
    gij_cnt = sum([gij_cnt+1 for item in lin if gij in item])
    gijzelf_cnt = sum([gijzelf_cnt+1 for item in lin if gijzelf in item])
    ge_cnt = sum([ge_cnt+1 for item in lin if ge in item])

    hij_cnt = sum([hij_cnt+1 for item in lin if hij in item])
    hijzelf_cnt = sum([hijzelf_cnt+1 for item in lin if hijzelf in item])
    ie_cnt = sum([ie_cnt+1 for item in lin if ie in item])
    men_cnt = sum([men_cnt+1 for item in lin if men in item])
    zij_enk__cnt = sum([zij_enk__cnt+1 for item in lin if zij_enk in item])
    zijzelf_enk_cnt = sum([zijzelf_enk_cnt+1 for item in lin if zijzelf in item])
    Zij_cnt = sum([Zij_cnt+1 for item in lin if Zij in item])
    zijzelf_cnt = sum([zijzelf_cnt+1 for item in lin if zijzelf in item])

    jou_cnt = sum([jou_cnt+1 for item in lin if jou in item])
    hem_cnt = sum([hem_cnt+1 for item in lin if hem in item])
    hemzelf_cnt = sum([hemzelf_cnt+1 for item in lin if hemzelf in item])
    m_cnt = sum([m_cnt+1 for item in lin if m in item])
    haar_cnt = sum([haar_cnt+1 for item in lin if haar in item])
    haarzelf_cnt = sum([haarzelf_cnt+1 for item in lin if haarzelf in item])
    r_dr_cnt = sum([r_dr_cnt+1 for item in lin if r_dr in item])
    hun_cnt = sum([hun_cnt+1 for item in lin if hun in item])
    henzelf_cnt = sum([henzelf_cnt+1 for item in lin if henzelf in item])
    jullie_cnt = sum([jullie_cnt+1 for item in lin if jullie in item])
    het_cnt = sum([het_cnt+1 for item in lin if het in item])
    ze_enk_cnt = sum([ze_enk_cnt+1 for item in lin if ze_enk in item])
    ze_mv_cnt = sum([ze_mv_cnt+1 for item in lin if ze_mv in item])
    mijnsgelijke_cnt = sum([mijnsgelijke_cnt+1 for item in lin if mijnsgelijke in item])
    onsgelijke_cnt = sum([onsgelijke_cnt+1 for item in lin if ons_gelijke in item])
    uwssgelijke_cnt = sum([uwsgelijke_cnt+1 for item in lin if uws_gelijke in item])
    zijnsgelijke_cnt = sum([zijnsgelijke_cnt+1 for item in lin if zijns_gelijke in item])
    haarsgelijke_cnt = sum([haarsgelijke_cnt+1 for item in lin if haars_gelijke in item])
    huns_gelijke_cnt = sum([huns_gelijke_cnt+1 for item in lin if huns_gelijke in item])


    mij_cnt = sum([mij_cnt+1 for item in lin if mij in item])
    mezelf_cnt = sum([mezelf_cnt+1 for item in lin if mezelf in item])
    me_cnt = sum([me_cnt+1 for item in lin if me in item])
    ons_cnt = sum([ons_cnt+1 for item in lin if ons in item])
    onszelf_cnt = sum([onszelf_cnt+1 for item in lin if onszelf in item])
    je_pr_cnt = sum([je_pr_cnt+1 for item in lin if je_pr in item])
    jezelf_cnt = sum([jezelf_cnt+1 for item in lin if jezelf in item])
    u_enk_o_cnt = sum([u_enk_o_cnt+1 for item in lin if u_enk_o in item])
    uzelf_cnt = sum([uzelf_cnt+1 for item in lin if uzelf in item])





    output_list = [ik_cnt,ikzelf_ikke_cnt,k_cnt,wij_cnt,wijzelf_cnt,we_cnt,jij_cnt,jijzelf_cnt,
    je_cnt,u_1_cnt,uzelf_cnt,gij_cnt,gijzelf_cnt,ge_cnt,hij_cnt,hijzelf_cnt,ie_cnt,men_cnt,zij_enk__cnt,zijzelf_enk_cnt,Zij_cnt,zijzelf_cnt,
    jou_cnt,hem_cnt,hemzelf_cnt,m_cnt,haar_cnt,haarzelf_cnt,r_dr_cnt,hun_cnt,henzelf_cnt,jullie_cnt,het_cnt,ze_enk_cnt,ze_mv_cnt,mijnsgelijke_cnt,
    onsgelijke_cnt,uwssgelijke_cnt,zijnsgelijke_cnt,haarsgelijke_cnt,huns_gelijke_cnt]

    pr_refl = [mij_cnt,mezelf_cnt,me_cnt,ons_cnt,onszelf_cnt,je_pr_cnt,jezelf_cnt,u_enk_o_cnt,uzelf_cnt]




    print(len(tokens))
    print(sum(output_list))
    print(sum(pr_refl))
    print(sum(pr_refl)+sum(output_list))
