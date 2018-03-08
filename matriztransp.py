matriz = []
m = int(input("Digite o número de linhas da matriz: "))
n = int(input("Digite o número de colunas da matriz: "))

def constroimatriz(m, n, matriz):
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            x = int(input("Digite um número: "))
            linha.append(x)
        matriz.append(linha)
    return matriz

def transposta(m, n, matriz):
    for i in range(m):
        for j in range(n):
            matriz[i][j] = matriz[j][i]
    return matriz

print (transposta)
