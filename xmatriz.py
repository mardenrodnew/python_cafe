
matrizA = []
matrizB = []

# Meu programa tem as seguintes tarefas, em sequencia:

# 1. Receber ou construir uma matriz A

constroimatriz (m, n, matrizA)
print(constroimatriz(m, n, matrizA))

# 2. Receber ou construir uma matriz B

constroimatriz (m, n, matrizB)
print(constroimatriz(x, y, matrizB))

def multiplicajesus (m, n, x, y, matrizA, matrizB):

# 3. Verificar se o número de colunas de A equivale ao número de linhas de B

    if n==x:
# 4. Caso An = Bm, então o programa deve efetuar a multiplicação das matrizes

            # UTILIZANDO UMA MATRIZ A 2x3 E UMA MATRIZ B 3X2 COMO EXEMPLO

        # I. Multiplicar a linha1 de A pela coluna 1 de B
            # a11*b11 + a12*b21 + a13*b31
        matrizA[0][0]*matrizB[0][0] +  matrizA[0][1]*matrizB[1][0] + matrizA[0][2]*matrizB[2][0]

        # II.Multiplicar a linha1 de A pela coluna2 de B
            # a11*b12 + a12*b22 + a13*b32
        matrizA[0][0]*matrizB[0][1] + matrizA[0][1]*matrizB[1][1] + matrizA[0][2]*matrizB[2][1]

        # III. Multiplicar a linha2 de A pela coluna1 de B
            # a21*b11 + a22*b21 + a23*b31
        matrizA[1][0]*matrizB[0][0] + matrizA[1][1]*matrizB[1][0] + matrizA[1][2]*matrizB[2][0]

        # IV. Multiplicar a linha2 de A pela coluna2 de B
            # a21*b12 + a22*b22 + a23*b32
        matrizA[1][0]*matrizB[0][1] + matrizA[1][1]*matrizB[1][1] + matrizA[1][2]*matrizB[2][1]

        # V. E assim sucessivamente, conforme os indices correspondentes ao número de linhas de A e colunas de B variarem

        # TENTATIVA DE GENERALIZAÇÃO

        matrizC = []
        #Sendo i um indice que varia num range(m), onde m é o número de linhas de matrizA
        for i in range(m):
            #Sendo j um indice que varia num range(y), onde y é o número de colunas de matrizB
            for j in range(y):
                linhac2 = []
                #Sendo k um indice que varia num range(n), onde n é o número de colunas de matrizA, este é o índice que seleciona o elemento da linha a ser multiplicado
                for k in range(n):
                    #O elemento1 será o elemento c11 da Matriz C
                    linhac1 = []
                    #Sendo l um indice que varia num range(x), onde l é o número de linhas de matrizB, este é o índice que seleciona o elemento da coluna a ser multiplicado
                    for l in range(x):
                        c = matrizA[i][k]*matrizB[l][j] + matrizA[i][k]*matrizB[l][j] + matrizA[i][k]*matrizB[l][j]
                        linhac1.append(c)
                linhac1.append(c)
            linhac2.append(c)
        linhac2.append(c)
        matrizC.append(linhac1)
        matrizC.append(linhac2)

# 5. Exibir a matriz C, resultante da multiplicação entre A e B
        return matrizC

    else:
# 6. Se An é diferente de Bm, então meu programa deve imprimir que não há como efetuar a operação
        return False


print (multiplicajesus(m, n, x, y, matrizA, matrizB))
