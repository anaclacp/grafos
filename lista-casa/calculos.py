# 7- Calcular o número de nós e arestas: Escreva um código que calcule e imprima o número de nós e o número de arestas de um grafo.

# 8- Calcular o grau de um nó: Escreva um código em Python que calcule e imprima o grau de um nó do grafo.

# 9- Encontrar todos os vizinhos de um nó: Escreva um código que encontre e imprima todos os vizinhos de um determinado nó do grafo.

# 10- Calcular o caminho mais curto entre dois nós: Escreva um código que calcule e imprima o caminho mais curto entre dois nós de um grafo.

import networkx as nx
import matplotlib.pyplot as plt #visualizar o grafo

def calcular(grafo):
    num_nos = grafo.number_of_nodes()
    num_arestas = grafo.number_of_edges()
    return num_nos, num_arestas

def calcular_grau(grafo, no):
    grau = grafo.degree[no]
    print(f"O grau do nó {no} é {grau}.")

def encontrar_vizinhos(grafo,no):
    vizinhos = list(grafo.neighbors(no))
    print(f"Os vizinhos do nó {no} são: ", vizinhos)

def caminho_mais_curto(grafo, no_origem, no_destino):
    try:
        caminho = nx.shortest_path(grafo, source=no_origem, target=no_destino)
        print(f"O caminho mais curto entre os nós {no_origem} e {no_destino} é:", caminho)
    except nx.NetworkXNoPath:
        print(f"Não há caminho entre os nós {no_origem} e {no_destino}.")

def verificar_ciclos(grafo):
    ciclos = nx.cycle_basis(grafo)
    if ciclos:
        print("O grafo possui os seguintes ciclos:")
        for ciclo in ciclos:
            print(ciclo)
    else:
        print("O grafo não possui ciclos.")

def plotar_grafo(grafo):
    pos = nx.spring_layout(grafo) # Posicionamento dos nós
    nx.draw(grafo, pos, with_labels=True, node_size=1200, node_color='skyblue', font_size=22, edge_color='pink',  arrows=False)
    plt.show()

grafo = nx.Graph()

#Entrada de dados
num_nos = int(input("Digite o número de nós do grafo: "))
num_arestas = int(input("Digite o número de arestas do grafo: "))

for i in range(1, num_nos + 1):
    grafo.add_node(i)

#Entrada de dados2
print("Insira as arestas no formato 'nó1 nó2':")
for i in range(num_arestas):
    aresta = input(f"Aresta {i+1}: ").split()
    grafo.add_edge(int(aresta[0]), int(aresta[1]))

# Calcular
num_nos_calculado, num_arestas_calculado = calcular(grafo)

no_desejado = int(input("Digite o número do nó para calcular o grau: "))

no_origem = int(input("\nDigite o número do nó de origem: "))
no_destino = int(input("Digite o número do nó de destino: "))

print("\nNúmero de nós:", num_nos_calculado)
print("Número de arestas:", num_arestas_calculado)

#Calcular o grau do nó
calcular_grau(grafo, no_desejado)

#Vizinhos
encontrar_vizinhos(grafo, no_desejado)

# Caminho mais curto
caminho_mais_curto(grafo, no_origem, no_destino)

# Verificar ciclos
verificar_ciclos(grafo)

#Plotar grafo 
plotar_grafo(grafo)
