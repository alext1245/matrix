def summ_of_matrix(A, B):
    summ = [[0 for x in range(0, len(A[0]))] for x in range(len(A))]
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            summ[i][j] = A[i][j] + B[i][j]
    return summ


def composition_of_matrix(A,B):
    comp = [[0 for x in range(0, len(A[0]))] for x in range(len(A))]
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            for x in range(0,len(A)):
                comp[i][j] += A[i][x]*B[x][j]
    return comp




