import numpy as np

Seq1 = str.upper(input("Enter 1st Seq: "))
Seq2 = str.upper(input("Enter 2nd Seq: "))

match = 1
misMatch = -1
gap = -2

# creat matrix
matrix_1 = np.zeros((len(Seq1) + 1, len(Seq2) + 1))
matrix_2 = np.zeros((len(Seq1), len(Seq2)))

# filing matrix2
for i in range(len(Seq1)):
    for j in range(len(Seq2)):
        if Seq1[i] == Seq2[j]:
            matrix_2[i][j] = match
        else:
            matrix_2[i][j] = misMatch


# filing matrix1
for i in range(len(Seq1) + 1):
    matrix_1[i][0] = i * gap

for j in range(len(Seq2) + 1):
    matrix_1[0][j] = j * gap






for i in range(1, len(Seq1) + 1):
    for j in range(1, len(Seq2) + 1):
        matrix_1[i][j] = max(matrix_1[i - 1][j - 1] + matrix_2[i - 1][j - 1],
                             matrix_1[i][j - 1] + gap, matrix_1[j, i - 1] + gap
                             )

m = len(Seq1)
n = len(Seq2)

Out1 = Out2 =Out3 = Out4= ""
maxScore = matrix_1[m][n]

while (m > 0 and n > 0):
    if (m > 0 and matrix_1[m][n] == matrix_1[m - 1][n] + gap):
        Out1 = Seq1[m - 1] + Out1
        Out2 = "-" + Out2

        m = m - 1
    elif (m > 0 and n > 0 and matrix_1[m][n] == matrix_1[m - 1][n - 1] + matrix_2[m - 1][n - 1]):
        Out1 = Seq1[m - 1] + Out1
        Out2 = Seq2[n - 1] + Out2
        m = m - 1
        n = n - 1
    else:
        Out1 = "-" + Out2
        Out2 = Seq2[n - 1] + Out2

        n = n - 1

if(Out1>Out2):
    Out4=Out1
elif(Out2>Out1):
    Out4=Out2
else:
    Out4=Out1

for i in range(0,len(Out4)):
    if(Out1[i] == Out2[i] == "G" or Out1[i] == Out2[i] == "A" or Out1[i] == Out2[i] == "T" or Out1[i] == Out2[i] == "C" ):
         Out3= Out3+"|"
    else:Out3 = Out3+" "




print(matrix_1)

print("\n\tMax Score: " + str(maxScore) + "\n")

print("\t\tSeq(1): " + Out1)
print("\t\t\t\t" + Out3)
print("\t\tSeq(2): " + Out2)