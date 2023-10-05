
# Assignment no:-02
# Name:-Namrata Bhosale
# Subject:-NLP
# Roll no:-08 , Batch:-B1
# Title:- TFIDF
import gensim
import pprint
from gensim import corpora
from gensim.utils import simple_preprocess
doc_list = [
   "Hello, how are you?", "How do you do?", 
   "Hey what are you doing? yes you What are you doing?"
]
doc_tokenized = [simple_preprocess(doc) for doc in doc_list]
dictionary = corpora.Dictionary()
BoW_corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in doc_tokenized]
for doc in BoW_corpus:
   print([[dictionary[id], freq] for id, freq in doc])
import numpy as np
tfidf = models.TfidfModel(BoW_corpus, smartirs='ntc')
for doc in tfidf[BoW_corpus]:
   print([[dictionary[id], np.around(freq,decomal=2)] for id, freq in doc])
   #OUTPUT
#    [['are', 1], ['hello', 1], ['how', 1], ['you', 1]]
# [['how', 1], ['you', 1], ['do', 2]]
# [['are', 2], ['you', 3], ['doing', 2], ['hey', 1], ['what', 2], ['yes', 1]]
# [['are', 0.33], ['hello', 0.89], ['how', 0.33]]
# [['how', 0.18], ['do', 0.98]]
# [['are', 0.23], ['doing', 0.62], ['hey', 0.31], ['what', 0.62], ['yes', 0.31]]

# [['are', 1], ['hello', 1], ['how', 1], ['you', 1]]
# [['how', 1], ['you', 1], ['do', 2]]
# [['are', 2], ['you', 3], ['doing', 2], ['hey', 1], ['what', 2], ['yes', 1]]

# [['are', 0.33], ['hello', 0.89], ['how', 0.33]]
# [['how', 0.18], ['do', 0.98]]
# [['are', 0.23], ['doing', 0.62], ['hey', 0.31], ['what', 0.62], ['yes', 0.31]]