import bibtexparser
from collections import defaultdict
from lib.constants import *
from lib.util import *
import collections
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 20

with open('../doc.bib') as bibtex_file:
    bib_db = bibtexparser.load(bibtex_file)

format_entries(bib_db)

cnt_metrics = collections.Counter()
for c,i in enumerate(bib_db.entries):
    try:
        if i.get('problem',None):
            # if not(len({'precision','recall','accuracy'} & set(i['metrics'])) > 0):
            print(i['metrics'])
            for metric in i['metrics']:
                # if 'precision' in metric:
                #     cnt_metrics['precision']
                # if 'recall' in metric:
                #     cnt_metrics['recall']
                cnt_metrics[metric] += 1
    except:
        continue
for metric in cnt_metrics.copy().keys():
    if metric not in PRETTY_METRIC:
        print('removing',metric,'and putting in others')
        cnt_metrics['others'] += cnt_metrics.pop(metric)

cnt_metrics = {k: v for k, v in
                reversed(sorted(cnt_metrics.items(), key=lambda item: item[1]))}

cnt_metrics['others'] = cnt_metrics.pop('others')
fig, ax = plt.subplots()
xs = list(map(PRETTY_METRIC.get,cnt_metrics.keys()))
ys = cnt_metrics.values()
bars = ax.bar(xs,ys,color='k')
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
    tick.set_horizontalalignment('right')
for x, y in zip(xs, ys):
    ax.annotate(str(y),xy=(x,y),ha='center',va='bottom')
ax.set_ylabel('#Articles')
# ax.set_ylim(min(ys),max(ys))
ax.set_ylim(top=max(ys)+5)
fig.savefig('metrics_count.png',bbox_inches='tight')
fig.savefig('metrics_count.eps',bbox_inches='tight')

# print(cnt_metrics.most_common(13))
