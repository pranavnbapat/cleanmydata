import spacy

# Contextual spell correction using BERT (bidirectional representations)
import contextualSpellCheck
# https://spacy.io/universe/project/contextualSpellCheck

nlp = spacy.load('en_core_web_sm')
contextualSpellCheck.add_to_pipe(nlp)
doc = nlp('Mind must be the manster of the body')

print(doc._.performed_spellCheck) #Should be True
print(doc._.outcome_spellCheck)
print(doc._.score_spellCheck)
