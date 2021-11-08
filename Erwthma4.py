#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 11:36:48 2021

@author: asimakis
"""

from nltk.book import *

tokens = sent1
normalized_sent1 = [ x.lower() for x in tokens]
print(normalized_sent1)

# Παρατηρούμε ότι τα κεφαλαία έχουν γίνει πεζά συνοεριλαμβανομένου και του ονόματος,
# όπως είδαμε στις προηγουμενες ασκησεις έχουμε διαφορετικά στατιστικά για tokens σε κεφαλαία με πεζά
# πχ Arthur/ARTHUR, OMG/omg, LAUNCELOT/Lancelot κλπ. Οπότε περιμένουμε να αλλαξουν σημαντικα τα στατιστικά
# απο τα ποσοστά μεμονομένων λέξεων, ως και το πόσο πλούσιο είναι το λεξιλόγιο. 

# Δεν ξερω για αλλες εφαρμογες
# Αναζήτηση λέξεων