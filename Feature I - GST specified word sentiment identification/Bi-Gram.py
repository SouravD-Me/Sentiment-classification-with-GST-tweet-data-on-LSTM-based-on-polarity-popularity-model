import nltk
from nltk.collocations import *
line = ""
open_file = open('GSTtweets.csv','r')
for val in open_file:
    line += val
tokens = line.split()

bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(tokens)
finder.apply_freq_filter(3)
print (finder.nbest(bigram_measures.pmi, 100))
