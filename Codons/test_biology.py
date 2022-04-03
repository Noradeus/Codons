#!/usr/bin/env python
# coding: utf-8

# In[7]:


import biology


# test pour exercice 1

# In[14]:


def test_est_base():
    assert not biology.est_base("X")
    assert biology.est_base("A")
    assert biology.est_base("G")
    assert biology.est_base("C")
    assert biology.est_base("T")
    assert not biology.est_base("a")
    print("fonction est_base: ok")

test_est_base()


# test pour exercice 2

# In[16]:


def test_est_adn():
    assert not biology.est_adn("fgjkhdf")
    assert not biology.est_adn("aCT")
    assert biology.est_adn("ATG")
    print("fonction est_adn: ok")

test_est_adn()


# test pour exercice 3

# In[19]:


def test_arn():
    assert biology.arn("ATG")=="AUG"
    assert biology.arn("AUG")==None
    assert biology.arn("AAA")=="AAA"
    print("fonction arn: ok")

test_arn()


# test pour exercice 4

# In[22]:


def test_arn_to_codons():
    assert biology.arn_to_codons("AAAUUUCCC")==["AAA","UUU","CCC"]
    assert biology.arn_to_codons("AAAUUUCC")==["AAA","UUU"]
    print("fonction arn_to_codons: ok")

test_arn_to_codons()


# test pour exercice 6 (test exo 5 manquant car difficiles a tester sans utiliser les résultats possiblement erronés rendus par la focntions)

# In[27]:


def test_codons_to_aa():
    assert biology.codons_to_aa(["CGU", "AAU", "UAA", "GGG", "CGU"],biology.load_dico_codons_aa("./data/codons_aa.json"))==["Arginine", "Asparagine"]
    print("fonction codons_to_aa: ok")

test_codons_to_aa()

# Partie 2

# exercice 1

def test_nextIndice():
    assert biology.nextIndice(["bonjour", "hello", "buongiorno", "ciao", "bye"],1,["hello", "bye"])==1
    assert biology.nextIndice(["bonjour", "hello", "buongiorno", "ciao", "bye"],2,["hello", "bye"])==4
    print("fonction nextIndice: ok")

test_nextIndice()

# exercice 2

def test_decoupe_sequence():
    assert biology.decoupe_sequence(["val1", "début", "val2", "val3", "end", "val4", "fin", "begin", "val5", "fin", "val6"],["début", "begin"],["fin", "end"])==[["val2", "val3"],["val5"]]
    print("fonction decoupe_sequence: ok")

test_decoupe_sequence

# exercice 3

def test_codons_to_seq_codantes():
    assert biology.codons_to_seq_codantes(["CGU", "UUU", "AUG", "CGU", "AUG", "AAU", "UAA", "AUG", "GGG", "CCC",  "CGU", "UAG", "GGG"],biology.load_dico_codons_aa("data/codons_aa.json"))==[["CGU", "AUG", "AAU"],["GGG", "CCC", "CGU"]]
    print("fonction codons_to_seq_codantes: ok")

test_codons_to_seq_codantes()

# exercice 4

def test_codons_to_seq_aas():
    assert biology.seq_codantes_to_seq_aas([["CGU", "AUG", "AAU"],["GGG", "CCC", "CGU"]],biology.load_dico_codons_aa("data/codons_aa.json"))==[["Arginine", "Methionine", "Asparagine"],["Glycine", "Proline", "Arginine"]]
    print("fonction seq_codantes_to_seq_aas: ok")

test_codons_to_seq_aas()

# exercice 5

def test_adn_encore_molecule():
    biology.adn_encore_molecule("CGTTTTATGCGTATGAATTAAATGGGGCCCCGTTAGGGG",biology.load_dico_codons_aa("data/codons_aa.json"),["Glycine", "Proline", "Arginine"])
    print("fonction adn_encode_molecule: ok")

test_adn_encore_molecule()