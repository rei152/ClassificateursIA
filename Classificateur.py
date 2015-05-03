# ------------------------------
# Ahthors : Andy Cheung, Eddy Strambini
# -----------------------------

import codecs

import os, sys
import random,math

DIR_POSEV = './pos'
DIR_NEGEV = './neg'

corpus = {}

corpusTestPos = {}
corpusTestNeg = {}

corpusTrainPos = {}
corpusTrainNeg = {}

totalMotsPos = 0
totalMotsNeg = 0

global DIR_NEGEV
global DIR_POSEV


# ------------------------------
# map mots -> occurence
# -----------------------------
def loadFile_TAGGED(DIR):
    # print("--- lecture fichier ---")

    dico = {}

    # Open a file
    file = codecs.open(DIR, "r",'utf-8')
    line = file.read()

    dicoSplit = line.split('\n')

    for i in range(len(dicoSplit)-1):
        try:
            mot = dicoSplit[i].split('\t')[2].rstrip('\r')
        except IndexError:
            mot = dicoSplit[i].rstrip('\r')

        if(mot in dico):
            dico[mot] += 1
        else:
            dico[mot] = 1

    # Close opend file
    file.close()

    return dico

# ------------------------------
# Récupère une liste de fichier dans un dossier
# Calcule et séparer la liste entre le corpsus et les tests
# -----------------------------
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
        if(n > int(len(f) * 0.2)):
            # corpusTrain = loadFile_TAGGED(mapWord, DIR+"/"+f[n])
            corpusTest = loadFile_TAGGED(DIR+"/"+f[n])
        else:
            corpusTrain = loadFile_TAGGED(DIR+"/"+f[n])

    return corpusTrain,corpusTest

# ------------------------------
# Charge les mots dans une map et compte leurs appararitions
# -----------------------------
def loadFIleToMap(DIR, mapToPopulate):

    # Open a file
    file = codecs.open(DIR, "r",'utf-8')
    line = file.read()
    dicoSplit = line.split('\n')

    for i in range(len(dicoSplit)):
        try:
            mot = dicoSplit[i].split('\t')[2].rstrip('\r')
        except IndexError:
            mot = dicoSplit[i].rstrip('\r')

        if(mot in mapToPopulate):
            mapToPopulate[mot] += 1
        else:
            mapToPopulate[mot] = 1

    # Close opend file
    file.close()

# ------------------------------
# Enlève les mots d'une map à partir d'une liste
# -----------------------------
def removeForbidden(wordsMap, forbiddenList):

    tmpMap = wordsMap.copy()

    for i in wordsMap:
        if i in forbiddenList:
            tmpMap.pop(i,None)

    return tmpMap

# ------------------------------
# Fonction Bayes
# -----------------------------
def BayesFunction(isForbidden = 1):
    forbidden = {}

    loadFIleToMap("frenchST.txt", forbidden)
    forbiddenWords = forbidden.keys()

    corpusTrainNeg, corpusTestNeg = getFolderList_TAGGED("./tagged/neg")
    corpusTrainPos, corpusTestPos = getFolderList_TAGGED("./tagged/pos")

    if isForbidden == 0:
        corpusTrainNeg = removeForbidden(corpusTrainNeg,forbiddenWords)
        corpusTestNeg = removeForbidden(corpusTestNeg,forbiddenWords)
        corpusTrainPos = removeForbidden(corpusTrainPos,forbiddenWords)
        corpusTestPos = removeForbidden(corpusTestPos,forbiddenWords)

    # mapNegWords = corpusTrainNeg.update(corpusTestNeg)
    # mapPosWords = corpusTrainPos.update(corpusTestPos)
    # mapNegProba = {}
    # mapPosProba = {}
    # print("corpusTestNeg")
    # print(corpusTestNeg)
    # print("corpusTestPos")
    # print(corpusTestPos)

    # totalWords = len(corpusTrainNeg) + len(corpusTrainPos)
    corpus = mergeMaps(corpusTrainNeg, corpusTrainPos)
    # print("corpus len: ", len(corpus))
    totalWords = len(corpus)
    # corpus = dict(corpusTrainNeg.items() + corpusTrainPos.items())

    # print("Corpsu: ", corpus)
    # print(totalWords)
    # print("Negative words")
    # print(mapNegWords)
    # print(len(mapNegWords))
    #
    # print("Positive words")
    # print(mapPosWords)
    # print(len(mapPosWords))
    # print("proba neg")
    #
    # print("totalWords",totalWords)
    mapNegProba = calculOccurance(corpusTrainNeg, totalWords)

    print(len(corpusTrainNeg))
    # print("proba pos")

    mapPosProba = calculOccurance(corpusTrainPos, totalWords)
    print("mapPosProba",len(mapPosProba))

    valusNeg = eval(mapNegProba, corpusTrainNeg)
    valusPos = eval(mapPosProba, corpusTrainPos)

    checkPrecision(corpusTrainPos,corpusTestPos,corpusTrainNeg,corpusTestNeg)

    if valusPos > valusNeg:
        print("Test positive, précision", valusPos)
    else:
        print("Test negative, précision", valusNeg)


# ------------------------------
# Test sur le corpus test avec le corpus train
# -----------------------------
def checkPrecision(corpusTrainPos,corpusTestPos,corpusTrainNeg,corpusTestNeg):

    countNeg = 0
    countPos = 0

    for i in corpusTestNeg:
        if  i not in corpusTrainPos:
            countNeg+=1

    for i in corpusTestPos:
        if i not in corpusTrainNeg:
            countPos+=1

    pourcentagePos = countPos/len(corpusTestPos)*100
    pourcentageNeg = countNeg/len(corpusTestNeg)*100

    print("Mot positive correctement classe ",pourcentagePos)
    print("Mot negative correctement classe ",pourcentageNeg)


# ------------------------------
# Fusionne deux maps
# -----------------------------
def mergeMaps(dicoA, dicoB):

    newDico = dicoA.copy()

    for i in dicoB.keys():
        if i in dicoA.keys():
            newDico[i]+= dicoB[i]

        else:
            newDico[i] = dicoB[i]

    return newDico


# ------------------------------
# Fonction évaluation
# -----------------------------
def eval(dicoMyWord, corpusTrain):
    # dicoMyWord = {}
    # print(corpusTrain)
    # print(dicoMyWord)

    dicoEval = {}

    valueTotal = 1.0
    # loadFIleToMap(FILE_DIR,dicoMyWord)

    for i in dicoMyWord.keys():
        if i in corpusTrain:
            dicoEval[i] = dicoMyWord[i]

    for i in dicoEval.keys():
        # valueLog = math.log(math.pow(dicoEval[i],corpusTrain[i]))
        # valusEval+=dicoEval[i]

        valusEval= math.pow(dicoEval[i],corpusTrain[i])
        valueLog = math.log(valusEval)

        # print(" ---------------- new ------------------- ")
        # print("mot: ", i)
        # print("dicoEval[i]",dicoEval[i])
        # print("corpusTrain[i]",corpusTrain[i])
        # print("valusEval",valusEval)
        # print("valueLog",valueLog)
        # print("valueTotal",valueTotal)

        valueTotal+=valueLog

        # print(" -- valuesEval -- ")
        # print(valusEval)
        #
        # print()

    valueTotal += math.log(0.5)
    # valueTotal *= 0.5

    # print("valueTotal ",valueTotal)

    # print(dicoEval)
    # print("final val : " + str(valusEval))

    return valueTotal

# ------------------------------
# Permet de calculer les ocurances des mots
# -----------------------------
def calculOccurance(mapWord,totalWord):
    newMap = {}

    for i in mapWord:
        newMap[i] =( mapWord[i] + 1 )/ (len(mapWord) + totalWord)
        # print("len(mapWord)",len(mapWord))
        # print("newMap[i]", newMap[i])
        # print("totalWord",totalWord)
        # print(" --- occurance calcule --- ")
        # print(newMap[i])

    return newMap

def main():
    print("----------- sans traitement ------------")
    BayesFunction()

    print("----------- avec traitement ------------")
    BayesFunction(0)

if __name__ == '__main__':
    main()
