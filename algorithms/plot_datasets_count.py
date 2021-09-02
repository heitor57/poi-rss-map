import bibtexparser
from collections import defaultdict
from lib.constants import *
from lib.util import *
import collections
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick

plt.rcParams["font.size"] = 22

with open("../map.bib") as bibtex_file:
    bib_db = bibtexparser.load(bibtex_file)

bib_db.entries = format_entries(bib_db)
cnt_datasets = collections.defaultdict(int)
for c, i in enumerate(bib_db.entries):
    try:
        if i.get("problem", None):
            for dataset in i["dataset"]:
                cnt_datasets[dataset] += 1
    except:
        continue
print(cnt_datasets)
cnt_datasets.pop("")
print(len(cnt_datasets.keys()))
old_cnt_values = np.array(list(cnt_datasets.copy().values()))
for dataset in cnt_datasets.copy().keys():
    if dataset not in PRETTY_DATASET:
        print("removing", dataset, "and putting in others")
        cnt_datasets["others"] += cnt_datasets.pop(dataset)

cnt_datasets = {
    k: v
    for k, v in reversed(sorted(cnt_datasets.items(),
                                key=lambda item: item[1]))
}
cnt_datasets["others"] = cnt_datasets.pop("others")
fig, ax = plt.subplots(figsize=(8.4, 4.8))
xs = list(map(PRETTY_DATASET.get, cnt_datasets.keys()))
ys = np.array(list(cnt_datasets.values()))
ys = 100 * ys / len(bib_db.entries)
bars = ax.bar(xs, ys, color="k")
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
    tick.set_horizontalalignment("right")
for x, y in zip(xs, ys):
    ax.annotate("%d" % (y), xy=(x, y), ha="center", va="bottom")
if LANG == "en":
    ax.set_ylabel("Percentage of Studies")
elif LANG == "br":
    ax.set_ylabel("Porcentagem de Estudos")
# ax.set_ylim(min(ys),max(ys))
ax.set_ylim(top=max(ys) + 4)

ax.yaxis.set_major_formatter(mtick.PercentFormatter())
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.savefig("data/datasets_count.png", bbox_inches="tight")
fig.savefig("data/datasets_count.eps", bbox_inches="tight")
