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

# problems = []
# for c,i in enumerate(bib_db.entries):
#     try:
#         problems.extend(i['problem'].split(','))
#     except:
#         pass
# print(Counter(problems))
    
format_entries(bib_db)

# df = pd.DataFrame(bib_db.entries)

# labels, counts = np.unique(df['year'],return_counts = True)
# plt.bar(labels,counts,align='center',color='k')
# plt.title('Articles by year')
# plt.xlabel('Year')
# plt.ylabel('#Articles')
# plt.show()

TRADITIONAL_MODELS = """USG
MGMPFM
LRT
iGSLR
LFBCA
LORE
IRenMF
GeoMF
RankGeoFM
GeoPFM
GeoSoCa
ASMF
CoRe
FPMC-LR
LOCABAL""".split('\n')
TRADITIONAL_MODELS = set(TRADITIONAL_MODELS)

problems = []
new_models = []
for c,i in enumerate(bib_db.entries):
    try:
        problems.extend(i['problem'])
        if i.get('model_name',None):
            new_models.extend(i['model_name'].split(','))
    except:
        continue
new_models = set(new_models)
# print(new_models)
problems = set(problems)
print(problems)

# for c,i in enumerate(bib_db.entries):
#     # if 'social' in i['information']:
#     print(f'---{c+1}---')
#     print(i['ID'])
#     print(i['problem'])
#     print(i['methodology'])
#     print(i['information'])
#     print(i.get('dataset','No dataset'))
#     print(i.get('metrics','No metrics'))
#     print(i.get('model_name','No model name'))
#     print(i.get('annotation','No annotation'))
    # baselines = i.get('baselines')
    # bl_new_models = set(baselines) & new_models
    # bl_trad_models = set(baselines) & TRADITIONAL_MODELS
    # print(baselines,bl_new_models,bl_trad_models,sep='\n')
    # i['score'] = len(baselines) + len(bl_new_models) + len(bl_trad_models)
    
# bib_db.entries = reversed(sorted(bib_db.entries, key=lambda k: k['score']) )


# print('Score','Title','Citations','Year')
# for c,i in enumerate(bib_db.entries):
#     if 'social' in i['information']:
#         print(i['score'],i['title'],i['num_citations'],i['year'])


