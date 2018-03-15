# Recebimento de vetores

# COMO PERMITIR QUE O USUÁRIO CRIE VETORES? A FORMA QUE CONHEÇO EXIGE SOMA :/

# Usando exemplo pra poder montar a função pedida.
vetor1 = (5,7)
vetor2 = (6,2)

def somarvetores (vetor1, vetor2):

    if len(vetor1)==len(vetor2):
        vetorsoma = []
        for i in range(len(vetor1)):
            soma = vetor1[i]+vetor2[i]
            vetorsoma.append(soma)
    return vetorsoma

print(somarvetores(vetor1,vetor2))

# Recebimento de matrizes

def somarmatrizes (matriz1, matriz2):

# Condição 1 para soma de matriz: mesmo número de linhas
if len(matriz1)==len(matriz2):

# Condição 2 para soma de matriz: mesmo número de colunas:

# COMO VERIFICAR SE AS MATRIZES TÊM O MESMO NÚMEROD E COLUNAS?
