import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
set(stopwords.words('english'))
words = re.findall(r'\w+',open('GST  Tokens Final.txt').read().lower())
count = Counter(words).most_common(1000)
print(count)
