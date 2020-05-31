import pandas as pd 
pd.options.mode.chained_assignment = None
import numpy as np 
from copy import deepcopy
from string import punctuation
from random import shuffle

import gensim
from gensim.models.word2vec import Word2Vec
from gensim.models import doc2vec
from gensim.models.deprecated.doc2vec import LabeledSentence
LabeledSentence = gensim.models.deprecated.doc2vec.LabeledSentence 

from nltk.tokenize import TweetTokenizer 
tokenizer = TweetTokenizer()

from tqdm import tqdm
tqdm.pandas(desc="progress-bar")

from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def ingest():
    data = pd.read_csv('data.csv')
    data = data[data.Sentiment.isnull() == False]
    data['Sentiment'] = data['Sentiment'].map(int)
    data = data[data['SentimentText'].isnull() == False]
    data.reset_index(inplace=True)
    data.drop('index',axis=1,inplace=True)
    print ('dataset loaded with shape', data.shape)    
    return data

data = ingest()
# print(data.head(5))

def tokenize(tweet):
    try:
        # tweet = unicode(tweet.decode('utf-8').lower())
        tokens = tokenizer.tokenize(tweet)
        # tokens = filter(lambda t: not t.startswith('@'), tokens)
        # tokens = filter(lambda t: not t.startswith('#'), tokens)
        # tokens = filter(lambda t: not t.startswith('http'), tokens)
        return tokens
    except:
        return 'NC'

def postprocess(data, n=9294): # Need to change 9294 to original number of tweets
    data = data.head(n)
    data['tokens'] = data['SentimentText'].progress_map(tokenize)
    data = data[data.tokens != 'NC']
    data.reset_index(inplace=True)
    data.drop('index', inplace=True, axis=1)
    return data

data = postprocess(data)
# print(data.head(5))

x_train, x_test, y_train, y_test = train_test_split(np.array(data.head(9294).tokens),np.array(data.head(9294).Sentiment), test_size=0.2)  # Need to change 9294 to original number of tweets


def labelizeTweets(tweets, label_type):
    labelized = []
    for i,v in tqdm(enumerate(tweets)):
        label = '%s_%s'%(label_type,i)
        labelized.append(LabeledSentence(v, [label]))
    return labelized

x_train = labelizeTweets(x_train, 'TRAIN')
x_test = labelizeTweets(x_test, 'TEST')

# print(x_train[0])

tweet_w2v = Word2Vec(size=200, min_count=10)   # can change size
tweet_w2v.build_vocab([x.words for x in tqdm(x_train)])
tweet_w2v.train([x.words for x in tqdm(x_train)],total_examples=tweet_w2v.corpus_count,epochs=tweet_w2v.iter)

vectorizer = TfidfVectorizer(analyzer=lambda x: x, min_df=10)
matrix = vectorizer.fit_transform([x.words for x in x_train])
tfidf = dict(zip(vectorizer.get_feature_names(), vectorizer.idf_))
print ('vocab size :', len(tfidf))

def buildWordVector(tokens, size):
    vec = np.zeros(size).reshape((1, size))
    count = 0.
    for word in tokens:
        try:
            vec += tweet_w2v[word].reshape((1, size)) * tfidf[word]
            count += 1.
        except KeyError: # handling the case where the token is not
                         # in the corpus. useful for testing.
            continue
    if count != 0:
        vec /= count
    return vec

from sklearn.preprocessing import scale
train_vecs_w2v = np.concatenate([buildWordVector(z, 200) for z in tqdm(map(lambda x: x.words, x_train))]) 
train_vecs_w2v = scale(train_vecs_w2v)

test_vecs_w2v = np.concatenate([buildWordVector(z, 200) for z in tqdm(map(lambda x: x.words, x_test))]) 
test_vecs_w2v = scale(test_vecs_w2v)

# LSTM Model

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Conv1D

data_dim = 200
timesteps = 8
batch_size = 1

model = Sequential()
model.add(Dense(1, activation='sigmoid', input_dim=200))
model.add(Dense(1, activation='sigmoid', input_dim=200))
model.add(Dense(1, activation='sigmoid', input_dim=200))
model.add(Dense(1, activation='sigmoid', input_dim=200))
model.add(Dense(1, activation='sigmoid', input_dim=200))
model.add(Dense(1, activation='sigmoid', input_dim=200))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])
model.fit(train_vecs_w2v, y_train, epochs=2000, batch_size=1, verbose=2)
model.add(LSTM(128,batch_input_shape=(batch_size,timesteps,data_dim)))
model.add(Dropout(0.5))
#model.add(Dropout(0.5))
model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])
#model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])

#model.fit(train_vecs_w2v, y_train, epochs=9, batch_size=32, verbose=2)


score = model.evaluate(test_vecs_w2v, y_test, batch_size=1, verbose=2)
print (score[1])
