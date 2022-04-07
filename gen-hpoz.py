import tracery
from tracery.modifiers import base_english
import random
from textwrap import fill
import glob
import os

files = glob.glob('annotations/*.txt')

chunks = {}

def create_dict() :
    for f in files:

        # create key by splitting file path
        path = os.path.splitext(f)[0]
        key = path.split('\\')[1]

        # create file
        file = open(f, 'r', encoding='utf8')

        # populate sentence chunks
        chunks[key] = file.readlines()
        chunks[key] = [line.replace('\n', '') for line in chunks[key]]

        # format and print results
        #print(chunks[key][100:110])
#        print(key)
#        print(random.sample(chunks[key], 5))
#        print()

def flatten_grammar() :
    rules = {
        'origin': [
            '#adv_phrase.capitalize#.',
            'The #adv_phrase#.',
            '#adv_phrase.capitalize# #conj_phrase#.',
            '#adj_phrase.capitalize#.',
            '#conj_phrase.capitalize#, #adj_phrase#.',
            '#adj_phrase.capitalize# #ger_nps#.',
            'The #past_np# #adv# #ger_nps#.',
            'The #pres_np# #ger_nps#.',
            '#noun_phrase.capitalize# #past_verb# #prep#.',
            '#pres_np.capitalize# #adj#.',
#            '#pres_np.capitalize# #mod#.',
            '#past_np.capitalize# #past_verb#.',
#            '#past_np.capitalize# #adj#.'

            #'The #singular_np# was #adv# #ger_nps#.',
           # 'The #plural_np# were #amod# #ger_nps#.'

            #'#ger_nps# #past_verb# #adj#.',
            #'#conj_phrase#, #adj_phrase#.',
            #'#conj_phrase#'
            #'#noun_phrase.capitalize# #past_verb#.',
            #'#noun_phrase.capitalize# #pastp_verb#.',
            #'#singular_np.capitalize# was #amod#.',
            #'#plural_np.capitalize# were #amod#.'
            #'#adv# #ger_nps#'
            #'#noun_phrase.capitalize#'
            #'#past_advcl_phrase# the #obj#.'
            #'#adj# #noun_phrase# #prep# #noun#'
            #'#noun_unit# #advcl_phrase# #mod_phrase#'
            #'#prep_phrase# #noun#'
            #'#predicate#',
            #'#predicate# #adv.capitalize#.'
        ],
        'noun_phrase': [
            '#singular_np#',
            '#plural_np#'
        ],
        'pres_np': [
            '#singular_np# is',
            '#plural_np# are'
        ],
        'past_np': [
            '#singular_np# was',
            '#plural_np# were'
        ],
        'singular_np': [
            '#noun#',
            '#noun# #adv#',
            '#noun# #adv_st#',
            '#amod# #noun#',
            '#adj# #noun#',
            '#adj# #noun.s#',
            '#adv#, the #noun#'
        ],
        'plural_np': [
            '#noun# and #noun#',
            '#noun# #plur_noun#',
            '#adj# #plur_noun#',
            '#prop_noun# #plur_noun#',
            '#amod# #plur_noun#',
            '#plur_noun#',
            '#adv#, the #noun# and #noun#'
        ],
        'adj_phrase': [
            '#singular_np# is #comp_adj#',
            '#singular_np# was #comp_adj#',
            '#singular_np# and #noun# were #comp_adj#',
            '#plur_noun# were #comp_adj#',
            '#plur_noun# were #sup_adj#'
        ],
        'adv_phrase': [
            '#singular_np# #adv# #past_verb#',
            '#plural_np# #adv# #pastp_verb#',
            '#adv# #past_verb#',
            '#adv# #pastp_verb#'
        ],
        'conj_phrase': [
            '#conj.capitalize# the #noun#'
        ],
        'ger_nps': [
            '#gerund# #singular_np.a#'
        ],
        'ger_npp': [
            '#gerund# #plural_np#'
        ],
        'prep_phrase': [
            '#gerund# #prep#'
        ],
        'adj': chunks['adjs'],
        'advcl': chunks['advcls'],
        'advmod_st': chunks['advmods_st'],
        'adv': chunks['advs'],
        'adv_st': chunks['advs_st'],
        'amod': chunks['amods'],
        'amod_st': chunks['amods_st'],
        'comp_adj': chunks['comp_adjs'],
        'conj': chunks['conjs'],
        'gerund_st': chunks['gerunds_st'],
        'gerund': chunks['gerunds'],
        'noun': chunks['nouns'],
        'noun_unit': chunks['noun_chunks'],
        'nsubj': chunks['nsubjs'],
        'obj': chunks['objects'],
        'past_verb': chunks['past_verbs'],
        'pastp_verb': chunks['pastp_verbs'],
        'plur_noun': chunks['plural_nouns'],
        'prep': chunks['preps'],
        'prop_noun': chunks['prop_nouns'],
        'sup_adj': chunks['sup_adjs'],
        'verb': chunks['verbs']
    }

    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)

    #return(grammar.flatten('#origin#'))
    return(' '.join([grammar.flatten('#origin#') for i in range(3)]))


create_dict()
#print(flatten_grammar())
#output = fill(flatten_grammar(), 40)
#print(type(output))
output = []
for i in range(600):
    sent = fill(flatten_grammar(), 40)
    output.append(' '.join(sent.split()))

with open('testoutput.txt', 'w', encoding='utf8') as fh:
    fh.write('\n'.join([item for item in output]))

