#2- Adicionar nós e arestas: Escreva um código em Python que adicione três nós (1, 2, 3) e três arestas ((1, 2), (1, 3), (2, 3)) a um grafo. Apresente duas soluções: uma para grafo direcionado e outra para grafo não direcionado.

import networkx as nx
import matplotlib.pyplot as plt

# Grafo direcionado
grafo_direcionado = nx.DiGraph()
grafo_direcionado.add_nodes_from([1, 2, 3])
grafo_direcionado.add_edges_from([(1, 2), (1, 3), (2, 3)])

nx.draw(grafo_direcionado, with_labels=True, pos=nx.spring_layout(grafo_direcionado), 
        node_size=1200, node_color='lightblue', font_size=22, edge_color='black')

plt.rcParams['axes.facecolor'] = 'lightpink'
plt.gca().set_facecolor('lightpink')

plt.axis('off')
plt.show() 

# Grafo não direcionado
grafo_nao_direcionado = nx.Graph()
grafo_nao_direcionado.add_nodes_from([1, 2, 3])
grafo_nao_direcionado.add_edges_from([(1, 2), (1, 3), (2, 3)])

nx.draw(grafo_nao_direcionado, with_labels=True, pos=nx.spring_layout(grafo_nao_direcionado), 
        node_size=1200, node_color='lightgreen', font_size=22, edge_color='black')

plt.rcParams['axes.facecolor'] = 'lightyellow'
plt.gca().set_facecolor('lightyellow')

plt.axis('off')
plt.show()


def verificar_presenca_no_grafo(grafo, node):
    if node in grafo:
        print(f"O nó de número {node} está presente no grafo.")
    else:
        print(f"O nó de número {node} não está presente no grafo.")

grafo = nx.Graph()
grafo.add_nodes_from([1, 2, 3])
grafo.add_edges_from([(1, 2), (1, 3), (2, 3)])

verificar_presenca_no_grafo(grafo, 1)

grafo2 = nx.Graph()
grafo2.add_nodes_from([4, 2, 3])
grafo2.add_edges_from([(4, 2), (4, 3), (4, 3)])

verificar_presenca_no_grafo(grafo2, 1)


