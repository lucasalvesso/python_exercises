def genMatriz(i, j):
    matriz = []
    for x in range(i):
        lin = []
        for y in range(j):
            lin.append(0)
        matriz.append(lin)
    return matriz

# sum matriz N x N
def sum(matrizA, matrizB):
    array3 = genMatriz(len(matrizA), len(matrizA))
    for i in range((len(matrizA))):
        for j in range((len(matrizB))):
            array3[i][j] = array1[i][j] + array2[i][j]
    return array3

# prod matriz N x N
def prod(matrizA, matrizB):
    array3 = genMatriz(len(matrizA), len(matrizA))
    for i in range((len(matrizA))):
        for j in range((len(matrizB))):
            array3[i][j] = 0
            for k in range(len(matrizA)):
                array3[i][j] = array3[i][j] + (array1[i][k] * array2[k][j])
    return array3

array1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(prod(array1, array2))