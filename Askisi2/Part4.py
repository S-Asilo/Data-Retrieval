#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:21:45 2021

@author: asimakis
"""

import nltk
from nltk.book import *
from nltk.stem import PorterStemmer
import string


def RemovePunctuation(list):
    eng_stopwords = nltk.corpus.stopwords.words('english')
    cleared_list = []
    normalized_token = [ x.lower() for x in list]
    
    for token in normalized_token:
        if token not in eng_stopwords and token not in string.punctuation:
            cleared_list.append(token)

    return cleared_list

# print(RemovePunctuation(text4[:50]))

stemmer = PorterStemmer()
pos_index = {}
textno = 0
text_map = {}

sentences = [text4[:50],text7[:50]]
text_names = ["text4", "text7"]

for sentence in sentences:
    final_token_list = RemovePunctuation(sentence)
    
    for pos, term in enumerate(final_token_list):
        term = stemmer.stem(term)
        
        if term in pos_index:
            pos_index[term][0] = pos_index[term][0] + 1
            
            if textno in pos_index[term][1]:
                pos_index[term][1][textno].append(pos)
                
            else:
                pos_index[term][1][textno] = [pos]
        
        else:
            pos_index[term] = []
            pos_index[term].append(1)
            pos_index[term].append({})
            pos_index[term][1][textno] = [pos]
            

    textno += 1
    
for index, name in enumerate(text_names):
    text_map[index] = name
    

for sentence in sentences:
    tmp = FreqDist(RemovePunctuation(sentence)).most_common(3)
    
    for tmp_string,freq in tmp:
        sample_pos_index = pos_index[ stemmer.stem(tmp_string)]
        file_list = sample_pos_index[1]
        print("Η λεκτική μονάδα", tmp_string, "εμφανίζεται στα κείμενα και θέσεις:")
        for fileno, positions in file_list.items():
            print(text_map[fileno], positions)
            
