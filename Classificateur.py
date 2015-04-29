import codecs

import os, sys
import random,math

DIR_POSEV = './pos'
DIR_NEGEV = './neg'

# map mots -> occurence

# def getCorpus(DIR,forbiddenWords):
#
#     corpusTrain,corpusTest = [],[]
#
#     LEN = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
#
#     for i in range(0,int(LEN*0.2)):
#         while(True):
#             n = random.randint(0,999)
#             if(n not in corpusTest):
#                 break
#
#         corpusTest.append(n)
#
#         for i in range (LEN):
#             if(i not in corpusTest):
#                 corpusTrain.append(i)
#
#     return corpusTest, corpusTrain

corpusTestPos = []
corpusTestNeg = []

corpusTrainPos = []
corpusTrainNeg = []


global DIR_NEGEV
global DIR_POSEV


# map mots -> occurence
def loadFile_TAGGED(DIR):
    # print("--- lecture fichier ---")

    dico = {}

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

    return dico


def getFolderList_TAGGED(DIR):
    f = []

    corpusTrain,corpusTest = [],[]

    for file in os.listdir(DIR):
        if file.endswith(".txt"):
            # print(file)
            f.append(file)

    # randomise la liste
    random.shuffle(f)

    for n in range(int(len(f))):
        if(n < int(len(f) * 0.2)):
            # corpusTrain = loadFile_TAGGED(mapWord, DIR+"/"+f[n])
            corpusTest = loadFile_TAGGED(DIR+"/"+f[n])
        else:
            corpusTrain = loadFile_TAGGED(DIR+"/"+f[n])

    return corpusTrain,corpusTest


    return corpusTrain,corpusTest

def loadFIleToMap(DIR, mapToPeuple):
    # mapToPeuple = {}

    # Open a file
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

        if(mot in mapToPeuple):
            mapToPeuple[mot] += 1
        else:
            mapToPeuple[mot] = 1

    # Close opend file
    file.close()

def main():
    forbidden = {}

    loadFIleToMap("frenchST.txt",forbidden)

    # corpusTestPos, corpusTrainPos = getCorpus(DIR_NEGEV,forbidden)
    # corpusTestNeg, corpusTrainNeg = getCorpus(DIR_POSEV,forbidden)

    corpusTrainNeg,corpusTestNeg = getFolderList_TAGGED("./tagged/neg")
    corpusTrainPos,corpusTestPos = getFolderList_TAGGED("./tagged/pos")
    # getFolderList_TAGGED(mapPosWords,"./tagged/pos")

    # mapNegWords = corpusTrainNeg.update(corpusTestNeg)
    # mapPosWords = corpusTrainPos.update(corpusTestPos)

    # mapNegProba = {}
    # mapPosProba = {}

    # print("corpusTestNeg")
    # print(corpusTestNeg)
    # print("corpusTestPos")
    # print(corpusTestPos)

    totalWords = len(corpusTrainNeg)+len(corpusTrainPos)

    # print(totalWords)
    # print("Negative words")
    # print(mapNegWords)
    # print(len(mapNegWords))
    #
    # print("Positive words")
    # print(mapPosWords)
    # print(len(mapPosWords))

    print("proba neg")
    mapNegProba = calculOccurance(corpusTrainNeg,totalWords)
    print(mapNegProba)

    print("proba pos")
    mapPosProba = calculOccurance(corpusTrainPos,totalWords)
    print(mapPosProba)

    valusNeg = eval(mapNegProba,corpusTestNeg)
    valusPos = eval(mapPosProba,corpusTrainPos)

    if valusPos > valusNeg:
        print("Test positive, précision", valusPos)
    else:
        print("Test negative, précision", valusNeg)


def eval(dicoMyWord, corpusTrain):
    # dicoMyWord = {}

    dicoEval = {}
    valusEval = 0
    # loadFIleToMap(FILE_DIR,dicoMyWord)

    for i in dicoMyWord:
        if i in corpusTrain:
            dicoEval[i] = corpusTrain[i]

    for i in dicoEval.keys():
        # print(" -- eval -- ")
        # print(math.log(dicoEval[i],10))
        # print(valusEval)

        # valusEval+=dicoEval[i]
        valusEval+=math.log(dicoEval[i],10)

    # print(dicoEval)
    # print("final val : " + str(valusEval))

    return valusEval


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