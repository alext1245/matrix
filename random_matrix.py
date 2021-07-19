from random import randint
from classes import Matrix

size = int(input('Enter size of random matrix: '))
m1 = [[randint(0, 100) for i in range(0, size)] for i in range(0, size)]
m2 = [[randint(0, 100) for i in range(0, size)] for i in range(0, size)]
print(m1)
print(m2)
m1 = Matrix(m1)
m2 = Matrix(m2)
print(m1.transpose())
print(m1 + m2)
print(m1 * m2)
print(m1 - m2)