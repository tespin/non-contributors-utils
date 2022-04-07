import json
from simpleneighbors import SimpleNeighbors
import spacy

def vec(s):
	return nlp.vocab[s].vector

def meanv(vecs):
	total = np.sum(vecs, axis=0)
	return total / len(vecs)

def build_lookup(p):
	lu = SimpleNeighbors(300)
	for word in p.keys():
		if nlp.vocab[word].has_vector:
			lu.add_one(word, vec(word))

	lu.build()
	return lu

nlp = spacy.load('en_core_web_md')
doc = nlp(open('txt/miracle-mile.txt', encoding='utf-8').read())

prob = dict(json.load(open('wordfreq-en-25000-log.json')))
lookup = build_lookup(prob)
features = lookup.nearest(vec('roof'), n=500)
#print(len(lookup.nearest(vec('roof'), n=20)))
#print(lookup.nearest(vec('roof'), n=500))
output = []
for word in doc:
    if word.is_alpha and word.text in features:
        output.append('')
    else:
        output.append(word.text)
    output.append(word.whitespace_)
#    if word.is_alpha and word.pos_ == 'NOUN':
#        new_word = random.choice(lookup.nearest(word.vector,

with open('test_nn.txt', 'w', encoding='utf-8') as fh:
    fh.write(' '.join([w for w in output]))
