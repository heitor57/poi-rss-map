import bibtexparser
from collections import defaultdict
from lib.constants import *
from lib.util import *

with open('../doc.bib') as bibtex_file:
    bib_db = bibtexparser.load(bibtex_file)


format_entries(bib_db)

table_string = ''

latex_header = r'\documentclass{article}

\usepackage{longtable}
\usepackage{rotating}
\usepackage{array,multirow,graphicx}
\begin{document}

\section{Introduction}
'

latex_foot = r'\end{document}'



for i, entry in enumerate(bib_db.entries):

    if entry.get('problem',None):
        print(entry['methodology'])
        print(entry['information'])
        print(entry['problem'])
        

