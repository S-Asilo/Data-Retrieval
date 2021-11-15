#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 22:36:35 2021

@author: asimakis
"""

from nltk.book import *
import nltk.tokenize

sentence = "Monticello wasn't designated as UNESCO World Heritage Site until 1987."
gr_sentence = "Μ' άρεσε και στο 'πα."
sentence = "Why, sometimes I've believed as many as six impossible things before breakfast."


TextList = [text1,text2,text3,text4,text5,text6,text7,text8,text9]


for text in TextList:
    if "Sense and Sensibility" in text.name:
        tokens1 = text[:200]
        
join_tokens = ' '.join([t for t in tokens1])

start = 0
while( (index := join_tokens.find(".",start)) != -1):
    start = index+1
    join_tokens = join_tokens[:index-1] + join_tokens[index:]

start = 0
while( (index := join_tokens.find(",",start)) != -1):
    start = index+1
    join_tokens = join_tokens[:index-1] + join_tokens[index:]

start = 0
while( (index := join_tokens.find("'",start)) != -1):
    start = index+1
    join_tokens = join_tokens[:index-1] + join_tokens[index:]

start = 0
while( (index := join_tokens.find(";",start)) != -1):
    start = index+1
    join_tokens = join_tokens[:index-1] + join_tokens[index:]
    

print("Οι πρώτες 200 λεκτικές μονάδες του Sense and Sensibility".center(120,"-"),end = "\n\n")

print(nltk.word_tokenize(join_tokens),end= "\n\n")
print(join_tokens.split(), end="\n\n")

print("Χρήση δικών μου προτάσεων".center(120,"-"),end = "\n\n")

print("Για την πρόταση: {}".format(gr_sentence), end= "\n\n")

print(nltk.word_tokenize(gr_sentence))
print(gr_sentence.split(), end="\n\n\n")

print("Για την πρόταση: {}".format(sentence), end= "\n\n")

print(nltk.word_tokenize(sentence))
print(sentence.split(), end="\n\n")
