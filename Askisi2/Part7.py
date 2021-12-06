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
from nltk.tokenize import TreebankWordTokenizer
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
    
print("Η ομοιότητα των πρώτων προτάσεων για τα κείμενα 4 και 7 είναι:")    
print(cosine_sim(document_tfidf_vectors[0], document_tfidf_vectors[1]) *100, "%")

# Σε σχέση με το προηγούμενο ερώτημα, μπορούμε να δουμε ότι το ποσοστό ομοιότητα είναι το ίδιο. Άρα αυτή η μέθοδος δεν μας
# προσφέρει κάτι καινούριο από αυτή τη πλευρά. Το πλεονέκτημα που μας παρέχει είναι η δυνατότητα της αναζήτησης. Να βρούμε 
# δηλαδή ποια από τις 2 αυτες προτασεις είναι πιο σχετική συγκριτικά με ένα query

tokenizer = TreebankWordTokenizer()

query1 = "Which document talks about the senate ?"
query2 = "Who is in the House of Representatives ?"
query3 = "board of directors"
query4 = "Pierre Vinken"


query1_vec = copy.copy(zero_vector)

tokens = tokenizer.tokenize(query1.lower())
token_counts = Counter(tokens)

for key, value in token_counts.items():    
    docs_containing_key = 0    
    for _doc in docs:
        if key in _doc:
            docs_containing_key += 1
            
    if docs_containing_key == 0:
        continue
    
    tf = value /len(tokens)
    idf = len(docs) / docs_containing_key
    query1_vec[key]= tf*idf

