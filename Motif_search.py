list_of_motifs = ["NPXXY", "E/DRY", "CWXP", "IPF"]



true_motif = []
skip = False
for i in range(len(list_of_motifs)):
    rule_set = []
    for i1 in range(len(list_of_motifs[i])):
        if skip:
            skip = False
        else:
            if list_of_motifs[i][i1] == '/':
                rule_set.append([rule_set.pop(), list_of_motifs[i][i1 + 1]])
                skip = True
            else:
                rule_set.append(list_of_motifs[i][i1])
    true_motif.append(rule_set)

print(true_motif)





