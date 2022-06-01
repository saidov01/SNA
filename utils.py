import math

import networkx as nx
from matplotlib import pyplot as plt


def draw(G, communities):
    plt.figure(figsize=(15, 15))
    print("start_draw")
    G_v2 = nx.Graph()
    for i, community in enumerate(communities, start=1):
        if len(community) < len(list(G)) * 0.005:
            continue
        new_node = f"{i}: {len(community)}"
        G_v2.add_node(new_node, size=len(community) * 30)
        for k, other in enumerate(communities[i:], start=i + 1):
            if len(other) < len(list(G)) * 0.005:
                continue
            other_node = f"{k}: {len(other)}"
            if community != other:
                other = set(other)
                size = 0
                for node in community:
                    size += len(set(G.neighbors(node)).intersection(other))
                if size:
                    G_v2.add_edge(new_node, other_node, width=math.log10(size))

    print("start_draw")
    colors = ["r", "g", "b", "#000000", "#CCCC00", "#0099CC"]
    for i in range(6, len(G_v2.nodes())):
        colors.append(colors[i % 5])

    pos = nx.kamada_kawai_layout(G_v2)
    nx.draw_networkx_nodes(
        G_v2,
        pos,
        nodelist=G_v2.nodes(),
        node_color=colors[: len(G_v2.nodes(data=True))],
        node_size=[data["size"] for _, data in G_v2.nodes(data=True)],
    )
    nx.draw_networkx_edges(
        G_v2, pos, edgelist=G_v2.edges(), width=[data["width"] for _, _, data in G_v2.edges(data=True)]
    )
    plt.show()
