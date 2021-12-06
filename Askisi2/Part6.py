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
import string

def cosine_sim(vec1, vec2):
    vec1 = [val for val in vec1.values()]
    vec2 = [val for val in vec2.values()]
    
    dot_prod = 0
    
    for i, v in enumerate(vec1):
        dot_prod += v* vec2[i]
        
    mag_1 = math.sqrt(sum([x**2 for x in vec1]))
    mag_2 = math.sqrt(sum([x**2 for x in vec2]))
    
    
    return dot_prod / (mag_1 * mag_2)


tokens = [text4[:], text7[:]]
    
all_doc_tokens = sum(tokens, [])


eng_stopwords = nltk.corpus.stopwords.words('english')
all_doc_tokens = [x for x in all_doc_tokens if x.lower() not in eng_stopwords]
all_doc_tokens = [x for x in all_doc_tokens if x not in string.punctuation]


lexicon = sorted(set(all_doc_tokens))    
# print(lexicon)

from collections import OrderedDict

zero_vector = OrderedDict((token, 0) for token in lexicon)
# print(len(zero_vector))


import copy

doc_vectors = []
for doc in tokens:
    vec = copy.copy(zero_vector)
    token_counts = Counter(doc)
    
    for key, value in token_counts.items():
        if key in all_doc_tokens:
            vec[key] = value / len(lexicon)
    
    doc_vectors.append(vec)
    
print(cosine_sim(doc_vectors[0], doc_vectors[1]))
