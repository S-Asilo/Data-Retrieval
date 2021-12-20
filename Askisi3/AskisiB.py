#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 20:02:37 2021

@author: asimakis
"""


import nltk
nltk.download('words')
from nltk.corpus import words



memo = {}
def levenshtein(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    cost = 0 if s[-1] == t[-1] else 1
       
    i1 = (s[:-1], t)
    if not i1 in memo:
        memo[i1] = levenshtein(*i1)
    i2 = (s, t[:-1])
    if not i2 in memo:
        memo[i2] = levenshtein(*i2)
    i3 = (s[:-1], t[:-1])
    if not i3 in memo:
        memo[i3] = levenshtein(*i3)
    res = min([memo[i1]+1, memo[i2]+1, memo[i3]+cost])
    
    return res


correct_words = words.words()
incorrect_words=['aminal', 'liveli', 'fatnatsic','doog', 'trup']

for word in incorrect_words:
    temp = [(levenshtein(word, w),w) for w in correct_words if w[0]==word[0]]
    print(sorted(temp, key = lambda val:val[0])[0][1])


f = open("Dictionaries/Greek_utf8.dic")
correct_gr_words = []

f.readline()

for line in f:
    line = line[:-1] #stripping new line
    correct_gr_words.append(line)

incorrect_gr_words = ["καλιμερα", "καναρήνι", "πουλωβαιρ", "καθώματσαι", "ταιλιο"]

for word in incorrect_gr_words:
    temp = [(levenshtein(word, w),w) for w in correct_gr_words if w[0]==word[0]]
    print(sorted(temp, key = lambda val:val[0])[0][1])
    
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams

for word in incorrect_gr_words:
    temp = [(jaccard_distance(set(ngrams(word, 2)),
                              set(ngrams(w, 2))),w)
            for w in correct_gr_words if w[0]==word[0]]
    print(sorted(temp, key = lambda val:val[0])[0][1])