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


porter = nltk.PorterStemmer()
stemmed_tokens1 = [porter.stem(t) for t in tokens1]

print(stemmed_tokens1, end = "\n\n")
#normalized without ending

wn1 = nltk.WordNetLemmatizer()
lemmatized_tokens1 = [wn1.lemmatize(t) for t in tokens1]

print(lemmatized_tokens1, end = "\n\n")
#seemingly nothibg changes

for index,token in enumerate(lemmatized_tokens1):
    if token != tokens1[index]:
        print(tokens1[index], " = ", token)
        
        
#Μετά την εκτέλεσεη του παραπάνω κώδικα, βλέπουμε οτι εχουμε περιπου 10 λέξειες που αλλάζουν από το αρχικό
# στην ουσία προσπαθεί να βγάλεο τον χρόνο (από πληθυντικό σε ενικό) με αποτελεσμα να χανεται πληροφορία και 
# σε προθέσεις πχ as -> a, was -> wa

# ----------------------------------- Δικό μου κείμεντο: ----------------------------------


############################################## NEEEEEDS WORK 
print(50*"-", end = "\n\n")

my_string_root = ["I", "sat","comfortably","on","the","comfortable","sofa",".","It","was","alltogether","an","allright","day"]
my_string_plural = ["I", "told", "the", "children", "wearing", "the", "scarves", "to", "stop", ".", "All", "those", "yells", "hurt", "my", "ears"] 

plural_words = ["florae", "moose", "octopi", "warves", "abilities", "geese", "data", "mice"]

my_string_gr = ["'Ηταν", "μια", "καλή", "μέρα", "θα" ,"μπορούσε", "να" ,"ήταν", "και", "καλύτερη", "όμως" ]


stemmed_string1 = [porter.stem(t) for t in my_string_root]
print(stemmed_string1, end = "\n\n")
lemmatized_string1 = [wn1.lemmatize(t) for t in my_string_root]
print(lemmatized_string1, end = "\n\n")

stemmed_string1 = [porter.stem(t) for t in my_string_plural]
print(stemmed_string1, end = "\n\n")
lemmatized_string1 = [wn1.lemmatize(t) for t in my_string_plural]
print(lemmatized_string1, end = "\n\n")

stemmed_string1 = [porter.stem(t) for t in plural_words]
print(stemmed_string1, end = "\n\n")
lemmatized_string1 = [wn1.lemmatize(t) for t in plural_words]
print(lemmatized_string1, end = "\n\n")


#normalize as well plz
stemmed_string1 = [porter.stem(t) for t in my_string_gr]
print(stemmed_string1, end = "\n\n")
lemmatized_string1 = [wn1.lemmatize(t) for t in my_string_gr]
print(lemmatized_string1, end = "\n\n")