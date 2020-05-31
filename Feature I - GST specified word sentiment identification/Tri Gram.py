import nltk
from collections import Counter
f = open('GSTtweets7.csv')
raw = f.read()

tokens = nltk.word_tokenize(raw)

#Create your bigrams
bgs = nltk.trigrams(tokens)

#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)
count = Counter(fdist).most_common(100)
print (count)

#for k,v in fdist.items():
    #print (k,v)
