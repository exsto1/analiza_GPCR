import os
path = 'uniprot_results'

files = os.listdir(path)

for i in files:
    temp = open('/'.join([path, i])).readlines()
    temp = [i.rstrip().split('\t') for i in temp if len(i.split('\t')) == 3]
    

