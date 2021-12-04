#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 19:33:03 2021

@author: asimakis
"""

from nltk.book import *
import nltk
import string

TextList = [text1,text2,text3,text4,text5,text6,text7,text8,text9]

eng_stopwords = nltk.corpus.stopwords.words('english')


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



# print(FreqDist(tokens1).most_common(50))
FreqDist(tokens1).plot(50)

# print(clearPunctuation(normalized_token1).most_common(50))
FreqDist(clearPunctuation(normalized_token1)).plot(50)

