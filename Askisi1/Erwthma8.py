#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 05:00:06 2021

@author: asimakis
"""

import nltk
from nltk.book import *
import string

TextList = [text1,text2,text3,text4,text5,text6,text7,text8,text9]

#Erwthma 8

eng_stopwords = nltk.corpus.stopwords.words('english')
gr_stopwords = nltk.corpus.stopwords.words('greek')

def clearEngPunctuation(token_list):
    cleared_list = []
    
    for token in token_list:
        if token not in eng_stopwords and token not in string.punctuation:
            cleared_list.append(token)
            
    return cleared_list

def clearGrePunctuation(token_list):
    cleared_list = []
    
    for token in token_list:
        if token not in gr_stopwords and token not in string.punctuation:
            cleared_list.append(token)
            
    return cleared_list


for text in TextList:
    if "Sense and Sensibility" in text.name:
        tokens1 = text[:200]
        

normalized_token1 = [ x.lower() for x in tokens1]

print("Οι πρώτες 200 λεκτικές μονάδες του Sense and Sensibility".center(120,"-"),end = "\n\n")

print()
print(clearEngPunctuation(normalized_token1))

print()
print("Χρήση δικών μου προτάσεων".center(120,"-"),end = "\n\n")

my_string_gr = ["'Ηταν", "μια", "καλή", "μέρα", "θα" ,"μπορούσε", "να" ,"ήταν", "και", "καλύτερη", "όμως" ]
normalized_string = [x.lower() for x in my_string_gr]

print()
print(clearGrePunctuation(normalized_string))

my_string_root = ["I", "sat","comfortably","on","the","comfortable","sofa",".","It","was","alltogether","an","allright","day"]
normalized_string = [x.lower() for x in my_string_root]

print()
print(clearEngPunctuation(normalized_string))

####needs extra text