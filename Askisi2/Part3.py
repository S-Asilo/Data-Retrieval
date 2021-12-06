#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 23:53:01 2021

@author: asimakis
"""

import pandas as pd
import nltk.tokenize
import numpy as np
from nltk.book import *

sentence1 = "Thomas Jefferson began building Monticello at the age of 26."
sentence2 = "Why, sometimes I've believed as many as six impossible things before breakfast."
sentence3 = "Hope is a good breakfast, but it is a bad supper.” "
sentence4 = "It always seems impossible until it's done."
sentence5 = "Many hands make light work."


sentences =[sentence2,sentence3,sentence4,sentence5]

corpus = {}

for i, sent in enumerate(sentences):
    corpus['sent{}'.format(i + 2)] = dict((tok.strip('.'), 1) for tok in sent.split())
    
df = pd.DataFrame.from_records(corpus).fillna(0).astype(int)


print()

print("Ομοιότητα μεταξύ των προτάσεων 2,3,4 και 5:")
print( len([(k,v) for (k,v) in (df.sent2 & df.sent4 & df.sent3 & df.sent5).items() if v]) / len([(k,v) for (k,v) in (df.sent2 & df.sent4 & df.sent3 & df.sent5).items()])*100,"%") 


print("Ομοιότητα μεταξύ των προτάσεων 2 και 3:")
print( len([(k,v) for (k,v) in (df.sent2 & df.sent3).items() if v]) / len([(k,v) for (k,v) in (df.sent2 | df.sent3).items() if v])*100,"%")

print("Ομοιότητα μεταξύ των προτάσεων 2 και 4:")
print( len([(k,v) for (k,v) in (df.sent2 & df.sent4).items() if v]) / len([(k,v) for (k,v) in (df.sent2 | df.sent4).items() if v])*100,"%")

print("Ομοιότητα μεταξύ των προτάσεων 2 και 5:")
print( len([(k,v) for (k,v) in (df.sent2 & df.sent5).items() if v]) / len([(k,v) for (k,v) in (df.sent2 | df.sent5).items() if v])*100,"%")

print("Ομοιότητα μεταξύ των προτάσεων 3 και 4:")
print( len([(k,v) for (k,v) in ( df.sent4 & df.sent3 ).items() if v]) / len([(k,v) for (k,v) in ( df.sent4 | df.sent3 ).items() if v])*100,"%")

print("Ομοιότητα μεταξύ των προτάσεων 3 και 5:")
print( len([(k,v) for (k,v) in ( df.sent3 & df.sent5).items() if v]) / len([(k,v) for (k,v) in ( df.sent3 | df.sent5).items() if v])*100,"%")

print("Ομοιότητα μεταξύ των προτάσεων 4 και 5:")
print( len([(k,v) for (k,v) in ( df.sent4 & df.sent5).items() if v]) / len([(k,v) for (k,v) in ( df.sent4 | df.sent5).items() if v])*100,"%")



for i, sent in enumerate(sentences):
    corpus['sent{}'.format(i + 2)] = dict((tok, 1) for tok in nltk.word_tokenize(sent))
    
df = pd.DataFrame.from_records(corpus).fillna(0).astype(int)


print()

print("Ομοιότητα μεταξύ των προτάσεων 2,3,4 και 5:")
print( len([(k,v) for (k,v) in (df.sent2 & df.sent4 & df.sent3 & df.sent5).items() if v]) / len([(k,v) for (k,v) in (df.sent2 & df.sent4 & df.sent3 & df.sent5).items()]) *100,"%")
print( [(k,v) for (k,v) in (df.sent2 & df.sent4 & df.sent3 & df.sent5).items() if v])


print("Ομοιότητα μεταξύ των προτάσεων 2 και 3:")
print( len([(k,v) for (k,v) in (df.sent2 & df.sent3).items() if v]) / len([(k,v) for (k,v) in (df.sent2 | df.sent3).items() if v]) *100,"%")
print( [(k,v) for (k,v) in (df.sent2 & df.sent3).items() if v])

print("Ομοιότητα μεταξύ των προτάσεων 2 και 4:")
print( len([(k,v) for (k,v) in (df.sent2 & df.sent4).items() if v]) / len([(k,v) for (k,v) in (df.sent2 | df.sent4).items() if v])*100 ,"%")
print( [(k,v) for (k,v) in (df.sent2 & df.sent4).items() if v])

print("Ομοιότητα μεταξύ των προτάσεων 2 και 5:")
print( len([(k,v) for (k,v) in (df.sent2 & df.sent5).items() if v]) / len([(k,v) for (k,v) in (df.sent2 | df.sent5).items() if v])*100,"%")
print( [(k,v) for (k,v) in (df.sent2  & df.sent5).items() if v])

print("Ομοιότητα μεταξύ των προτάσεων 3 και 4:")
print( len([(k,v) for (k,v) in ( df.sent4 & df.sent3 ).items() if v]) / len([(k,v) for (k,v) in ( df.sent4 | df.sent3 ).items() if v])*100,"%")
print( [(k,v) for (k,v) in ( df.sent4 & df.sent3 ).items() if v])

print("Ομοιότητα μεταξύ των προτάσεων 3 και 5:")
print( len([(k,v) for (k,v) in ( df.sent3 & df.sent5).items() if v]) / len([(k,v) for (k,v) in ( df.sent3 | df.sent5).items() if v])*100,"%")
print( [(k,v) for (k,v) in ( df.sent3 & df.sent5).items() if v])

print("Ομοιότητα μεταξύ των προτάσεων 4 και 5:")
print( len([(k,v) for (k,v) in ( df.sent4 & df.sent5).items() if v]) / len([(k,v) for (k,v) in ( df.sent4 | df.sent5).items() if v])*100,"%")
print( [(k,v) for (k,v) in ( df.sent4 & df.sent5).items() if v])




sentences = [text4[:50], text7[:50]]

corpus = {}

for i, sent in enumerate(sentences):
    corpus['text{}'.format(i + 1)] = dict((tok, 1) for tok in sent)
    
df = pd.DataFrame.from_records(corpus).fillna(0).astype(int)

print()

print("Ομοιότητα μεταξύ των text4 και text7:")
print( len([(k,v) for (k,v) in (df.text1 & df.text2).items() if v]))
print( [(k,v) for (k,v) in (df.text1 & df.text2).items() if v])


# Α) Με τις προτασεις που επιλέχθηκαν, θα περιμέναμε να έχουν τουλάχιστον μια κοινή λέξη με τη πρόταση 2. Παρ' όλα αυτά, μόνο
#     η πρόταση 4 παρουσιάζει ομοιοτητα. Αυτό γίνεται λόγω της χρήσης του split καθώς μπορούμε να δούμε ότι στη πρόταση 3, μετά τη λέξη
# breakfast έχουμε ένα κόμμα. Αλλάζοντας για αυτό τον λόγο το split με το tokenize που είδαμε στα προηγούμενα ερωτήματα, βλέπουμε ότι πλέον 
# αναγνωρίζει το breakfast ως κοινη λέξη άλλα μαζί και κάθε τελεία ή κόμμα που μπορεί να έχουν ως κοινο οι προτασεις ( θόρυβος ).
# Όμως ακόμα δεν έχουμε τη λέξη many ως κοινη με τη πρόταση 5. Αυτό γίνεται λόγω της απουσίας κανονικοποίησης ( όπως είδαμε στην άσκηση 1)

# Β) Βλέπουμε ότι έχουμε 5 λέκτικές μονάδες κοινες (από 50 σύνολο το 10%). Παρ' όλα αυτά, είναι όλες προθέσεις. Άρα δεν μπορούμε να εξάγουμε συμπέρασμα
# Αν χρησιμοποιούσαμε κάποια από τις τεχνικές αφαίρεσεις των προθεσεων που είδαμε στην Άσκηση 1 τότε θα μπορουσαμε να εξάγουμε καλύτερα συμπερασματα από τα 
# αποτελέσματα μας

# όπως είδαμε μια μεγαλη ποσοστιαία ομοιοτητα δεν εχει σημασια αν υπάρχει λόγω προθεσεων και σημείων στίξης.