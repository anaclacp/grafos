import networkx as nx

# Criando um grafo vazio
grafo = nx.Graph()

num_nos = int(input("Digite o número de nós do grafo: "))
num_arestas = int(input("Digite o número de arestas do grafo: "))

#Nós
for i in range(num_nos):
    grafo.add_node(i+1)
#Arestas
    
for i in range(num_arestas):
    no1 = int(input(f"Digite o nó de origem da aresta {i+1}: "))
    no2 = int(input(f"Digite o nó de destino da aresta {i+1}: "))
    grafo.add_edge(no1, no2)

#Exercício 4: Verificar a presença de um nó
node = int(input("Digite o número do nó que deseja verificar: "))
if grafo.has_node(node):
    print(f"O nó de número {node} está presente no grafo.")
else:
    print(f"O nó de número {node} não está presente no grafo.")

#Exercício 5: Verificar a presença de uma aresta
no1 = int(input("Digite o número do primeiro nó: "))
no2 = int(input("Digite o número do segundo nó: "))
if grafo.has_edge(no1, no2):
    print(f"A aresta entre os nós {no1} e {no2} está presente no grafo.")
else:
    print(f"A aresta entre os nós {no1} e {no2} não está presente no grafo.")
