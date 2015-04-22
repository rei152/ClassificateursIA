# -*- coding: utf-8 -*-

import os
import random
import codecs

__author__ = 'andy.cheung'


DIR_POSEV = './pos'
DIR_NEGEV = './neg'

# map mots -> occurence
def loadFile_TAGGED(dico, DIR):
    print("--- lecture fichier ---")
    # Open a file
    file = codecs.open(DIR, "r",'utf-8')
    print("Name of the file: ", file.name)

    line = file.read()
    print("Read Line: %s" % (line))
    poubelle = line.split('\n')
    print(len(poubelle))
    print(poubelle)

    for i in range(len(poubelle)-1):
        # print("poubelle " + poubelle[i])
        try:
            mot = poubelle[i].split('\t')[2].rstrip('\r')
        except IndexError:
            mot = poubelle[i].rstrip('\r')

        print(mot)

        if(mot in dico):
            dico[mot] += 1
        else:
            dico[mot] = 1

    # Close opend file
    file.close()


def getFolderList_TAGGED(dico,DIR):
    f = []
    for file in os.listdir(DIR):
        if file.endswith(".txt"):
            print(file)
            f.append(file)

    newf = random.shuffle(f)
    # print(f)

    for n in range(len(f)):
        loadFile_TAGGED(dico, f[n])

def loadForbidden(DIR, listForbiddenWords):
    print("--- lecture fichier ---")
    # Open a file
    file = codecs.open(DIR, "r",'utf-8')
    print("Name of the file: ", file.name)

    line = file.read()

    # print("Read Line: %s" % (line))
    poubelle = line.split('\n')

    for i in poubelle:
        print(i)
        listForbiddenWords.append(i)

    print("listForbiddenWords")
    print(listForbiddenWords)
    # Close opend file
    file.close()

forbidden = []
dico = {}

#load("neg-0000.txt")
loadForbidden("frenchST.txt",forbidden)
getFolderList_TAGGED(dico,".")

print(len(dico))
print(dico)