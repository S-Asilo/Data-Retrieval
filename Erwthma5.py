#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 15:44:58 2021

@author: asimakis
"""

from nltk.book import *
import nltk

nltk.download("wordnet")


TextList = [text1,text2,text3,text4,text5,text6,text7,text8,text9]


for text in TextList:
    if "Sense and Sensibility" in text.name:
        tokens1 = text[:200]


print("Οι πρώτες 200 λεκτικές μονάδες του Sense and Sensibility".center(120,"-"),end = "\n\n")


normalized_tokens1 = [x.lower() for x in tokens1]
print("Μετά την κανονικοποίηση:")
print(normalized_tokens1,end= "\n\n")

porter = nltk.PorterStemmer()
stemmed_tokens1 = [porter.stem(t) for t in tokens1]

print("Μετά την εφαρμογή stemming:")
print(stemmed_tokens1, end = "\n\n")
#normalized without ending

wn1 = nltk.WordNetLemmatizer()
lemmatized_tokens1 = [wn1.lemmatize(t) for t in tokens1]

print("Μετά την εφαρμογή lemmatization:")
print(lemmatized_tokens1, end = "\n\n")
#seemingly nothibg changes

print("Αλλαγές μετά την εφαρμογή lemmatization")
for index,token in enumerate(lemmatized_tokens1):
    if token != tokens1[index]:
        print("To {} άλλαξε σε {}".format(tokens1[index], token))
        
        
#Μετά την εκτέλεσεη του παραπάνω κώδικα, βλέπουμε οτι εχουμε περιπου 10 λέξειες που αλλάζουν από το αρχικό
# στην ουσία προσπαθεί να βγάλεο τον χρόνο (από πληθυντικό σε ενικό) με αποτελεσμα να χανεται πληροφορία και 
# σε προθέσεις πχ as -> a, was -> wa

# ----------------------------------- Δικό μου κείμεντο: ----------------------------------


print("\n")
print("Χρήση δικών μου προτάσεων".center(120,"-"),end = "\n\n")


my_string_root = ["I", "sat","comfortably","on","the","comfortable","sofa",".","It","was","alltogether","an","allright","day"]
my_string_plural = ["I", "told", "the", "children", "wearing", "the", "scarves", "to", "stop", ".", "All", "those", "yells", "hurt", "my", "ears"] 
my_string_gr = ["'Ηταν", "μια", "καλή", "μέρα", "θα" ,"μπορούσε", "να" ,"ήταν", "και", "καλύτερη", "όμως" ]



my_string = " ".join(my_string_root)

print("Για την πρόταση: {}".format(my_string), end= "\n\n")

print("Μετά την κανονικοποίηση:")
normalized_string1 = [x.lower() for x in my_string_root]
print(normalized_string1, end="\n\n")

print("Μετά την εφαρμογή stemming:")
stemmed_string1 = [porter.stem(t) for t in my_string_root]
print(stemmed_string1, end = "\n\n")

print("Μετά την εφαρμογή lemmatization:")
lemmatized_string1 = [wn1.lemmatize(t) for t in my_string_root]
print(lemmatized_string1, end = "\n\n\n")


my_string = " ".join(my_string_plural)

print("Για την πρόταση: {}".format(my_string), end= "\n\n")

print("Μετά την κανονικοποίηση:")
normalized_string1 = [x.lower() for x in my_string_plural]
print(normalized_string1, end="\n\n")

print("Μετά την εφαρμογή stemming:")
stemmed_string1 = [porter.stem(t) for t in my_string_plural]
print(stemmed_string1, end = "\n\n")

print("Μετά την εφαρμογή lemmatization:")
lemmatized_string1 = [wn1.lemmatize(t) for t in my_string_plural]
print(lemmatized_string1, end = "\n\n\n")


plural_words = ["florae", "moose", "octopi", "warves", "abilities", "geese", "data", "mice"]
print("Για τις λέξεις: {}".format(plural_words), end= "\n\n")

print("Μετά την εφαρμογή stemming:")
stemmed_string1 = [porter.stem(t) for t in plural_words]
print(stemmed_string1, end = "\n\n")

print("Μετά την εφαρμογή lemmatization:")
lemmatized_string1 = [wn1.lemmatize(t) for t in plural_words]
print(lemmatized_string1, end = "\n\n\n")


my_string = " ".join(my_string_gr)

print("Για την πρόταση: {}".format(my_string), end= "\n\n")

print("Μετά την κανονικοποίηση:")
normalized_string1 = [x.lower() for x in my_string_gr]
print(normalized_string1, end="\n\n")

print("Μετά την εφαρμογή stemming:")
stemmed_string1 = [porter.stem(t) for t in my_string_gr]
print(stemmed_string1, end = "\n\n")

print("Μετά την εφαρμογή lemmatization:")
lemmatized_string1 = [wn1.lemmatize(t) for t in my_string_gr]
print(lemmatized_string1, end = "\n\n")