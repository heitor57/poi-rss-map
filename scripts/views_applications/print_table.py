import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import bibtexparser
import argparse
from utility_library.constants import *
from utility_library.util import *

argparse = argparse.ArgumentParser()
argparse.add_argument('-c', action='store_false',default=True)
args = argparse.parse_args()

with open('../../map.bib') as bibtex_file:
    bib_db = bibtexparser.load(bibtex_file)

TRADITIONAL_MODELS = """USG
MGMPFM
LRT
iGSLR
LFBCA
LORE
IRenMF
GeoMF
Rank-GeoFM
GeoPFM
GeoSoCa
ASMF
CoRe
FPMC-LR
LOCABAL""".split('\n')

TRADITIONAL_MODELS = set(TRADITIONAL_MODELS)

new_models = []
for c, i in enumerate(bib_db.entries):
    try:
        problems.extend(i['problem'])
        if i.get('model_name', None):
            new_models.extend(i['model_name'].split(','))
    except:
        continue
new_models = set(new_models)

bib_db.entries = format_entries(bib_db)

for c, i in enumerate(bib_db.entries):
    baselines = i.get('baselines')
    bl_new_models = set(baselines) & new_models
    bl_trad_models = set(baselines) & TRADITIONAL_MODELS
    i['score'] = len(baselines) + len(bl_new_models) + len(bl_trad_models)

bib_db.entries = reversed(sorted(bib_db.entries, key=lambda k: k['score']))

table_string = ''

latex_header = r'''
\documentclass{article}
\usepackage{longtable}
\usepackage{rotating}
\usepackage{amssymb}
\usepackage{array,multirow,graphicx}
\usepackage{textcomp}
\usepackage[numbers]{natbib}
\usepackage[a4paper, margin=0.5cm]{geometry}

\begin{document}
{\tiny
'''

latex_foot = r'''
}
\bibliographystyle{plainnat}
\bibliography{../map.bib}
\end{document}'''

table_string += r'\begin{tabular}{%s}' % (
    '|l|l|l|' + 'l|' *
    (len(PRETTY_PROBLEM) + len(PRETTY_METHODOLOGY) + len(PRETTY_INFORMATION))
) + '\n'


table_string += r'\hline \multicolumn{3}{|c|}{Related work} & \multicolumn{%d}{c|}{Problem}' % (len(PRETTY_PROBLEM)) +\
    r'& \multicolumn{%d}{c|}{Methodology}' % (len(PRETTY_METHODOLOGY)) +\
    r'& \multicolumn{%d}{c|}{Information-used}' % (len(PRETTY_INFORMATION)) +\
    r'\\' + '\n'

table_string += r'\hline Reference & \rotatebox[origin=c]{90}{\#Citations} & \rotatebox[origin=c]{90}{Score(r)} &' +\
    '&'.join(map(lambda x: r'\rotatebox[origin=c]{90}{%s}' % (x),
                 tuple(PRETTY_PROBLEM.values())+tuple(PRETTY_METHODOLOGY.values())+tuple(PRETTY_INFORMATION.values()))) + r'\\\hline' + '\n'

for i, entry in enumerate(bib_db.entries):
    if entry.get('problem', None):
        table_string += r'\citeauthor{%s} \cite{%s} & %d & %d' % (
            entry['ID'], entry['ID'], int(
                entry['num_citations']), entry['score'])
        table_string += ' & ' + ' & '.join([
            r'\(\checkmark\)' if j in entry['problem'] else ''
            for j in PRETTY_PROBLEM.keys()
        ])
        table_string += ' & ' + ' & '.join([
            r'\(\checkmark\)' if j in entry['methodology'] else ''
            for j in PRETTY_METHODOLOGY.keys()
        ])
        table_string += ' & ' + ' & '.join([
            r'\(\checkmark\)' if j in entry['information'] else ''
            for j in PRETTY_INFORMATION.keys()
        ])
        table_string += r'\\\hline' + '\n'

table_string += r'\end{tabular}' + '\n'

open('../../results/map_table.tex', 'w').write(table_string)

fname_full_table = '../../results/map_table_full.tex'
open(fname_full_table, 'w').write(latex_header + table_string + latex_foot)
if args.c:
    import os
    os.system(
        f"cd ../../results && latexmk -pdflatex=xelatex -pdf -interaction=nonstopmode map_table_full.tex"
    )
