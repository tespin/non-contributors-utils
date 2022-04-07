import argparse
import spacy
import random

parser = argparse.ArgumentParser(description='Save lists generated with Spacy.')
parser.add_argument('-f', '--file', metavar='file', nargs='?', default='no-nouns.txt', help='filename')
parser.add_argument('-o', '--output', metavar='output', nargs='?', default='output.txt', help='name of output file')
#parser.add_argument('-l', 
parser.add_argument('-t', '--tag', metavar='pos tag', nargs='+', help='part of speech tag')
#parser.add_argument('-d', '--dep', metavar='dependency', nargs='*', default='', help='dependency relation')
parser.add_argument('-s', '--subt', metavar='subtree', nargs='?', type=bool, default=False, help='word or subtree')
parser.add_argument('-l', '--limit', metavar='limit', nargs='?', type=int, default=24, help='character limit for subtree')

args = vars(parser.parse_args())

nlp = spacy.load('en_core_web_md')
text = open(args['file'], encoding='utf-8').read()
doc = nlp(text)
words = [w for w in list(doc) if w.is_alpha]

def flatten_subtree(st):
    return ''.join([w.text_with_ws for w in list(st)]).strip()

def make_list(tags, st):
    if st == False:
        _ = [word.text for word in words if word.tag_ in tags]
    else:
        _ = [flatten_subtree(word.subtree).replace('\n', '') for word in doc if word.tag_ in tags and len(flatten_subtree(word.subtree)) < args['limit']]

    # we create a new list where extra whitespace is stripped
    ls = []
    for line in _:
        ls.append(' '.join(line.split()))

    # turn the list into a set then back again to remove repeats
    s = list(set(ls))

    return s

def save(filename, ls):
    with open(filename, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join([item for item in ls]))
    print('Saved ' + filename)

save(args['output'], make_list(args['tag'], args['subt']))
