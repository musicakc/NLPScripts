from nltk.corpus import wordnet as wn
import numpy as np

xsyn = wn.synsets('information')

ysyn = wn.synsets('retrieval')

#print xsyn
#print ysyn

xlen = len(xsyn)
ylen = len(ysyn)

simindex = np.zeros((xlen,ylen))
#print simindex

def relative_matrix(asyn,bsyn,simindex):
    i = -1
    j = -1
    cb = []
    ib = []

    for asyn_element in asyn:
        i +=1
        cb = wn.synset(asyn_element.name)
        j = -1
        for bsyn_element in bsyn:
            j += 1
            i = wn.synset(bsyn_element.name)
            if not cb.pos == ib.pos:
                continue
            score = cb.wup_similarity(ib)
            r = cb.path_similarity(ib)
            if simindex[i,j] < score:
                simindex[i,j] = score

relative_matrix(xsyn,ysyn,simindex)
print simindex
