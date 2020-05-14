import bibtexparser
from collections import defaultdict
from lib.constants import *
from lib.util import *
import collections
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 14

with open('../doc.bib') as bibtex_file:
    bib_db = bibtexparser.load(bibtex_file)

format_entries(bib_db)

num_valid = 0
for c,i in enumerate(bib_db.entries):
    try:
        if i.get('problem',None):
            # if not(len({'precision','recall','accuracy'} & set(i['metrics'])) > 0):
            print(i['ID'],i['metrics'])
            num_valid += 1
    except:
        continue

print(num_valid)
