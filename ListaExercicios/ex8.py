matrix1 = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
matrix2 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]


def somaMatriz(m1, m2):
    newMatrix = []

    nLinhasM1 = len(m1)
    nColunasM1 = len(m1[0])

    nLinhasM2 = len(m2)
    nColunasM2 = len(m2[0])

    if not(nLinhasM1 == nLinhasM2):
        print("número de linhas diferentes")
        return
    elif not(nColunasM1 == nColunasM2):
        print("problema no número de colunas")
        return

    for l in matrix1:
        if len(l) == nColunasM1:
            print("problema no número de colunas")
            return
    
    for l in matrix2:
        if len(l) == nColunasM2:
            print("problema no número de colunas")
            return

    for l in range(0, nLinhasM1):
        auxMatrix = []
        for c in range(0, nColunasM1):
            auxMatrix.append(m1[l][c] + m2[l][c])
        newMatrix.append(auxMatrix)
    
    return newMatrix

print(somaMatriz(matrix1, matrix2))
