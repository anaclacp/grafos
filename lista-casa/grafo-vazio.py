import networkx as nx
import matplotlib.pyplot as plt

# Criar um grafo vazio
grafo_vazio = nx.Graph()

# Verificar se o grafo está vazio
if grafo_vazio.number_of_nodes() == 0 and grafo_vazio.number_of_edges() == 0:
    print("O grafo está vazio!")
else:
    print("O grafo não está vazio.")

# Criar um grafo direcionado vazio
grafo_direcionado = nx.DiGraph()

grafo_direcionado.add_nodes_from([1, 2, 3, 4])
grafo_direcionado.add_edges_from([(1, 2),(2, 3),(1, 3),(4, 1),(4, 3)])

# Desenhar o grafo direcionado
plt.figure()
nx.draw(grafo_direcionado, with_labels=True, pos=nx.spring_layout(grafo_direcionado), 
        node_size=1200, node_color='pink', font_size=22, edge_color='purple')
plt.title('Grafo Direcionado')
plt.show()

if grafo_direcionado.number_of_nodes() == 0 and grafo_vazio.number_of_edges() == 0:
    print("O grafo está vazio!")
else:
    print("O grafo não está vazio.")

# Criar grafo não-direcionado
grafo_nao_direcionado = nx.Graph()

grafo_nao_direcionado.add_nodes_from([1, 2, 3, 4])
grafo_nao_direcionado.add_edges_from([(1, 2),(2, 4),(1, 3),(2, 1),(3, 4)])

plt.figure()
nx.draw(grafo_nao_direcionado, with_labels=True, pos=nx.spring_layout(grafo_nao_direcionado), 
        node_size=1200, node_color='lavender', font_size=22, edge_color='green')
plt.title('Grafo Não Direcionado')
plt.show()

if grafo_nao_direcionado.number_of_nodes() == 0 and grafo_vazio.number_of_edges() == 0:
    print("O grafo está vazio!")
else:
    print("O grafo não está vazio.")
