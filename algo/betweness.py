import random

import networkx as nx
import matplotlib.pyplot as plt
from itertools import count


def run(G, truncate=True):
    if truncate:
        plt.figure(figsize=(15,15))
        result = nx.betweenness_centrality(G, 100)
        max_ = max(result.values())
        for k, v in result.items():
            result[k] = v / max_
        print("start_draw")
        nodes = [k for k, v in sorted(result.items(), key=lambda x: x[1])[-4:]]
        new_graph = nx.Graph()
        for n in nodes:
            new_graph.add_node(n, color="#ff0000", size=900)
        for n in nodes:
            for k in G.neighbors(n):
                new_graph.add_edge(n, k)

        for n in list(new_graph.nodes()):
            if n not in nodes and len(list(new_graph.neighbors(n))) < 2:
                if random.random() > 0.1:
                    new_graph.remove_node(n)

        nx.draw(new_graph)
        plt.show()
    else:
        plt.figure(figsize=(15,15))
        betweenness_centrality = nx.betweenness_centrality(G)

        nx.set_node_attributes(G, betweenness_centrality, "betweenness_centrality")

        groups = set(nx.get_node_attributes(G, "betweenness_centrality").values())
        mapping = dict(zip(sorted(groups), count()))
        nodes = G.nodes()
        colors = [mapping[G.nodes[n]["betweenness_centrality"]] / 60 for n in nodes]
        node_sizes = [(i * 400) + 100 for i in colors]

        pos = nx.kamada_kawai_layout(G)
        ec = nx.draw_networkx_edges(G, pos, alpha=0.2)
        nc = nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color=colors, node_size=node_sizes, cmap=plt.cm.jet)

        plt.title('Betweenness centrality', size=15)
        plt.colorbar(nc)
        plt.axis('off')
        plt.show()
