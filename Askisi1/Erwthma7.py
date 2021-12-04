#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 23:22:18 2021

@author: asimakis
"""

import nltk
from nltk.book import *
import string


#Erwthma 7
eng_stopwords = nltk.corpus.stopwords.words('english')
print("Stopwords της αγγλικής γλώσσας:",len(eng_stopwords),end="\n\n")

gr_stopwords = nltk.corpus.stopwords.words('greek')
print("Stopwords της ελληνικής γλώσσας:",len(gr_stopwords))



