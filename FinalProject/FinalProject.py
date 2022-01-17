import nltk
from nltk.book import *
import string
from collections import Counter
import math
from rank_bm25 import BM25Okapi

tok_text = [text1,text2,text3,text4,text5,text6,text7,text8,text9]

bm25 = BM25Okapi(tok_text)

query = "white whale"

tokenized_query = query.split(" ")

results = bm25.get_top_n(tokenized_query, tok_text, n=3)


print()
print("Results using BM25")
for i in results:
    print(i)
print()


# Second ranking alg

def cosine_sim(vec1, vec2):
    vec1 = [val for val in vec1.values()]
    vec2 = [val for val in vec2.values()]
    
    dot_prod = 0
    
    for i, v in enumerate(vec1):
        dot_prod += v *vec2[i]
        
    mag_1 = math.sqrt(sum([x**2 for x in vec1]))
    mag_2 = math.sqrt(sum([x**2 for x in vec2]))
    
    
    return dot_prod / (mag_1 * mag_2)


tok = []
for text in tok_text:
    tok.append(text[:])
    
all_doc_tokens = sum(tok, [])
all_doc_tokens = [x.lower() for x in all_doc_tokens]

eng_stopwords = nltk.corpus.stopwords.words('english')
all_doc_tokens = [x for x in all_doc_tokens if x.lower() not in eng_stopwords]
all_doc_tokens = [x for x in all_doc_tokens if x not in string.punctuation]

lexicon = sorted(set(all_doc_tokens))    

from collections import OrderedDict

zero_vector = OrderedDict((token, 0) for token in lexicon)

import copy

doc_vectors = []
for doc in tok:
    vec = copy.copy(zero_vector)
    token_counts = Counter(doc)
    
    for key, value in token_counts.items():
        if key in all_doc_tokens:
            vec[key] = value / len(lexicon)
    
    doc_vectors.append(vec)
    
    
vec = copy.copy(zero_vector)
token_counts = Counter(tokenized_query)

for key, value in token_counts.items():
    if key in all_doc_tokens:
        vec[key] = value / len(lexicon)
        
query_vector = vec

    
from operator import itemgetter

results = []
for i, vector in enumerate(doc_vectors):
    results.append(   [ tok_text[i] ,cosine_sim(vector, vec)  ])
    
results = sorted(results, key = itemgetter(1),reverse=True)


print("Results using cosine similarity as a score for ranking results")
print(results[0][0])
print(results[1][0])
print(results[2][0])
