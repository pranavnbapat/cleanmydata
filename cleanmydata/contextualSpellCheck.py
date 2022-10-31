import spacy

# Contextual spell correction using BERT (bidirectional representations)
import contextualSpellCheck
# https://spacy.io/universe/project/contextualSpellCheck

nlp = spacy.load('en_core_web_sm')
contextualSpellCheck.add_to_pipe(nlp)
