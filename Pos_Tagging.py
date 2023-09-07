#Assignment No-01
#Name:-Namrata Bhosale
#Roll no:-08, Batch:-B1
#Title:-Part-of-speecg Tagging

#Import Library
import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
    "Robert was a good king."
    " He wanted to bring peace to his kingdom."
    " There were many others who wanted to become king."
    "They started plotting against him."
)
#Part-of-speech Tagging
about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )

#output

# TOKEN: Robert
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: was
# =====
# TAG: VBD        POS: AUX
# EXPLANATION: verb, past tense

# TOKEN: a
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: good
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: king
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: .
# =====
# TAG: .          POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer

# TOKEN: He
# =====
# TAG: PRP        POS: PRON
# EXPLANATION: pronoun, personal

# TOKEN: wanted
# =====
# TAG: VBD        POS: VERB
# EXPLANATION: verb, past tense

# TOKEN: to
# =====
# TAG: TO         POS: PART
# EXPLANATION: infinitival "to"

# TOKEN: bring
# =====
# TAG: VB         POS: VERB
# EXPLANATION: verb, base form

# TOKEN: peace
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: to
# =====
# TAG: IN         POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: his
# =====
# TAG: PRP$       POS: PRON
# EXPLANATION: pronoun, possessive

# TOKEN: kingdom
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: .
# =====
# TAG: .          POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer

# TOKEN: There
# =====
# TAG: EX         POS: PRON
# EXPLANATION: existential there

# TOKEN: were
# =====
# TAG: VBD        POS: VERB
# EXPLANATION: verb, past tense

# TOKEN: many
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: others
# =====
# TAG: NNS        POS: NOUN
# EXPLANATION: noun, plural

# TOKEN: who
# =====
# TAG: WP         POS: PRON
# EXPLANATION: wh-pronoun, personal

# TOKEN: wanted
# =====
# TAG: VBD        POS: VERB
# EXPLANATION: verb, past tense

# TOKEN: to
# =====
# TAG: TO         POS: PART
# EXPLANATION: infinitival "to"

# TOKEN: become
# =====
# TAG: VB         POS: VERB
# EXPLANATION: verb, base form

# TOKEN: king
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: .
# =====
# TAG: .          POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer

# TOKEN: They
# =====
# TAG: PRP        POS: PRON
# EXPLANATION: pronoun, personal

# TOKEN: started
# =====
# TAG: VBD        POS: VERB
# EXPLANATION: verb, past tense

# TOKEN: plotting
# =====
# TAG: VBG        POS: VERB
# EXPLANATION: verb, gerund or present participle

# TOKEN: against
# =====
# TAG: IN         POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: him
# =====
# TAG: PRP        POS: PRON
# EXPLANATION: pronoun, personal

# TOKEN: .
# =====
# TAG: .          POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer











