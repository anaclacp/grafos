# 6- Remover nós e arestas: Escreva um código para demonstrar como remover um nó e uma aresta no grafo.

import networkx as nx 
import matplotlib.pyplot as plt

#Criação do grafo
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

print("Grafo antes da remoção:")
plt.figure("Grafo antes da remoção de Nó")  
nx.draw(G,  with_labels=True, pos=nx.spring_layout(G), 
        node_size=1200, node_color='pink', font_size=22, edge_color='purple',  arrows=False)
plt.show()

#Nó
no_removido = 3
G.remove_node(no_removido)

#Exibir grafo após remoção
print("\nGrafo após a remoção do nó", no_removido, ":")
plt.figure("Grafo Após Remoção de Nó")  
nx.draw(G, with_labels=True, pos=nx.spring_layout(G), 
        node_size=1200, node_color='lightgoldenrodyellow', font_size=22, edge_color='lightcoral',  arrows=False)
plt.show()

#Aresta
aresta_removida = (1, 2)
G.remove_edge(*aresta_removida)

#Exibir grafo após remoção 
print("\nGrafo após a remoção da aresta", aresta_removida, ":")
plt.figure("Grafo Após Remoção de Aresta")  
nx.draw(G, with_labels=True, pos=nx.spring_layout(G), 
        node_size=1200, node_color='lightblue', font_size=22, edge_color='lightseagreen',  arrows=False)
plt.show()