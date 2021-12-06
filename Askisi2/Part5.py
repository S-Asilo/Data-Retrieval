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
tokens = text4[:50]

eng_stopwords = nltk.corpus.stopwords.words('english')
tokens = [x for x in tokens if x not in eng_stopwords]


bag_of_words = Counter(tokens)