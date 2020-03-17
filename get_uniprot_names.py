from urllib import request
from tqdm import tqdm

file = open('CryoEM_GPCRGP_structures_with_CBRs.csv').readlines()
output = open('Uniprot_names.txt', 'w')

file = [i.split(',')[1] for i in file[1:]]
for i in file:
    output.write(f'{i}\n')


for i in tqdm(range(len(file)), desc='Looking for sequences families:'):
    url = 'https://www.uniprot.org/uniprot/?query='
    url += file[i]
    # if i < len(file) - 1:
    #     url += '+OR+'
    url += '&columns=id%2Centry%20name%2Cdatabase(Pfam)&format=tab&sort=score'
    try:
        site = request.urlopen(url).readlines()
        site = [i.decode('utf-8') for i in site[1:]]
        out = open(file[i], 'w')
        for i in range(len(site)):
            out.write(site[i])
        out.close()
    except:
        print(url)
        continue
    # print(site)
    # print(url)
