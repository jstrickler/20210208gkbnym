#!/usr/bin/env python
from glob import glob

files = glob('../DATA/*.txt') # <1>
print(files, '\n')

no_files = glob('../DATA/*.wom')
print(no_files, '\n')

