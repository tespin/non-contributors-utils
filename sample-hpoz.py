import tracery
from tracery.modifiers import base_english
import spacy
import random
from collections import Counter
from textwrap import fill

nlp = spacy.load('en_core_web_md')
text = open('txt/miracle-mile.txt', encoding='utf-8').read()
doc = nlp(text)

def flatten_subtree(st):
    return ''.join([w.text_with_ws for w in list(st)]).strip()

sentences = list(doc.sents)
words = [w for w in list(doc) if w.is_alpha]
noun_chunks = list(doc.noun_chunks)
entities = list(doc.ents)

people = [e for e in entities if e.label_ == 'PERSON']
art = [e for e in entities if e.label_ == 'WORK_OF_ART']
facilities = [e for e in entities if e.label_ == 'FAC']

#print(" ".join([word.text for word in doc if word.pos_ != 'NOUN']))
objects = [flatten_subtree(word.subtree).replace('\n', ' ') for word in doc if word.dep_ in ('dobj', 'iobj', 'obj', 'pobj')]
modifiers = [flatten_subtree(word.subtree).replace('\n', ' ') for word in doc if word.dep_ in ('amod', 'nmod')]
#print(random.sample(objects, 100))
#print(random.sample(modifiers, 100))
#no_objects = [flatten_subtree(word.subtree).replace('\n', '').replace(word.text, '') for word in doc if word.dep_ in ('dobj', 'iobj', 'obj', 'pobj')]
no_nouns = [flatten_subtree(word.subtree).replace('\n', '').replace(word.text, '') for word in doc if word.tag_ in ('NN', 'NNP', 'NNS', 'NNPS')]
#no_nouns = [flatten_subtree(word.subtree).replace('\n', '').replace(word.text, '') for word in doc if word.pos_ == 'NOUN']
subjects = [flatten_subtree(word.subtree).replace('\n', ' ') for word in doc if word.dep_ in ('nsubj', 'nsubjpass')]
#print(random.sample(subjects_nn, 10))
past_tense_verbs = [word.text for word in words if word.tag_ == 'VBD' and word.lemma_ != 'be']
adjectives = [word.text for word in words if word.tag_.startswith('JJ')]
nouns = [word.text for word in words if word.tag_.startswith('NN')]
prep_phrases = [flatten_subtree(word.subtree).replace('\n', ' ') for word in doc if word.dep_ == 'prep']
#print(random.sample, prep_phrases, 100)

rules = {
    'origin': [
        '#object# #prepphrase#.'
 #       '#subject.capitalize# #predicate#.',
 #       '#subject.capitalize# #predicate#.',
 #       '#prepphrase.capitalize#, #subject# #predicate#.'
    ],
    'predicate': [
        '#verb#',
        '#verb# #nounphrase#',
        '#verb# #prepphrase#'
    ],
    'nounphrase': [
        'the #noun#',
        'the #adj# #noun#',
        'the #noun# #prepphrase#',
        'the #noun# and the #noun#',
        '#noun.a#',
        '#adj.a# #noun#',
        'the #noun# that #predicate#'
    ],
    'subject': subjects,
    'verb': past_tense_verbs,
    'noun': no_nouns,
    'adj': adjectives,
    'object': objects,
    'prepphrase': prep_phrases

}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
#output = " ".join([grammar.flatten('#origin#') for i in range(12)])
#print(fill(output, 25))
print(grammar.flatten('#origin#'))

#sents = random.sample(sentences, 10)
#for sent in random.sample(sentences, 10):
#    print('Original sentence:', sent.text.replace('\n', ' '))
#    for word in sent:
#        print()
#        print('Word:', word.text.replace('\n', ' '))
#        print('Tag:', word.tag_)
#        print('Dependency relation:', word.dep_)
#        print('Recognized entity:', word.ent_type_)
#        print('Flattened subtree: ', flatten_subtree(word.subtree).replace('\n', ' '))


#
#sent = random.choice(facilities).sent
#sent = random.choice(sentences)
#print('original sentence:', sent.text.replace('\n', ' '))
#for word in sent:
#    print()
#    print('Word:', word.text.replace('\n', ' '))
#    print('Flattened subtree: ', flatten_subtree(word.subtree).replace('\n', ' '))
#    print('Tag:', word.tag_)
#    print('Head:', word.head.text)
#    print('Dependency relation:', word.dep_)
#    print('Recognized entity: ', word.ent_type_)
#    print('Children:', list(word.children))



#word_count = Counter([w.text for w in words])
#for word, count in word_count.most_common(100):
#    print(word, count)

#works = [flatten_subtree(word.subtree).replace('\n', " ") for word in art.text if 

# prints sentence where art entity is removed
#for item in random.sample(art, 5):
#    print('[' + item.text.strip() + ']:' + item.sent.text.replace(item.text, ''))


#def flatten_subtree(st):
#    return ''.join([w.text_with_ws for w in list(st)]).strip()

#for ent in random.sample(entities, 10):
#    print(ent.text, ent.label_)

#for item in random.sample(people, len(people)):
#    print(item.text.strip())

#for item in random.sample(sentences, 5):
#    print(">", item.text.strip().replace("\n", " "))

#for item in random.sample(noun_chunks, 10):
#    print(item.text)

#sentence_strs = [item.text for item in doc.sents]
#print(random.sample(sentence_strs, 10))
