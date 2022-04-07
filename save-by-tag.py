import argparse
import spacy
import random

parser = argparse.ArgumentParser(description='Save lists generated with Spacy.')
parser.add_argument('-f', '--file', metavar='file', nargs='?', default='no-nouns.txt', help='filename')
parser.add_argument('-o', '--output', metavar='output', nargs='?', default='output.txt', help='name of output file')
parser.add_argument('-a', '--annotation', metavar='annotation', nargs='?', default='annotation', help='type of annotation')
parser.add_argument('-l', '--labels', metavar='labels', nargs='+', help='pos, tag, or dependency labels')
parser.add_argument('-s', '--subt', metavar='subtree', nargs='?', type=bool, default=False, help='word or subtree')
parser.add_argument('-n', '--num', metavar='num', nargs='?', type=int, default=24, help='character limit')

args = vars(parser.parse_args())

nlp = spacy.load('en_core_web_md')
text = open(args['file'], encoding='utf-8').read()
doc = nlp(text)
words = [w for w in list(doc) if w.is_alpha]

def flatten_subtree(st):
    return ''.join([w.text_with_ws for w in list(st)]).strip()

def make_list(annotation, labels, st, num):
    if annotation == 'pos':
        if st == False:
            _ = [word.text for word in words if word.pos_ in labels]
        else:
            _ = [flatten_subtree(word.subtree).replace('\n', '') for word in doc if word.pos_ in labels and len(flatten_subtree(word.subtree)) < num]
    elif annotation == 'tag':
        if st == False:
            _ = [word.text for word in words if word.tag_ in labels]
        else:
            _ = [flatten_subtree(word.subtree).replace('\n', '') for word in doc if word.tag_ in labels and len(flatten_subtree(word.subtree)) < num]
    elif annotation == 'dep':
        if st == False:
            _ = [word.text for word in words if word.dep_ in labels]
        else:
            _ = [flatten_subtree(word.subtree).replace('\n', '') for word in doc if word.dep_ in labels and len(flatten_subtree(word.subtree)) < num]
    else:
        print('Invalid annotation specified.')
        exit()

    # create a new list with stripped whitespace
    ls = []
    for line in _:
        ls.append(' '.join(line.split()))

    # turn the list into a set then back to remove repeated elements
    s = list(set(ls))

    return s

def save(filename, ls):
    with open(filename, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join([item for item in ls]))
    print('Saved ' + filename)

save(args['output'], make_list(args['annotation'], args['labels'], args['subt'], args['num']))
print(args)
