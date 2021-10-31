#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 18:47:01 2021

@author: asimakis
"""

from nltk.book import *


# Δοκίμασε να κανεις και concordance στις λεξεις κλειδια (whale etc)

print(FreqDist(text1).most_common(50))
FreqDist(text1).plot(50)

#Έχει να κάνει με μια φάλαινα γιατί είναι το μόνο ουσιαστικό στις top 50
#Από κει και πέρα μπορούμε να δούμε ότι δεν έχουμε γυναίκα πρωταγωνιστή καθώς
#δεν έχουμε hee/she/hers μόνο him/his etc. Δεν μπορουμε να εξάγουμε περισσότερα συμπεράσματα
# επειδή οι top 50 λέξεις είναι άρθρα κλπ.

print()
print(FreqDist(text6).most_common(50))
FreqDist(text6).plot(50)

#Ιππότες της στρογγυλής τραπέζης, Βλεπουμε οτι και στα 2 εχουμε τεραστια συγκεντρωση στα σημεια στιξης
#ARTHUR