# -*- coding: utf-8 -*-

import os
import random
import codecs

__author__ = 'andy.cheung'


DIR_POSEV = './pos'
DIR_NEGEV = './neg'

# map mots -> occurence


def load_TAGGED(DIR):
    print("--- lecture fichier ---")
    # Open a file
    file = codecs.open(DIR, "r",'utf-8')
    print("Name of the file: ", file.name)

    line = file.read()
    #print("Read Line: %s" % (line))

    poubelle = line.split('\n')

    print(poubelle)

    for i in range(len(poubelle)-1):
        mot = poubelle[i].split('\t')[2]
        print(mot)

    # Close opend file
    file.close()


def getFolderList_TAGGED(DIR):
    f = []
    for file in os.listdir(DIR):
        if file.endswith(".txt"):
            print(file)
            f.append(file)

    newf = random.shuffle(f)
    print(f)

    for n in range(len(f)):
        load_TAGGED(f[n])

#load("neg-0000.txt")
getFolderList_TAGGED(".")