import numpy as np

with open('Input_file.fq', 'r') as ff:
    content = ff.readlines()

key, occurrence = np.unique(content, return_counts=True)

key = key[np.argsort(occurrence)]
occurrence = occurrence[np.argsort(occurrence)]

import sys
sys.stdout = open('Output_file.txt','wt')

for k,o in zip(key, occurrence):
    print('Number of occurrences:', o, ' for key:', k)