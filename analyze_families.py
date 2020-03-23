import os
from tqdm import tqdm
from urllib import request

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
    # print(i0, temp_dict)


def find_title_clan(family):
    family_word = ""
    clan_word = ""
    clan_id = ""
    url = f'http://pfam.xfam.org/family/{family}'
    site = request.urlopen(url).readlines()
    site = [i.decode('utf-8') for i in site]
    for i in range(len(site)):
        if "Family" in site[i]:
            family_word = site[i].split(' ')[1]
            break
    for i in range(len(site)):
        if "This family is a member of clan" in site[i]:
            clan_word = site[i + 1].split('>')[1].split('<')[0]
            clan_id = site[i + 2].split('>')[1].split('<')[0]
            break
    return family_word, clan_word, clan_id, url


filtered_results = {i:results[i] for i in results if results[i] > 150}
sorted_results = sorted(filtered_results, key=lambda i: filtered_results[i], reverse=True)
max_len = len(max(filtered_results, key=lambda i: filtered_results[i]))
summary = open('old_files/summary.txt', 'w')
summary_csv = open('old_files/summary.csv', 'w')
summary_csv.write(f'rodzina_id,rodzina_slownie,clan_id,clan_slownie,liczba_hitow,url\n')
for i in tqdm(sorted_results):
    family, clan_word, clan_id, url = find_title_clan(i)
    summary_csv.write(f'{i},{family},{clan_id},{clan_word},{filtered_results[i]},{url}\n')
    family += " " * (20 - len(family))
    clan_word += " " * (20 - len(clan_word))
    clan_id += " " * (6 - len(clan_id))
    hits = str(filtered_results[i]) + " " * (max_len - len(str(filtered_results[i])))
    summary.write(f'Family {i}, {family}, member of the clan {clan_id}, {clan_word}: {hits} hitów, link:{url}\n')




# print(filtered_results)
# print(len(results), len(filtered_results))



# output = open('found_families.txt', 'w')
# for i in filtered_results.keys():
#     output.write(i + '\n')
