from matrixsd import *
from random import randint
from classes import Matrix, Operation_with_matrix

size = int(input('Enter size of random matrix: '))
m1 = [[randint(0, 100) for i in range(0, size)] for i in range(0, size)]
m2 = [[randint(0, 100) for i in range(0, size)] for i in range(0, size)]
print(m1)
print(m2)
tp = Matrix(m1)
operation = Operation_with_matrix(m1,m2)
print(operation.summ_of_matrix())
print(operation.composition_of_matrix())
print(operation.subtraction_of_matrix())
print(tp.transpose())