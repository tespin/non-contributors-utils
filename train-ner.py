import spacy

spacy.load('en_core_web_md')
text = open('txt/miracle-mile.txt', encoding='utf-8').read()
doc = nlp(text)rint(random.choice(art).sent)

TRAIN_DATA = [
    (
        'one-story single-family residences in the portion north', 
        {'entities': [(24, 34, 'FEAT')]},
    ),
    (
        'two-story multi-family residences in the portion south',
        {'entities': [(23, 33, 'FEAT')]},
    ),
    (
        'Most buildings in the proposed HPOZ',
        {'entities': [(5, 14, 'FEAT')]},
    ),
    (
        'spatial and landscape features such as concrete sidewalks, mature trees, relatively consistent lot sizes, uniform setbacks, and a skewed orthogonal street pattern.',
        {'entities': [(48, 57, 'FEAT'), (66, 71, 'FEAT'), (95, 98, 'FEAT'), (114, 122, 'FEAT'), (148, 154, 'FEAT')]},
    ),
    (
        '',
        {'entities': [()]},
    ),
]
