#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 10:59:05 2019

@author: nacho
"""

import sys
#p= r'D:\Doctorado\codigo'
p='/media/nacho/DatosHD/Doctorado/CBMS2019/codigo'
sys.path.append(p)

#import unicodedata
import pandas as pd
import numpy as np
from numpy import exp, log, dot, zeros, outer, random, dtype, float32 as REAL,\
    double, uint32, seterr, array, uint8, vstack, fromstring, sqrt, newaxis,\
    ndarray, empty, sum as np_sum, prod, ones, ascontiguousarray, vstack
    
import collections
from six import iteritems, itervalues, string_types
from six.moves import xrange
from gensim import utils, matutils

from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors

import logging

# Carga del Modelo elegido, según de la funcion snomed2vec.load.
# Utilzia el modelo entrenado Word2Vec, (Word vectors)y el modelo generado final Snomed2Vec.(Sentence vectors)

def snomed2vec_load(typeModel=0):
    """ 
    Dependiendo del parámetro typeModel, se carga los siguientes modelos preentrenados (Word2Vec):
    1. typeModel=0 -> Modelo entrenado con los (Informes de ALta de urgencia + Descripcion Snomed-CT)
    2. typeModel=1 -> Modelo entrenado con wikipedia en español + Descripción Terminos Snomed-CT.

    """
    if typeModel==0: #Modelo Informes de Alta + Descripciones Snomed-CT
        print('Modelo entrenado con los Informes de Alta de Urgencias + Descripciones de Snomed-CT')
        fich = './Models/SKs300w8m1-InfAltSnomed.txt'
        fSnomed = './Models/Snomed2Vec-SK300-IA-Snomed-v1.npy'
        
    elif typeModel==1: #Modelo Wikipedia
        print('Modelo entrenado con la Wikipedia en Español')
        fich = '/Models/SKs300w5m1-wikipedia.txt'
        fSnomed = '/Models/Snomed2Vec-CBoW300-Wiki-Op3.npy'
    
    f = fich
    fSno = fSnomed
    cols=['idConcept','jerarquia','corpusTerm','vecSnom','concept']
    print('Carga del Modelo Snomed2Vec tipo:(%s)' % str(typeModel))
    with open(fSnomed,'rb') as np_file:
        data = np.load(np_file)
    
    return KeyedVectors.load_word2vec_format(f, binary=False), pd.DataFrame(data, columns=cols)


    
# Definiciones necesarias:
# Definir las siguientes varibles globales.
# Matriz formada por el tamaño global del vocabulario "vocab" y el tamaño "size" del vector de la palabra

#Entrada: Se le pasa el dataframe SnomedWork


def init_vars(data):
    vector_size = len(data['vecSnom'][0])
    vocab_size = len(data['vecSnom'])
    print(vector_size)
    print(vocab_size)
    
    logging.info("precomputing L2-norms of word weight vectors")
    
    index2word = data['concept'].tolist() # map from a word's matrix index (int) to word (string)
    
    syn0 = np.array(data['vecSnom'].tolist(), dtype=REAL)
    syn0[np.isnan(syn0)] = 0.0
    
    syn0norm = zeros((vocab_size, vector_size), dtype=REAL)
    np.seterr(divide='ignore', invalid='ignore')
    
    syn0norm = (syn0 / sqrt((syn0 ** 2).sum(-1))[..., newaxis]).astype(REAL)
    
    
    return syn0, index2word, syn0norm

def vectorSnomed(lstgrams,model,size):
    output=[]
    buffer=np.zeros((size,), dtype=np.float32)
    for item in lstgrams:
        try:
            buffer = buffer + model.word_vec(item)
        except:
            buffer = buffer + np.zeros((size,), dtype=REAL)
    return buffer


def mas_similar(positive, model, topn):
    
    vector=vectorSnomed(positive,model,300)
    vectorNorm = (vector / sqrt((vector ** 2).sum(-1))[..., newaxis]).astype(REAL)
    
    mean = []
    mean.append(vectorNorm)
    mean = matutils.unitvec(array(mean).mean(axis=0)).astype(REAL)
        
    limited = syn0norm
    dists = dot(limited, mean)
    dists[np.isnan(dists)] = 0.0
    
    best = matutils.argsort(dists, topn=topn, reverse=True)
        
    result = [(index2word[sim], float(dists[sim])) for sim in best]
    return result[:topn]


def similares(term, jer='all', nMax=3):
    term = str(term)
    queryTerm=term.split()
    lst=[]
    jerarquia=[]
    bufJer=''
    buffer=mas_similar(queryTerm, w2vModel, topn=1000)
    
    for indice in range(len(buffer)):
        
        buffJer = buffer[indice][0].split('|')[-1]
        jerarquia.append(buffJer)
        totalJer = collections.Counter(jerarquia)
        if jer == 'all':
            if totalJer[buffJer]<=nMax:
                lst.append(buffer[indice])
        elif buffJer == jer:
            if totalJer[buffJer]<=nMax:
                lst.append(buffer[indice])

        #print(buffer[i])
    return lst, totalJer



# Pruebas de Ejecucion de codigo para test:
# Ejemplo de Carga del modelo type=0 -------------------
# 1.0 --- w2vModel, SnomedWork = snomed2vec_load(0)
# Comrobacion del DataFrame:
# 1.1 --- SnomedWork.head()
# 2.0 --- syn0, index2word, syn0norm = init_vars(SnomedWork)
# parámetro de Entrada: "frase para buscar sus conceptos clínicos"
# 3.0 --- sent = 'infarto miocardio agudo'
# 3.1 --- result, jerarquias = similares(sent, jer='all',nMax=3)
    

