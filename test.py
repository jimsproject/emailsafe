import matplotlib.pyplot as plt
import networkx as nx

# Membuat graf
G = nx.DiGraph()

# Menambahkan edge
G.add_edge('entrance', 'A', weight=1.0)
G.add_edge('A', 'B', weight=1.0)
G.add_edge('B', 'C', weight=1.0)
G.add_edge('C', 'D', weight=1.0)
G.add_edge('D', 'exit', weight=1.0)

# Menambahkan posisi untuk setiap node
pos = {
    'entrance': (0, 0),
    'A': (1, 0),
    'B': (2, 0),
    'C': (3, 0),
    'D': (4, 0),
    'exit': (5, 0)
}

# Menambahkan berat untuk setiap edge
labels = nx.get_edge_attributes(G, 'weight')

# Menggambar graf
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Menampilkan graf
plt.show()
