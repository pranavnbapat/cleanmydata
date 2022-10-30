import spacy

# Contextual spell correction using BERT (bidirectional representations)
import contextualSpellCheck
# https://spacy.io/universe/project/contextualSpellCheck

nlp = spacy.load('en_core_web_sm')
contextualSpellCheck.add_to_pipe(nlp)
doc = nlp('Income was $9.4 milion compared to the prior year of $2.7 milion.')

# print(doc._.performed_spellCheck) #Should be True
# print(doc._.outcome_spellCheck) #Income was $9.4 million compared to the prior year of $2.7 million.
#

print(doc)
