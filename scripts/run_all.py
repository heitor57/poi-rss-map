#!/usr/bin/python3
import os

fdir = "./views_applications/"
files = os.listdir(fdir)

for f in files:
    print(f'executing {fdir+f}')
    os.system(f'cd {fdir} && python3 {f}')
    print(f'{f} done')
