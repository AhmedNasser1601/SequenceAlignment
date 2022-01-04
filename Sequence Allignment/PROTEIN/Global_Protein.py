import numpy as np
import pandas as pd

protiens = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G',
            'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S',
            'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '*']

blosum62 = pd.read_csv("BLOSUM62.csv")
blosum62 = blosum62.rename(index=lambda s: protiens[int(s)])
blosum62_map = {}

for i in protiens:
    for j in protiens:
        blosum62_map[(i, j)] = blosum62.at[i, j]

def global_align(x, y, gap = -1):
    len_y = len(y) + 1
    len_x = len(x) + 1

    NW = np.zeros((len_y, len_x))

    for i in range(len_y):
        NW[i][0] = gap * i
    for i in range(len_x):
        NW[0][i] = gap * i

    for i in range(1, len_y):
        for j in range(1, len_x):
            NW[i][j] = max(NW[i][j - 1] + gap,
                           NW[i - 1][j] + gap,
                           NW[i - 1][j - 1] + blosum62_map[(y[i - 1], x[j - 1])])

    new_x = ""
    new_y = ""
    i = len(y)
    j = len(x)
    print("\n\tMax Score: " + str(NW[len(y)][len(x)]) + "\n")

    while i > 0 or j > 0:
        score = NW[i][j]

        if i > 0 and j > 0 and score == NW[i - 1][j - 1] + blosum62_map[(y[i - 1], x[j - 1])]:
            new_x = x[j - 1] + new_x
            new_y = y[i - 1] + new_y
            i -= 1
            j -= 1
        elif j > 0 and score == NW[i][j - 1] + gap:
            new_x = x[j - 1] + new_x
            new_y = '_' + new_y
            j -= 1
        else:
            new_x = '_' + new_x
            new_y = y[i - 1] + new_y
            i -= 1

    return (new_x, new_y)




X = 'MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFK'
Y = 'MVLSAADKNNVKGIFTKIAGHAEEYGAETLERMFTTYPPTKTYFPHFDLSHGSAQIKGHGKKVVAALIEAANHIDDIAGTLSKLSDLHAHKLRVDPVNFK'

X, Y = global_align(X, Y)
print(X + "\n" + Y)