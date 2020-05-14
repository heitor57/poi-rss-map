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
cnt_datasets = collections.defaultdict(int)
for c,i in enumerate(bib_db.entries):
    try:
        if i.get('problem',None):
            for dataset in i['dataset']:
                cnt_datasets[dataset] += 1
    except:
        continue

for dataset in cnt_datasets.copy().keys():
    if dataset not in PRETTY_DATASET:
        del cnt_datasets[dataset]

# print
# cnt_datasets = dict(reversed(sorted(cnt_datasets,key=lambda i: print(i))))
cnt_datasets = {k: v for k, v in
                reversed(sorted(cnt_datasets.items(), key=lambda item: item[1]))}
fig, ax = plt.subplots()
xs = list(map(PRETTY_DATASET.get,cnt_datasets.keys()))
ys = cnt_datasets.values()
bars = ax.bar(xs,ys,color='k')
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
    tick.set_horizontalalignment('right')
for x, y in zip(xs, ys):
    ax.annotate(str(y),xy=(x,y),ha='center',va='bottom')
ax.set_ylabel('#Articles')
# ax.set_ylim(min(ys),max(ys))
ax.set_ylim(top=max(ys)+2)
fig.savefig('datasets_count.png',bbox_inches='tight')
# plt.show()

# table_string = ''
# table_string += r'\begin{table}{%s}' % ('l'*len(cnt_datasets)) + '\n'
# table_string += ' & '.join(xs) + r'\\\hline'+'\n'
# table_string += ' & '.join(map(str,ys)) + r'\\\hline'+'\n'
# table_string += r'\end{table}' + '\n'

# open('dataset_count_table.tex','w').write(table_string)
