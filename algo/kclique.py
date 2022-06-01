from cdlib import algorithms
from networkx.algorithms.community import *

import networkx as nx
from matplotlib import pyplot as plt
from utils import draw


def run(G, k, small=False):
    result = algorithms.kclique(G, k)
    if small:
        communities = list(k_clique_communities(G, k))
        pos = nx.kamada_kawai_layout(G)

        plt.figure(figsize=(15, 15))
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        colors = ['blue', 'black', 'red', 'green', 'yellow', "orange", "purple", "olive"]
        nx.draw_networkx_nodes(G, pos, alpha=0.45, node_size=150)
        print (len(communities))
        for idx, cliq in enumerate(communities):
            nx.draw_networkx_nodes(list(cliq), pos, nodelist=list(cliq), node_color=colors[idx], node_size=300)

        plt.title('K-clique communities', size=15)
        plt.axis('off')
        plt.show()
    else:
        draw(G, result.communities)
