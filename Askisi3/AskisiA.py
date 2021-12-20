Words = ["Round","Robin","world","wide","pandemic","recursive","worlds"]
Words1 = ["Ruond","Rabin","wall","widen","pndemic","terrible","awesome"]
GrWords = ["Κότα", "Τρομερό","Κοτα","Περιορισμός","Τέλος","Φοβερό"]
GrWords1= ["Κοντά", "Τροεμρό","Κώτα","Περιωρισμοί","Τέλειος","Φοβεροί"]

memo = {}
def levenshtein(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    cost = 0 if s[-1] == t[-1] else 1
       
    i1 = (s[:-1], t)
    if not i1 in memo:
        memo[i1] = levenshtein(*i1)
    i2 = (s, t[:-1])
    if not i2 in memo:
        memo[i2] = levenshtein(*i2)
    i3 = (s[:-1], t[:-1])
    if not i3 in memo:
        memo[i3] = levenshtein(*i3)
    res = min([memo[i1]+1, memo[i2]+1, memo[i3]+cost])
    
    return res


for i in Words:
    for j in Words1:
        print("Comparing {} with {} using Levenshtein Distance:".format(i,j))
        print("Result = {}".format(levenshtein(i,j)))



for i in GrWords:
    for j in GrWords1:
        print("Comparing {} with {} using Levenshtein Distance:".format(i,j))
        print("Result = {}".format(levenshtein(i,j)))
        
    
# Προβληματα με swaping αναγραμματισμοι δλδ μεγαλο κοστος 
# Καλο μονο για να δουμε αν εχουν καμια σχεση ή οχι
