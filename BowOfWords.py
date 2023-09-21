import gensim
from gensim import corpora

text1 = ["""Gensim is a free open-source Python library for representing documents as semantic vectors,
           as efficiently and painlessly as possible. Gensim is designed 
           to process raw, unstructured digital texts using unsupervised machine learning algorithms."""]

tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)

print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)
g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)
 