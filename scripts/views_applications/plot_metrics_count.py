import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import bibtexparser
from utility_library.constants import *
from utility_library.util import *
import collections
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib.ticker as mtick
plt.rcParams['font.size'] = 22

with open('../../map.bib') as bibtex_file:
    bib_db = bibtexparser.load(bibtex_file)

bib_db.entries = format_entries(bib_db)

cnt_metrics = collections.Counter()
for c, i in enumerate(bib_db.entries):
    try:
        if i.get('problem', None):
            print(i['metrics'])
            for metric in i['metrics']:
                cnt_metrics[metric] += 1
    except:
        continue

print(len(cnt_metrics.keys()))
old_cnt_values = np.array(list(cnt_metrics.copy().values()))
for metric in cnt_metrics.copy().keys():
    if metric not in PRETTY_METRIC:
        print('removing', metric, 'and putting in others')
        cnt_metrics['others'] += cnt_metrics.pop(metric)

cnt_metrics = {
    k: v
    for k, v in reversed(sorted(cnt_metrics.items(), key=lambda item: item[1]))
}
print("Number of articles", len(bib_db.entries))
cnt_metrics['others'] = cnt_metrics.pop('others')
fig, ax = plt.subplots(figsize=(8.4, 4.8))
xs = list(map(PRETTY_METRIC.get, cnt_metrics.keys()))
ys = np.array(list(cnt_metrics.values()))
ys = 100 * ys / len(bib_db.entries)

bars = ax.bar(xs, ys, color='k')
for x, bar in zip(xs, bars):
    if x in 'Coverage,ILD,EPC,PRg,Others,Outros':
        bar.set_color('grey')
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
    tick.set_horizontalalignment('right')
for x, y in zip(xs, ys):
    ax.annotate("%d" % (y), xy=(x, y), ha='center', va='bottom')

if LANG == 'en':
    ax.set_ylabel('Percentage of Studies')
elif LANG == 'br':
    ax.set_ylabel('Porcentagem de Estudos')
ax.set_ylim(top=max(ys) + 5)
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.savefig('../../results/metrics_count.png', bbox_inches='tight')
fig.savefig('../../results/metrics_count.eps', bbox_inches='tight')
