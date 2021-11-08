#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 23:22:18 2021

@author: asimakis
"""

import nltk
from nltk.book import *
import string

TextList = [text1,text2,text3,text4,text5,text6,text7,text8,text9]


#Erwthma 7
eng_stopwords = nltk.corpus.stopwords.words('english')
print(len(eng_stopwords),end="\n\n")

gr_stopwords = nltk.corpus.stopwords.words('greek')
print(len(gr_stopwords))


#Erwthma 8
def clearPunctuation(token_list):
    cleared_list = []
    
    for token in token_list:
        if token not in eng_stopwords and token not in string.punctuation:
            cleared_list.append(token)
            
    return cleared_list


for text in TextList:
    if "Sense and Sensibility" in text.name:
        tokens1 = text[:200]
        

normalized_token1 = [ x.lower() for x in tokens1]

print(clearPunctuation(normalized_token1))


####needs extra text