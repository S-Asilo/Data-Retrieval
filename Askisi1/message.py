
from nltk import PorterStemmer, WordNetLemmatizer
from nltk.book import text2

def main():
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    print("## 200 Λέξεις του Sense and Sensibility", end="\n\n")
    print("\\footnotesize", end="\n\n")
    print("Original:", end="\n\n")
    print(' '.join([t for t in text2[0:200]]), end="\n\n")
    print("After naive normalization:", end="\n\n")
    print(' '.join([t.lower() for t in text2[0:200]]), end="\n\n")
    print("After stemming:", end="\n\n")
    print(' '.join([stemmer.stem(t) for t in text2[0:200]]), end='\n\n')
    print("After lemmatization:", end="\n\n")
    print(' '.join([lemmatizer.lemmatize(t) for t in text2[0:200]]), end='\n\n')
    print("\\normalsize", end="\n\n")

    # John McAfee
    sent1 = ["Software", "production", "is", "unlike", "any", "other", "production", "that", "preceded", "it", "."]
    sent2 = ["The", "octopi", "moved", "from", "the", "facilities", "into", "the", "fora", "and", "greeted", "the", "mice", ",", "the", "dwarves", "and", "the", "geese", "."]

    # Java για λίγους σελίδα 230
    prot1 = ["Αναφέρθηκε", "προηγούμενα", "ότι", "δύο", "(", "ή", "περισσότερα", ")", "νήματα", "που", "προσέρχονται", "από", "το", "ίδιο", "εκτελέσιμο", "πρόγραμμα", "μοιράζονται", "τον", "ίδιο", "χώρο", "μνήμης", "."]
    prot2 = ["Εδώ", "είναι", "η", "κατάλληλη", "στιγμή", "να", "γίνουμε", "περισσότερο", "συγκεκριμένοι", "."]

    sentences = [sent1, sent2, prot1, prot2]

    for i, sent in enumerate(sentences):
        print(f"## Sentence #{i+1}", end="\n\n")
        print("Original:", end="\n\n")
        print(sent, end="\n\n")
        print("After naive normalization:", end="\n\n")
        print([t.lower() for t in sent], end="\n\n")
        print("After stemming:", end="\n\n")
        print([stemmer.stem(t) for t in sent], end="\n\n")
        print("After lemmatization:", end="\n\n")
        print([lemmatizer.lemmatize(t) for t in sent], end="\n\n")
        print(end="\n\n")


if __name__ == "__main__":
    main()
