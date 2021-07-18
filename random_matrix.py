from random import randint
from classes import Matrix

size = int(input('Enter size of random matrix: '))
m1 = [[randint(0, 100) for i in range(0, size)] for i in range(0, size)]
m2 = [[randint(0, 100) for i in range(0, size)] for i in range(0, size)]
print(m1)
print(m2)
matrix = Matrix(m1)
print(matrix.transpose())
print(matrix.summ_of_matrix(m1,m2))
print(matrix.composition_of_matrix(m1,m2))
print(matrix.subtraction_of_matrix(m1,m2))