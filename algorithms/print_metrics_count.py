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

for c,i in enumerate(bib_db.entries):
    try:
        if i.get('model_name',None):
            print(i['title'])
            print(i['metrics'])
    except:
        continue
