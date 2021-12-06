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
# tokens = [text6[:], text7[:]]
    
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
    
    
print("Η ομοιότητα των κειμένων 4 και 7 είναι:")    
print(cosine_sim(doc_vectors[0], doc_vectors[1]) * 100, "%")

# Αρχικα, η πρωτη παρατηρηση που κανουμε εχει να κανει σχετικα με τον χρονο εκτελεσης του προγραμματος που ειναι σημαντικα μεγαλυτερος
# από αυτό του προηγούμενου ερωτήματος ανάλογα δηλαδή με το μέγεθος των κειμένων που επεξεργαζόμαστε. Η δεύερη παρατηρηση που εχουμε να 
# κάνουμε είναι σχετικη με το αποτέλεσμα. Ότι το ποσοστό ομοιότητας είναι πολύ μικρό, μόλις 16%. Από τη στιγμή που έχουμε αφαιρέσει τις 
# περιτές λέξεις και τα σημεία στιξης  άρα οι λέξεις που έχουν απομείνει είναι αυτες που κοθβαλάνε το νόημα του κειμένου οδηγούμαστε στο 
# συμπέρασμα ότι τα κείμενα έχουν ελάχιστη σχέση το ένα με το άλλο. Παρ' όλα αυτά, αν συγκρίνουμε το κείμενο 6 που ειναι το Monty Python and the Holy Grail,  
# με το 7 που ειναι το Wall Street journal, βλεπουμε οτι η ομοιότητα είναι μόλις 6,7 % άρα ίσως το 16% υποδηλώνει διαφορές στο λεξιλόγιο (ίσως λόγω συγγραφεα)
# άλλα ομοιότητες στον τόνο και το νόημα των κειμένων. Δυστυχώς χωρίς περισσότερες πληροφορίες(όπως κείεμνα σχετικά με το ίδιο θέμα ή κείμενα του ίδιου συγγραφέα) 
# δεν μπορούμε να καταλήξουμε σε καλύτερα συμπεράσματα