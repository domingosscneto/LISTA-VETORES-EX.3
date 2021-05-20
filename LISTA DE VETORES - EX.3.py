#Calcula a UNIÃO entre dois vetores
import random
vetorA = [0]*3
vetorB = [0]*3
n = len(vetorA)
m = len(vetorB)

def preencheVetor():
    for x in range(n):
        vetorA[x] = random.randint(0,10)
    print(vetorA)
    for x in range(m):
        vetorB[x] = random.randint(0,10)
    print(vetorB)

def uniãoVetor():
    lista = []
    for i in range(n):
        lista.append(vetorA[i])
    for i in range(n):
        if vetorB[i] not in vetorA:
            lista.append(vetorB[i])
    lista = list(dict.fromkeys(lista))
    print(f'Diferença entre os dois vetores: {lista}')


preencheVetor()
uniãoVetor()