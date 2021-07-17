from matrixsd import *

while True:
    try:
        length_of_matrix = int(input('Enter the size of the matrix '))
    except:
        print('Pls enter number!')
    else:
        print(length_of_matrix)
        break

matrix_A = [[0 for x in range(0, length_of_matrix)] for x in range(0, length_of_matrix)]
matrix_B = [[0 for x in range(0, length_of_matrix)] for x in range(0, length_of_matrix)]

for i in range(0, length_of_matrix):
    matrix_A[i] = input('Enter matrix A: ').split(',')
    for j in range(0, length_of_matrix):
        matrix_A[i][j] = int(matrix_A[i][j])
for i in range(0, length_of_matrix):
    matrix_B[i] = input('Enter matrix B: ').split(',')
    for j in range(0, length_of_matrix):
        matrix_B[i][j] = int(matrix_B[i][j])


print(matrix_A)
print(matrix_B)
print(summ_of_matrix(matrix_A,matrix_B))
print(composition_of_matrix(matrix_A,matrix_B))
