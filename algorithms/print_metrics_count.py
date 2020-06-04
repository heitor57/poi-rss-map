import bibtexparser
from collections import defaultdict
from lib.constants import *
from lib.util import *
import collections
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib.ticker as mtick
plt.rcParams['font.size'] = 18

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

print(len(cnt_metrics.keys()))
old_cnt_values = np.array(list(cnt_metrics.copy().values()))
for metric in cnt_metrics.copy().keys():
    if metric not in PRETTY_METRIC:
        print('removing',metric,'and putting in others')
        cnt_metrics['others'] += cnt_metrics.pop(metric)

cnt_metrics = {k: v for k, v in
                reversed(sorted(cnt_metrics.items(), key=lambda item: item[1]))}
print("Number of articles", len(bib_db.entries))
cnt_metrics['others'] = cnt_metrics.pop('others')
fig, ax = plt.subplots(figsize=(8.4,4.8))
xs = list(map(PRETTY_METRIC.get,cnt_metrics.keys()))
ys = np.array(list(cnt_metrics.values()))
ys = 100*ys / len(bib_db.entries)

bars = ax.bar(xs,ys,color='k')
for x, bar in zip(xs,bars):
    if x in 'Coverage,ILD,EPC,PRg,Others':
        bar.set_color('grey')
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
    tick.set_horizontalalignment('right')
for x, y in zip(xs, ys):
    ax.annotate("%d"%(y),xy=(x,y),ha='center',va='bottom')
ax.set_ylabel('Percentage of Studies')
# ax.set_ylim(min(ys),max(ys))
ax.set_ylim(top=max(ys)+5)
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
# ax.annotate('$\\tilde{x}$ %.2f\n$Q_3$ %.2f'%(
#     np.median(old_cnt_values),
#     np.percentile(old_cnt_values,75),
# ),
#             xy=(0.82,0.82),xycoords='axes fraction')

# sub_ax = inset_axes(ax,
#                     width="50%", # width = 30% of parent_bbox
#                     height=3., # height : 1 inch
#                     loc='upper center')
# sub_ax.pie([40,30,20],labels=['precision','diversity','novelty'])
fig.savefig('metrics_count.png',bbox_inches='tight')
fig.savefig('metrics_count.eps',bbox_inches='tight')

# print(cnt_metrics.most_common(13))
