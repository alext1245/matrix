from matrixsd import *
from random import randint

size = int(input('Enter size of random matrix: '))
m1 = [[randint(0, 100) for i in range(0, size)] for i in range(0, size)]
m2 = [[randint(0, 100) for i in range(0, size)] for i in range(0, size)]
print(m1)
print(m2)
print(summ_of_matrix(m1, m2))
print(composition_of_matrix(m1, m2))