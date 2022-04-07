import glob
import os

files = glob.glob('annotations-test/*.txt')

def cleanup():
    for f in files:
        filename = f.split('\\')[1]
        #print(filename)

        with open(f, 'r', encoding='utf8') as fh:
            lines = [line.lower() for line in fh]

        ls = list(set(lines))

        with open(f, 'w', encoding='utf8') as out:
            #out.write('\n'.join(lines))
            out.writelines(ls)

cleanup()

