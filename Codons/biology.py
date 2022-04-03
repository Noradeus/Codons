#!/usr/bin/env python
# coding: utf-8

# # Partie 1

# importations diverses

# In[18]:


from json import *


# exercice 1

# In[19]:


def est_base(car):
    if car=="A" or car=="T" or car=="G" or car=="C":
        return True
    else:
        return False


# exercice 2

# In[20]:


def est_adn(chaine):
    res=0
    for elt in chaine:
        if est_base(elt)==False:
            res=1
    return res==0


# exercice 3

# In[21]:


def arn(chaine):
    res=""
    if est_adn(chaine)==False:
        return None
    for elt in chaine:
        if elt=="T":
            res+="U"
        else:
            res+=elt
    return res


# exercice 4

# In[22]:


def arn_to_codons(chaine):
    i=0
    tab=[]
    while i<len(chaine)//3:
        k=i*3
        val=chaine[k]+chaine[k+1]+chaine[k+2]
        tab.append(val)
        i+=1
    return tab


# exercice 5

# In[3]:


def load_dico_codons_aa(fichier):
    f=open(fichier,"r")
    dicnon=f.read()
    f.close
    dico=loads(dicnon)
    return dico


def incrLettre(chn,x):
    if x==len(chn)+1:
        return "A"+chn
    elif x==1:
        if chn[-x]=="A":
            return chn[:-x]+"U"
        elif chn[-x]=="U":
            return chn[:-x]+"G"
        elif chn[-x]=="G":
            return chn[:-x]+"C"
        elif chn[-x]=="C":
            return incrLettre(chn[:-x]+"A",x+1)
    else:
        if chn[-x]=="A":
            return chn[:-x]+"U"+chn[-x+1:]
        elif chn[-x]=="U":
            return chn[:-x]+"G"+chn[-x+1:]
        elif chn[-x]=="G":
            return chn[:-x]+"C"+chn[-x+1:]
        elif chn[-x]=="C":
            return incrLettre(chn[:-x]+"A"+chn[-x+1:],x+1)

def codons_stop(dico):
    tmp="AAA"
    tab_dic=list(dico)
    tab=[]
    while len(tmp)<4:
        if not tmp in tab_dic:
            tab.append(tmp)
        tmp=incrLettre(tmp,1)
    return tab

# exercice 6

# In[24]:


def codons_to_aa(tab,dico):
    x=list(dico)
    rep=[]
    for elt in tab:
        if elt in x:
            rep.append(dico[elt])
        else:
            return rep
    return rep


# # Partie 2

# In[ ]:

def nextIndice(tab,ind,elements):
    i=ind
    o=0
    while i<len(tab):
        if tab[i]==elements[o]:
            return i
        if o==len(elements)-1 and i==len(tab)-1:
            return len(tab)
        elif i==len(tab)-1 and o<len(elements):
            i=ind
            o+=1
        else:
            i+=1

def decoupe_sequence(seq,start,stop):
    dec=False
    i=0
    tab=[]
    o=0
    temp=[]
    while i<len(seq):
        if seq[i] in stop:
            o+=1
            dec=False
            if not temp==[]:
                tab.append(temp)
            temp=[]
        if dec:
            temp.append(seq[i])
        if seq[i] in start:
            dec=True
        i+=1
    return tab

dic=load_dico_codons_aa("data/codons_aa.json")
def codons_to_seq_codantes(seqCod,dico):
    return decoupe_sequence(seqCod,["AUG"],["AGA","AGG","UAA","UAG"])

def seq_codantes_to_seq_aas(tab,dico):
    rep=[]
    for i in tab:
        rep.append(codons_to_aa(i,dico))
    return rep

def adn_encore_molecule(ADN,dico,mol):
    ARN=arn(ADN)
    Codons=arn_to_codons(ARN)
    seqCod=codons_to_seq_codantes(Codons,dico)
    return mol in seq_codantes_to_seq_aas(seqCod,dico)

print(adn_encore_molecule("CGTTTTATGCGTATGAATTAAATGGGGCCCCGTTAGGGG",dic,["Glycine", "Proline", "Arginine"]))