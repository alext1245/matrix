class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def rows_count(self):
        return len(self.matrix)

    def columns_count(self):
        return len(self.matrix[0])

    def transpose(self):
        tpmatrix = [[0 for x in range(0, self.columns_count())] for x in range(self.rows_count())]
        for i in range(0, self.rows_count()):
            for j in range(0, self.columns_count()):
                tpmatrix[i][j] = self.matrix[j][i]
        return tpmatrix


    def __add__(self, other):
        summ = [[0 for x in range(0, self.columns_count())] for x in range(self.rows_count())]
        for i in range(0, self.rows_count()):
            for j in range(0, self.columns_count()):
                summ[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return summ

    def __mul__(self, other):
        comp = [[0 for x in range(0, self.columns_count())] for x in range(self.rows_count())]
        for i in range(0, self.rows_count()):
            for j in range(0, self.columns_count()):
                for x in range(0, self.columns_count()):
                    comp[i][j] += self.matrix[i][x] * other.matrix[x][j]
        return comp

    def __sub__(self, other):
        sub = [[0 for x in range(0, self.columns_count())] for x in range(self.rows_count())]
        for i in range(0, self.rows_count()):
            for j in range(0, self.columns_count()):
                sub[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return sub