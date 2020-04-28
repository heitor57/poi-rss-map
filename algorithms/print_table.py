import bibtexparser
from collections import defaultdict
from lib.constants import *
from lib.util import *

with open('../doc.bib') as bibtex_file:
    bib_db = bibtexparser.load(bibtex_file)


format_entries(bib_db)

table_string = ''

latex_header = r'''\documentclass{article}

\usepackage{longtable}
\usepackage{rotating}
\usepackage{amssymb}
\usepackage{array,multirow,graphicx}
\usepackage{textcomp}
\begin{document}

\section{Introduction}
'''

latex_foot = r'''\bibliographystyle{plain}
\bibliography{../../doc}
\end{document}'''

table_string += r'\begin{longtable}{%s}' % ('|'+ 'l|'*(1+len(PRETTY_PROBLEM)+len(PRETTY_METHODOLOGY)+len(PRETTY_INFORMATION))) + '\n'


table_string += r'\hline & \multicolumn{%d}{c|}{Problem}' % (len(PRETTY_PROBLEM)) +\
    r'& \multicolumn{%d}{c|}{Methodology}' % (len(PRETTY_METHODOLOGY)) +\
    r'& \multicolumn{%d}{c|}{Information-used}' % (len(PRETTY_INFORMATION)) +\
    r'\\' + '\n'

table_string += r'\hline Related work & ' +\
    '&'.join(map(lambda x: r'\rotatebox[origin=c]{90}{%s}' % (x),
                 tuple(PRETTY_PROBLEM.values())+tuple(PRETTY_METHODOLOGY.values())+tuple(PRETTY_INFORMATION.values()))) + r'\\\hline' + '\n'
    

for i, entry in enumerate(bib_db.entries):
    if entry.get('problem',None):
        table_string += r'\citeauthor{%s} \cite{%s}' % (entry['ID'],entry['ID'])
        table_string += ' & ' + ' & '.join([r'\(\checkmark\)' if j in entry['problem'] else '' for j in PRETTY_PROBLEM.keys()])
        table_string += ' & ' + ' & '.join([r'\(\checkmark\)' if j in entry['methodology'] else '' for j in PRETTY_METHODOLOGY.keys()]) 
        table_string += ' & ' + ' & '.join([r'\(\checkmark\)' if j in entry['information'] else '' for j in PRETTY_INFORMATION.keys()])
        table_string += r'\\\hline'+'\n'
        

table_string += r'\end{longtable}' + '\n'

open('map_table.tex','w').write(table_string)
