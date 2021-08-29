import bibtexparser
from collections import defaultdict
from lib.constants import *
from lib.util import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter
import collections
with open('../map.bib') as bibtex_file:
    bib_db = bibtexparser.load(bibtex_file)

format_entries(bib_db)
# problems = []
# for c,i in enumerate(bib_db.entries):
#     try:
#         problems.extend(i['problem'].split(','))
#     except:
#         pass
# print(Counter(problems))
    
# format_entries(bib_db)

# df = pd.DataFrame(bib_db.entries)

# labels, counts = np.unique(df['year'],return_counts = True)
# plt.bar(labels,counts,align='center',color='k')
# plt.title('Articles by year')
# plt.xlabel('Year')
# plt.ylabel('#Articles')
# plt.show()

# TRADITIONAL_MODELS = """USG
# MGMPFM
# LRT
# iGSLR
# LFBCA
# LORE
# IRenMF
# GeoMF
# RankGeoFM
# GeoPFM
# GeoSoCa
# ASMF
# CoRe
# FPMC-LR
# LOCABAL""".split('\n')
# TRADITIONAL_MODELS = set(TRADITIONAL_MODELS)
# years_count = Counter()
# dsc = Counter()
# for c,i in enumerate(bib_db.entries):
#     try:
#         print(i['num_citations'])
#         # print(i.get('problem',None))

#             # for dataset in i['dataset'].split(','):
#             #     dsc[dataset] += 1
#     except:
#         continue
# print(new_models)
# print(years_count)
# print(dsc)

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

cnt_datasets = collections.Counter()
for c,i in enumerate(bib_db.entries):
    try:
        if i.get('problem',None):
            for dataset in i['metrics']:
                if dataset == '':
                    print(i['ID'])
                cnt_datasets[dataset] += 1
    except:
        continue


# print(cnt_datasets.keys())
# unique, count = np.unique(list(cnt_datasets.values()),return_counts=True)
# print(len(cnt_datasets.keys()))

# print(unique,count)
# print(count[0]/np.sum(count))
# print(1-count[0]/np.sum(count))
