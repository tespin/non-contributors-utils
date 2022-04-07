import spacy
import random
from collections import Counter
from textwrap import fill

nlp = spacy.load('en_core_web_md')
text = open('txt/miracle-mile.txt', encoding='utf-8').read()
doc = nlp(text)

no_nouns = " ".join([word.text for word in doc if word.tag_ not in ('NN', 'NNP', 'NNS')])
print(no_nouns[500:1000])

with open("words.txt", "w", encoding='utf-8') as fh:
    for line in no_nouns:
        fh.write(' '.join([line]))
        