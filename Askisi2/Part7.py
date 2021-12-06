#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:29:54 2021

@author: asimakis
"""

import nltk
from nltk.book import *
from collections import Counter
import math
import string
import copy
from collections import OrderedDict


def cosine_sim(vec1, vec2):
    vec1 = [val for val in vec1.values()]
    vec2 = [val for val in vec2.values()]
    
    dot_prod = 0
    
    for i, v in enumerate(vec1):
        dot_prod += v *vec2[i]
        
    mag_1 = math.sqrt(sum([x**2 for x in vec1]))
    mag_2 = math.sqrt(sum([x**2 for x in vec2]))
    
    
    return dot_prod / (mag_1 * mag_2)

docs = [sent4, sent7]
# docs = [text4[:], text7[:]]

all_doc_tokens = sum(docs, [])

eng_stopwords = nltk.corpus.stopwords.words('english')
all_doc_tokens = [x for x in all_doc_tokens if x.lower() not in eng_stopwords]
all_doc_tokens = [x for x in all_doc_tokens if x not in string.punctuation]

lexicon = sorted(set(all_doc_tokens))    

zero_vector = OrderedDict((token, 0) for token in lexicon)

document_tfidf_vectors = []

for doc in docs:
    vec = copy.copy(zero_vector)
    token_counts = Counter(doc)

    for key, value in token_counts.items():
        if key in all_doc_tokens:
            docs_containing_key = 0
            for _doc in docs:
                if key in _doc:
                    docs_containing_key += 1
                    
            tf = value / len(lexicon)
            if docs_containing_key:
                idf = len(docs) / docs_containing_key
            else:
                idf = 0
            vec[key] = tf * idf
    
    document_tfidf_vectors.append(vec)    
    
print(cosine_sim(document_tfidf_vectors[0], document_tfidf_vectors[1]) *100, "%")

