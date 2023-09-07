# Assignment No-01
# Name:-Namrata Bhosale
# Roll no:-08, Batch:-B1
# Title:-Lemmatization

# Import Library
import spacy

nlp = spacy.load("en_core_web_sm")
conference_help_text = (
    "Robert was a good king."
    " He wanted to bring peace to his kingdom."
    " There were many others who wanted to become king."
    "They started plotting against him."
)
# Lemmatization
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")
# OUTPUT:-
#  was : be
#  He : he
#  wanted : want
#   There : there
#  were : be
#  others : other
#  wanted : want
#  They : they
#  started : start
#  plotting : plot
#  him : he
