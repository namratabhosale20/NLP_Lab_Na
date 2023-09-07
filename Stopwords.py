#Assignment No-01
#Name:-Namrata Bhosale
#Roll no:-08, Batch:-B1
#Title:-StopWords

#Import Library
import spacy
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)
336
for stop_word in list(spacy_stopwords)[:10]:
   print(stop_word)

#output
# using
# becomes
# had
# itself
# once
# often
# is
# herein
# who
# too
