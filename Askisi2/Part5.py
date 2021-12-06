#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 20:28:21 2021

@author: asimakis
"""

import nltk
from nltk.book import *
from collections import Counter
import math


def cosine_sim(vec1, vec2):
    vec1 = [val for val in vec1.values()]
    vec2 = [val for val in vec2.values()]
    
    dot_prod = 0
    
    for i, v in enumerate(vec1):
        dot_prod += vec2[i]
        
    mag_1 = math.sqrt(sum([x**2 for x in vec1]))
    mag_2 = math.sqrt(sum([x**2 for x in vec2]))
    
    
    return dot_prod / (mag_1 * mag_2)


# Needs vectorization
tokens = [text4[:50], text7[:50]]

# document_vector = []
# doc_length = len(tokens)

# eng_stopwords = nltk.corpus.stopwords.words('english')
# tokens = [x for x in tokens if x not in eng_stopwords]
# bag_of_words = Counter(tokens)

# for key, value in bag_of_words.most_common():   
#     document_vector.append(value / doc_length)
    
all_doc_tokens = sum(tokens, [])

lexicon = sorted(set(all_doc_tokens))    
# print(len(lexicon))

from collections import OrderedDict

zero_vector = OrderedDict((token, 0) for token in lexicon)

# print(zero_vector) 

import copy

doc_vectors = []
for doc in tokens:
    vec = copy.copy(zero_vector)
    token_counts = Counter(doc)
    
    for key, value in token_counts.items():
        vec[key] = value / len(lexicon)
    
    doc_vectors.append(vec)
    
    
# print(len(doc_vectors))

# print(doc_vectors[0])