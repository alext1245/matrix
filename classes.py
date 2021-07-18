class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def transpose(self):
        tpmatrix = [[0 for x in range(0, len(self.matrix[0]))] for x in range(len(self.matrix))]
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[0])):
                tpmatrix[i][j] = self.matrix[j][i]
        return tpmatrix

    def summ_of_matrix(self, A, B):
        self.A = A
        self.B = B
        summ = [[0 for x in range(0, len(self.A[0]))] for x in range(len(self.A))]
        for i in range(0, len(self.A)):
            for j in range(0, len(self.A[0])):
                summ[i][j] = self.A[i][j] + self.B[i][j]
        return summ

    def composition_of_matrix(self, A, B):
        self.A = A
        self.B = B
        comp = [[0 for x in range(0, len(self.A[0]))] for x in range(len(self.A))]
        for i in range(0, len(self.A)):
            for j in range(0, len(self.A[0])):
                for x in range(0, len(self.A)):
                    comp[i][j] += self.A[i][x] * self.B[x][j]
        return comp

    def subtraction_of_matrix(self,A, B):
        self.A = A
        self.B = B
        sub = [[0 for x in range(0, len(self.A[0]))] for x in range(len(self.A))]
        for i in range(0, len(self.A)):
            for j in range(0, len(self.A[0])):
                sub[i][j] = self.A[i][j] - self.B[i][j]
        return sub