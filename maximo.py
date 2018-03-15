m = int(input("Digite o número de elementos que deseja em sua lista: "))
lista = []

def constroilista(m, lista):
        for i in range(m):
            x = int(input("Digite um elemento da lista: "))
            lista.append(x)
        return lista

print(constroilista(m, lista))

def maximo(lista):
    for i in range(len(lista)):
        if lista[i]>lista[i-1]:
            maior = lista[i]
    return maior

print("O maior número de sua lista é:", maximo(lista))
