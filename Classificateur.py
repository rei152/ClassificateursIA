__author__ = 'andy.cheung'

import os, sys
import random

DIR_POSEV = './pos'
DIR_NEGEV = './neg'

def getCorpus(DIR):

    corpusTrain,corpusTest = [],[]

    LEN = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

    for i in range(0,int(LEN*0.1)):
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

corpusTestPos, corpusTrainPos = getCorpus(DIR_NEGEV)
corpusTestNeg, corpusTrainNeg = getCorpus(DIR_POSEV)

print(corpusTestPos)
print(corpusTrainPos)

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