import bibtexparser
from collections import defaultdict
from lib.constants import *
from lib.util import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter
with open('../doc.bib') as bibtex_file:
    bib_db = bibtexparser.load(bibtex_file)

format_entries(bib_db)


cnt = defaultdict(lambda:defaultdict(int))

for c,i in enumerate(bib_db.entries):
    try:
        if i.get('problem',None):
            for p in i['problem']:
                for m in i['methodology']:
                    cnt[p][m] += 1
    except:
        continue
for problem, methodologies in cnt.items():
    print('*',PRETTY_PROBLEM[problem])
    for methodology, qnt in methodologies.items():
        print('\t- '+PRETTY_METHODOLOGY[methodology]+':',qnt)

# for k, v in sorted(cnt.items(),key= lambda x: x[0][0]):
#     print(', '.join(k),v)
