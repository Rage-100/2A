import networkx as nx 
import matplotlib.pyplot as plt 
  
# Create directed graph with nodes and edges 
G = nx.DiGraph() 
G.add_edges_from([ 
    ("Dog", "Mammal", {"label": "is-a"}), 
    ("Cat", "Mammal", {"label": "is-a"}), 
    ("Mammal", "Animal", {"label": "is-a"}), 
    ("Dog", "Barks", {"label": "can"}), 
    ("Dog", "HasFur", {"label": "has"}), 
    ("Cat", "Meows", {"label": "can"}), 
    ("Cat", "HasFur", {"label": "has"}), 
    ("Animal", "CanFly", {"label": "cannot"}) 
]) 
  
# Check relationship 
print(f"Is a Dog an Animal? {nx.has_path(G, 'Dog', 'Animal')}") 
  
# Visualize 
pos = nx.spring_layout(G, seed=42) 
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, 
arrows=True) 
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 
'label'), font_color='red') 
plt.title("Simple Semantic Network") 
plt.axis('off') 
plt.show()
