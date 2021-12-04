#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 21:12:44 2021

@author: asimakis
"""

import pandas as pd
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
        
    print(pd.DataFrame(onehot_vector,columns = vocab, index = token_sequence))
    
    
Η κάθε γραμμή, όπως το έχω βάλει να φαίνεται, αναπαριστά την κάθε λέκτική μονάδα της πρότασης που εξετάζουμε.
Αν δεν είχαμε βάλει το όρισμα index, θα είχαμε νούμερα που θα ήταν και η θέση των λεκτικών μονάδων στη λίστα token_sequence

και αλλα ; ???