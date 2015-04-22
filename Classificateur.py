import codecs

import os, sys
import random

DIR_POSEV = './pos'
DIR_NEGEV = './neg'

# map mots -> occurence

def getCorpus(DIR):

    corpusTrain,corpusTest = [],[]

    LEN = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

    for i in range(0,int(LEN*0.2)):
        while(True):
            n = random.randint(0,999)
            if(n not in corpusTest):
                break

        corpusTest.append(n)

        for i in range (LEN):
            if(i not in corpusTest):
                corpusTrain.append(i)

    return corpusTest, corpusTrain

corpusTestPos = []
corpusTestNeg = []

corpusTrainPos = []
corpusTrainNeg = []


global DIR_NEGEV
global DIR_POSEV


# map mots -> occurence
def loadFile_TAGGED(dico, DIR):
    # print("--- lecture fichier ---")

    # Open a file
    # print(DIR)
    file = codecs.open(DIR, "r",'utf-8')
    # print("Name of the file: ", file.name)

    line = file.read()
    # print("Read Line: %s" % (line))
    poubelle = line.split('\n')
    # print(len(poubelle))
    # print(poubelle)

    for i in range(len(poubelle)-1):
        # print("poubelle " + poubelle[i])
        try:
            mot = poubelle[i].split('\t')[2].rstrip('\r')
        except IndexError:
            mot = poubelle[i].rstrip('\r')

        # print(mot)

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
            # print(file)
            f.append(file)

    newf = random.shuffle(f)
    # print(f)

    for n in range(len(f)):
        loadFile_TAGGED(dico, DIR+"/"+f[n])

def loadForbidden(DIR, listForbiddenWords):
    # print("--- lecture fichier ---")
    # Open a file

    file = codecs.open(DIR, "r",'utf-8')
    # print("Name of the file: ", file.name)

    line = file.read()

    # print("Read Line: %s" % (line))
    poubelle = line.split('\r\n')

    for i in poubelle:
        # print(i)
        listForbiddenWords.append(i)

    print("listForbiddenWords")
    print(listForbiddenWords)
    # Close opend file
    file.close()



def main():
    forbidden = []

    totalWords = 0

    mapNegWords = {}
    mapNegProba = {}

    mapPosWords = {}
    mapPosProba = {}

    corpusTestPos, corpusTrainPos = getCorpus(DIR_NEGEV)
    corpusTestNeg, corpusTrainNeg = getCorpus(DIR_POSEV)

    print(corpusTestPos)
    print(corpusTrainPos)

    loadForbidden("frenchST.txt",forbidden)
    getFolderList_TAGGED(mapNegWords,"./tagged/neg")
    getFolderList_TAGGED(mapPosWords,"./tagged/pos")

    totalWords = len(mapNegWords)+len(mapPosWords)
    print(totalWords)

    print("Negative words")
    print(mapNegWords)
    print(len(mapNegWords))

    print("Positive words")
    print(mapPosWords)
    print(len(mapPosWords))

    print("proba neg")
    mapNegProba = calculOccurance(mapNegWords,totalWords)
    print(mapNegProba)

    print("proba pos")
    mapPosProba = calculOccurance(mapPosWords,totalWords)
    print(mapPosProba)





def calculOccurance(mapWord,totalWord):
    newMap = {}

    for i in mapWord:
        newMap[i] = mapWord[i]/totalWord

    return newMap

if __name__ == '__main__':
    main()

# LEN_NEG = len([name for name in os.listdir(DIR_NEGEV) if os.path.isfile(os.path.join(DIR_NEGEV, name))])
# LEN_POS = len([name for name in os.listdir(DIR_POSEV) if os.path.isfile(os.path.join(DIR_POSEV, name))])
#
# corpusTestPos = []
# corpusTestNeg = []
#
# corpusTrainPos = []
# corpusTrainNeg = []
#
# n = -1
#
# for i in range(0,int(LEN_POS*0.1)):
#
#     while(True):
#         n = random.randint(0,999)
#         if(n not in corpusTestPos):
#             break
#
#     corpusTestPos.append(n)
#
# for i in range (LEN_POS):
#     if(i not in corpusTestPos):
#         corpusTrainPos.append(i)
#
#
#
# for i in range(0,int(LEN_NEG*0.1)):
#
#     while(True):
#         n = random.randint(0,999)
#         if(n not in corpusTestNeg):
#             break
#
#     corpusTestNeg.append(n)
#
# for i in range (LEN_NEG):
#     if(i not in corpusTestNeg):
#         corpusTrainNeg.append(i)