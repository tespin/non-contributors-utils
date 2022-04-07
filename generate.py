import tracery
from tracery.modifiers import base_english
import random
from textwrap import fill

with open('objects.txt', encoding='utf-8') as f: 
    objects = [line.strip() for line in f]
    f.close()

with open('subjects.txt', encoding='utf-8') as f:
    subjects = [line.strip() for line in f]
    f.close()

with open('modifiers.txt', encoding='utf-8') as f:
    modifiers = [line.strip() for line in f]
    f.close()

with open('adjectives.txt', encoding='utf-8') as f:
    adjectives = [line.strip() for line in f]
    f.close()

with open('past_tense_verbs.txt', encoding='utf-8') as f:
    past_tense_verbs = [line.strip() for line in f]
    f.close()

with open('prep_phrases.txt', encoding='utf-8') as f:
    prep_phrases = [line.strip() for line in f]
    f.close()

with open('nouns.txt', encoding='utf-8') as f:
    nouns = [line.strip() for line in f]
    f.close()

rules = {
    'origin': [
        '#predicate#.'
    ],
    'predicate': [
        '#nounphrase# #verb#',
        '#nounphrase# #adjective# #verb# #modifier#',
        '#objphrase# #verb# #modifier#',
        '#objphrase# #adjective# #verb# #modifier#'
    ],
    'nounphrase': [
        'the #noun#',
        '#adjective.a# #noun#',
        '#noun#, #noun#, and #noun#',
        'the #noun# #prepphrase#'
    ],
    'objphrase': [
        'the #modifier# #object#',
        'the #modifier# #subject#',
        '#object# #prepphrase#',
        '#subject# #prepphrase#',
        '#object# #prepphrase# #noun#',
        '#subject# #prepphrase# #noun#'
    ],
    'object': objects,
    'subject': subjects,
    'modifier': modifiers,
    'adjective': adjectives,
    'verb': past_tense_verbs,
    'prepphrase': prep_phrases,
    'noun': nouns
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
output = " ".join([grammar.flatten('#origin#') for i in range(10)])
print(fill(output, 40))
#print(grammar.flatten('#origin#'))

#print('Random objects: ', random.sample(objects, 5))
#print('Random subjects: ', random.sample(subjects, 5))
#print('Random modifiers: ', random.sample(modifiers, 5))
#print('Random past tense verbs: ', random.sample(past_tense_verbs, 5))
#print('Random adjectives: ', random.sample(adjectives, 5))
#print('Random prep phrases: ', random.sample(prep_phrases, 5))
#print('Random nouns: ', random.sample(nouns, 5))
