import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import matplotlib.collections
import bibtexparser
from collections import defaultdict

with open('../doc.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

fields = ['problem',
          'methodology',
          'information']

PRETTY_PROBLEM = {
    'poi_rec': 'Poi rec.',
    'time_aware': 'Time-aware',
    'next_poi': 'Next Poi',
    'in_out_town': 'In-/Out-of-town',
    'others': 'Others',
}
PROBLEM_IDX = {j: i for i,j in enumerate(PRETTY_PROBLEM.keys())}

PRETTY_METHODOLOGY = {
    'link_based': 'Link-based',
    'cf': 'CF',
    'factorization': 'Factorization',
    'probabilistic': 'Probabilistic',
    'hybrid': 'Hybrid',
    'others': 'Others'
}

METHODOLOGY_IDX = {j: i for i,j in enumerate(PRETTY_METHODOLOGY.keys())}

PRETTY_INFORMATION = {
    'user_pref': 'User Pref.',
    'geographical': 'Geographical',
    'social': 'Social',
    'textual': 'Textual',
    'categorical': 'Categorical',
    'sequential': 'Sequential',
    'temporal': 'Temporal',
}
INFORMATION_IDX = {j: i for i,j in enumerate(PRETTY_INFORMATION.keys())}

methodologies = []
informations = []
problems = []

count_methodologies = defaultdict(int)
count_informations = defaultdict(int)
count_problems = defaultdict(int)
num_articles = 0
for i,entry in enumerate(bib_database.entries):
    if entry.get('problem',None):
        methodologies.append(entry['methodology'].split(','))
        informations.append(entry['information'].split(','))
        problems.append(entry['problem'].split(','))
        num_articles += 1

for i,methodology in enumerate(methodologies.copy()):
    methodologies[i] = [m for m in methodology if m in PRETTY_METHODOLOGY]
    if not methodologies[i]:
        methodologies[i] = ['others']
    for j in methodologies[i]:
        count_methodologies[j] += 1

for i,information in enumerate(informations.copy()):
    informations[i] = [inf for inf in information if inf in PRETTY_INFORMATION.keys()]
    # if not informations[i]:
    #     informations[i] = ['others']
    for j in informations[i]:
        count_informations[j] += 1


for i,problem in enumerate(problems.copy()):
    problems[i] = [p for p in problem if p in PRETTY_PROBLEM.keys()]
    if not problems[i]:
        problems[i] = ['others']

    for j in problems[i]:
        count_problems[j] += 1


count_matrix_im = np.zeros((len(PRETTY_INFORMATION),len(PRETTY_METHODOLOGY)))
for l1, l2 in zip(informations,methodologies):
    for i in l1:
        for j in l2:
            count_matrix_im[INFORMATION_IDX[i], METHODOLOGY_IDX[j]] += 1

count_matrix_ip = np.zeros((len(PRETTY_INFORMATION),len(PRETTY_PROBLEM)))
for l1, l2 in zip(informations,problems):
    for i in l1:
        for j in l2:
            count_matrix_ip[INFORMATION_IDX[i], PROBLEM_IDX[j]] += 1

fig = plt.figure(figsize=[13.9, 8.8])

style = {'edgecolor':'k','facecolor':'white'}

RATIO_SIZE_CIRCLE = 120
ax = fig.add_subplot(111)
indices = np.where(count_matrix_im > 0)
index_row, index_col = indices
index_row = index_row + 1
index_col = index_col + 1
values = count_matrix_im[indices]
norms = np.sum(count_matrix_im).repeat(np.count_nonzero(count_matrix_im>0))

indices = np.where(count_matrix_ip > 0)
index_row, index_col = np.append(index_row,indices[0]+1), np.append(index_col,-indices[1]-1)
values = np.append(values, count_matrix_ip[indices])


norms = np.append(norms,np.sum(count_matrix_ip).repeat(np.count_nonzero(count_matrix_ip>0)))


for xi, yi, value in zip(index_col,index_row,values):
    ax.annotate(int(value),(xi,yi),ha='center',va='center')

    
# ax.scatter(index_col, index_row, values*RATIO_SIZE_CIRCLE, **style)
values_areas = 2.5*(values/np.max(values))
values_radii = np.sqrt(values_areas)/np.pi

circles = [plt.Circle((xi,yi), radius=v, **style) for xi,yi, v in zip(index_col,index_row,values_radii)]
for circle in circles:
    ax.add_artist(circle)
degree = 315
unit_vector = np.array([np.cos(np.pi*degree/180),np.sin(np.pi*degree/180)])

for r, c, v,norm, value_radius in zip(index_row, index_col, values,norms, values_radii):
    ax.annotate(f'{100*v/norm:.2f}%',
                np.array([c,r])+
                +(value_radius+0.25)*unit_vector,
                ha='center',va='center')
    

# [[for j in range]]
ax.spines['left'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
xticks = np.append(np.arange(len(PRETTY_METHODOLOGY))+1,-1*np.arange(len(PRETTY_PROBLEM))-1)
# _xticklabels = list(PRETTY_METHODOLOGY.keys())+list(PRETTY_PROBLEM.keys())

xticklabels = [f'{PRETTY_METHODOLOGY[label]}\n{count_methodologies[label]} ({100*count_methodologies[label]/num_articles:.0f}%)' for label in PRETTY_METHODOLOGY.keys()] + [f'{PRETTY_PROBLEM[label]}\n{count_problems[label]} ({100*count_problems[label]/num_articles:.0f}%)' for label in PRETTY_PROBLEM.keys()]
# xticklabels = list(PRETTY_METHODOLOGY.values())+list(PRETTY_PROBLEM.values())
yticks = np.arange(len(PRETTY_INFORMATION))+1

yticklabels = [f'{PRETTY_INFORMATION[label]}\n{count_informations[label]} ({100*count_informations[label]/num_articles:.0f}%)' for label in PRETTY_INFORMATION.keys()]

ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)
ax.set_yticks(yticks)
# ax.set_yticklabels(yticklabels)
ax.get_yaxis().set_visible(False)

for tick,label in zip(yticks,yticklabels):
    ax.annotate(label,(0,tick),ha='center')
ax.yaxis.tick_left()

ax.set_ylim(0,len(PRETTY_INFORMATION)+0.5)
ax.set_xlim(np.min(xticks)-0.5,np.max(xticks)+0.5)
for tick in xticks:
    ax.vlines(tick,*ax.get_ylim(),linestyles='dashed',linewidth=1,zorder=0)

for tick in yticks:
    ax.hlines(tick,*ax.get_xlim(),linestyles='dashed',linewidth=1,zorder=0)
# ax.set_xlabel('Problem-Methodology')

ax.annotate('Label\n#Articles (Percentage of #articles)',(0,0.3),weight='bold',ha='center',va='center')
# plt.show()
fig.savefig('teste.png', bbox_inches='tight')
