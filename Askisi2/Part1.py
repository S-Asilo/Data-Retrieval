#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 13:22:03 2021

@author: asimakis
"""

from nltk.book import *
import nltk.tokenize
import numpy as np

sentence1 = "Thomas Jefferson began building Monticello at the age of 26."
sentence2 = "Why, sometimes I've believed as many as six impossible things before breakfast."

sentences = [sentence1,sentence2]

token_sequences = []

for sentence in sentences:
    
    token_sequences.append(sentence.split())
    token_sequences.append(nltk.word_tokenize(sentence))    
    

for token_sequence in  token_sequences:
    
    vocab = sorted(set(token_sequence))
    
    num_tokens = len(token_sequence)
    vocab_size = len(vocab)
    
    onehot_vector = np.zeros((num_tokens, vocab_size), int)
    
    for i, word in enumerate(token_sequence):
        onehot_vector[i, vocab.index(word)] = 1
        
    print(onehot_vector, end="\n\n")
    
    
Για την πρώτη πρόταση (αυτή του κεφαλαίου 2.2), βλέπουμε ότι ο πίνακας που συμπτώσεων είναι τετραγωνικός ανεξάρτητα από την
μέθοδο κατάτμισης που χρησιμοποιείται. Αυτό γίνεται γιατί οι λεκτικές μονάδες (tokens) που παράγονται και από τις 2 μεθόδους 
είναι μοναδικές. Μπορούμε επίσης να παρατηρήσουμε ότι με τη χρήση της δεύτερης τεχνικής έχουμε νεγακλυτερο πίνακα. Αυτο αιτιολογείται
αππό την παραγωγή περισσότερων λεκτικών ομάδων με το διαχωρισμό της τελείας στο τέλος της πρότασης. Πέρα από αυτό, το αποτέλεσμα είναι ίδιο
με αυτό του παραδείγματος στο κεφαλαιο 2.2.

Όσο για τη δεύτερη πρότασση, μπορούμε να δούμε ότι με τη χρήση της split χωρίζονται οι λεκτικές μονάδες στο κενό. Ακριβώς όπως και στη πρώτη πρότααση.
Παρ' όλα αυτά, ο πίνακας δεν είναι  τετραγωνικός. Αυτό συμβαίνει επειδή υπάρχει μία λεκτική μονάδα που εμφανίζεται παραπάνω από μία φορά, η λεκτική μονάδα as.
Μπορουμε επίσης να επιβεβαιώσουμε την πρόβλεψη μας ότι έχουμε "πρόβλημα" και με άλλα σημεία στίξης λόγω του διαχωρισμού στο κενό ( Ι've).
Αυτό το πρόβλημα λύνεται με την χρήση του tokenize αν και δεν διαχωριζει τα σημεια στίξης αν βρίσκονται στην αρχή της λέξης. Ως αποτελεσμα, έχουμε το ίδιο "φαινόμενο" με τη πρώτη πρόταση.
δηλαδή περισσότερες διαστάσεις στον πίνακα μας.                            