import random

import networkx as nx

G = nx.Graph()
with open('.data/facebook.csv') as f, open('.data/twitter.csv', 'w+') as w:
    w.write(f.readline())
    for r in f:
        G.add_edge(*r.strip().split(","))

    for node in list(G):
        if len(list(G.neighbors(node))) < 10:
            G.remove_node(node)

    for edge in G.edges():
        w.write(edge[0] + "," + edge[1] + "\n")
