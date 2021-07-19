class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def rows_count(self):
        return len(self.matrix)

    def columns_count(self):
        return len(self.matrix[0])

    def transpose(self):
        tpmatrix = [[0 for x in range(0, len(self.matrix[0]))] for x in range(len(self.matrix))]
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[0])):
                tpmatrix[i][j] = self.matrix[j][i]
        return tpmatrix


    def __add__(self, other):
        summ = [[0 for x in range(0, len(self.matrix[0]))] for x in range(len(self.matrix))]
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[0])):
                summ[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return summ

    def __mul__(self, other):
        comp = [[0 for x in range(0, len(self.matrix[0]))] for x in range(len(self.matrix))]
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[0])):
                for x in range(0, len(self.matrix[0])):
                    comp[i][j] += self.matrix[i][x] * other.matrix[x][j]
        return comp

    def __sub__(self, other):
        sub = [[0 for x in range(0, len(self.matrix[0]))] for x in range(len(self.matrix))]
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[0])):
                sub[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return sub