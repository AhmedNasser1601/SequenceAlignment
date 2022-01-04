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


Seq1 = str.upper(input("Enter 1st Protein: "))
Seq2 = str.upper(input("Enter 2nd Protein: "))

gap = -1

matrix_1 = np.zeros((len(Seq1) + 1, len(Seq2) + 1))

for i in range(len(Seq1) + 1):
    matrix_1[i][0] = i * 0

for j in range(len(Seq2) + 1):
    matrix_1[0][j] = j * 0

for j in range(1, len(Seq1) + 1):
    for i in range(1, len(Seq2) + 1):
        matrix_1[i][j] = max(matrix_1[i - 1][j - 1] + blosum62_map[(Seq1[i - 1], Seq2[j - 1])],
                             matrix_1[i][j - 1] + gap,
                             matrix_1[j][i - 1] + gap)
        if(matrix_1[i][j]<0):
            matrix_1[i][j]=0

maxScore = 0

for j in range(1, len(Seq1) + 1):
    for i in range(1, len(Seq2) + 1):
       if(maxScore<matrix_1[i][j]):
           maxScore=matrix_1[i][j]

n = m = 0

for j in range(1, len(Seq1) + 1):
    for i in range(1, len(Seq2) + 1):
      if(matrix_1[i][j] == maxScore):
           m = i
           n = j

Out1 = Out2 = Out3 = Out4 = ""

while (True):
    if (m > 0 and matrix_1[m][n] == matrix_1[m - 1][n] ):
        Out1 = Seq1[m - 1] + Out1
        Out2 = "-" + Out2
        m = m - 1
    elif (m > 0 and n > 0 and matrix_1[m][n] == matrix_1[m - 1][n - 1] + blosum62_map[(Seq1[m - 1], Seq2[n - 1])]):
        Out1 = Seq1[m - 1] + Out1
        Out2 = Seq2[n - 1] + Out2
        m -= 1
        n -= 1
    else:
        Out1 = "-" + Out2
        Out2 = Seq2[n - 1] + Out2
        n -= 1

    if (m <= 0):
        break
    if (n <= 0):
        break
    if (matrix_1[m][n] <= 0):
        break

if (Out1 > Out2):
    Out4 = Out1
elif (Out2 > Out1):
    Out4 = Out2
else:
    Out4 = Out1

for i in range(0, len(Out4)):
    if (Out1[i] == Out2[i] != "-" ):
        Out3 = Out3 + "|"
    else:
        Out3 = Out3 + " "


print(matrix_1)

print("\n\tMax Score: " + str(maxScore) + "\n")

print("\t\tSeq(1): " + Out1)
print("\t\t\t\t" + Out3)
print("\t\tSeq(2): " + Out2)



'''
            acdef ghikl ---
                  ||-||
            mn--- ghqkl rrs
'''