#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 22:02:14 2021

@author: asimakis
"""


from nltk.book import *

# H text() περιέχει το None που δημιουργεί προβλήματα, οπότε φτιάχνουμε
# κανούρια λίστα

TextList = [text1,text2,text3,text4,text5,text6,text7,text8,text9]

#Βήμα 1 
# A)

def lexical_richness(textNumber):
    if textNumber == 1:
        return len(text1.vocab()) / len(text1)
    elif textNumber == 2:
        return len(text2.vocab()) / len(text2)
    elif textNumber == 3:
        return len(text3.vocab()) / len(text3)
    elif textNumber == 4:
        return len(text4.vocab()) / len(text4)
    elif textNumber == 5:
        return len(text5.vocab()) / len(text5)
    elif textNumber == 6:   
        return len(text6.vocab()) / len(text6)
    elif textNumber == 7:
        return len(text7.vocab()) / len(text7)
    elif textNumber == 8:
        return len(text8.vocab()) / len(text8)
    elif textNumber == 9:
        return len(text9.vocab()) / len(text9)


# 1,a

print()
print("Στατιστικά Κειμένων".center(50))

MontyKeywords = ["LAUNCELOT"]
ChatKeywords = ["omg","OMG","lol"]


for index,text in enumerate(TextList):
    if text.name in ["Monty Python and the Holy Grail", "Chat Corpus"]:
        print("".center(50,'-'),end=("\n\n"))
        print(text.name.center(50),end=("\n\n"))
        print("Το {:.2f}% των λέξεων είναι μοναδικό".format( lexical_richness(index+1)*100).center(50),end=("\n\n"))
        
        if "Monty Python and the Holy Grail" in text.name :
            for keyword in MontyKeywords:
                print("Η λέξη {}: ".format(keyword).center(50))
                print("Εμφανίζεται {} Φορές".format(text.count(keyword)).center(50))
                print("Σε ποσοστό {:.2f}%".format(text.count(keyword) / len(text) * 100).center(50),end=("\n\n") )
        else:
            for keyword in ChatKeywords:
                print("Η λέξη {}: ".format(keyword).center(50))
                print("Εμφανίζεται {} Φορές".format(text.count(keyword)).center(50))
                print("Σε ποσοστό {:.2f}%".format(text.count(keyword) / len(text) * 100).center(50),end=("\n\n") )
                

            
# 1,b
print()
print("Στατιστικά Κειμένων".center(50))

MontyKeywords.extend(["Holy","Arthur","ARTHUR"])
ChatKeywords.extend(["brb","good","hey"])



for index,text in enumerate(TextList):
    if text.name in ["Monty Python and the Holy Grail", "Chat Corpus"]:
        print("".center(50,'-'),end=("\n\n"))
        print(text.name.center(50),end=("\n\n"))
        print("Το {:.2f}% των λέξεων είναι μοναδικό".format( lexical_richness(index+1)*100).center(50),end=("\n\n"))
        
        if text.name == "Monty Python and the Holy Grail":
            for keyword in MontyKeywords:
                print("Η λέξη {}: ".format(keyword).center(50))
                print("Εμφανίζεται {} Φορές".format(text.count(keyword)).center(50))
                print("Σε ποσοστό {:.2f}%".format(text.count(keyword) / len(text) * 100).center(50),end=("\n\n") )
        else:
            for keyword in ChatKeywords:
                print("Η λέξη {}: ".format(keyword).center(50))
                print("Εμφανίζεται {} Φορές".format(text.count(keyword)).center(50))
                print("Σε ποσοστό {:.2f}%".format(text.count(keyword) / len(text) * 100).center(50),end=("\n\n") )

#Για κάποιο λόγο, βλέπουμε διαφορές ανάμεσα σε κεφαλαία και όχι, απο εκεί και πέρα παρατηρούμε ότι ένα πολύ μικρό ποσοστό των κειμένων είναι μοναδικές λέξεις
#Και από αυτές, έχοντας μόνο τον τίτλο του βιβλίου για στοιχείο, είναι δύσκολο να βρούμε λέξεις με μεγάλη συχνότητα
#αν και ακταφέραμε να βρούμε λέξεις που χρησιμοποιούνται περισσότερο από τον μέσο όρο.