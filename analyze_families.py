import os
path = 'uniprot_results'

files = os.listdir(path)

results = {}

for i0 in files:
    temp = open('/'.join([path, i0])).readlines()
    temp = [i.rstrip().split('\t') for i in temp[1:]]
    temp = [i for i in temp if len(i) == 3]
    temp_dict = {}
    for i in temp:
        for i1 in i[-1].split(';'):
            if i1 != '':
                if i1 in temp_dict:
                    temp_dict[i1] += 1
                else:
                    temp_dict[i1] = 1

                if i1 in results:
                    results[i1] += 1
                else:
                    results[i1] = 1
    print(i0, temp_dict)

filtered_results = {i:results[i] for i in results if results[i] > 150}
print(filtered_results)
print(len(results), len(filtered_results))

output = open('found_families.txt', 'w')
for i in filtered_results.keys():
    output.write(i + '\n')
