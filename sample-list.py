import argparse
import random
import os

parser = argparse.ArgumentParser(description='Sample lists generated with spacy.')
parser.add_argument('-f', '--files', metavar='files', nargs='+', help='path to files')
parser.add_argument('-n', '--num', metavar='number', nargs='?', default=5, type=int, help='number of samples')

args = vars(parser.parse_args())

def sample(files, num):
    for filename in files:
        # we open a file and read it into 'file'
        file = open(filename, 'r', encoding='utf-8')

        # create a list of all the lines and remove whitespace
        ls = file.readlines()
        ls = [line.replace('\n', '') for line in ls]

        # print the sample in a clean and formatted way
        print()
        print('Random {}'.format(os.path.splitext(filename)[0]))
        print(random.sample(ls, num))

sample(args['files'], args['num'])
