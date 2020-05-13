from lib.constants import *
import re
def format_entries(bib_db):

    to_maintain = []
    for i, entry in enumerate(bib_db.entries):
        if entry.get('problem',None):
            entry['methodology'] = [j for j in entry['methodology'].split(',') if j in PRETTY_METHODOLOGY]
            if not entry['methodology']:
                entry['methodology'] = ['others']

            entry['information'] = [j if j in PRETTY_INFORMATION else 'others' for j in entry['information'].split(',')]

            entry['problem'] = list(set([j if j in PRETTY_PROBLEM else 'others' for j in entry['problem'].split(',')]))

            entry['baselines'] = entry.get('baselines','').split(',')
            entry['metrics'] = entry.get('metrics','').split(',')
            entry['dataset'] = re.sub(r'\([^)]*\)','',entry.get('dataset','')).split(',')
            to_maintain.append(i)
    bib_db.entries = [bib_db.entries[i] for i in to_maintain]
        
