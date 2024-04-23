import networkx as nx
import matplotlib.pyplot as plt

# Criar um grafo aleatório com 100 nós e probabilidade de aresta de 0.1
grafo_aleatorio = nx.gnp_random_graph(100, 0.1)

# Paleta de cores pastel
paleta_cores = [
    '#FF69B4', 
    '#FFF8DC', 
    '#87CEFA',
    '#9370DB'  
]

# Opções de layout para a visualização
layouts = [
    ("Spring Layout", nx.spring_layout),
    ("Circular Layout", nx.circular_layout),
    ("Random Layout", nx.random_layout),
    ("Shell Layout", nx.shell_layout),
    ("Spectral Layout", nx.spectral_layout),
    ("Kamada Kawai Layout", nx.kamada_kawai_layout)
]

# Plotar o grafo com as cores definidas
plt.figure(figsize=(15, 10))
for i, (layout_name, layout_function) in enumerate(layouts, 1):
    plt.subplot(2, 3, i)
    pos = layout_function(grafo_aleatorio)
    nx.draw(grafo_aleatorio, pos, with_labels=False, node_size=30, node_color=paleta_cores[i%len(paleta_cores)], edge_color='black')
    plt.title(layout_name)
plt.tight_layout()
plt.show()
