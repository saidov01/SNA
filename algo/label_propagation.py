from cdlib import algorithms

from utils import draw


def run(G):
    result = algorithms.label_propagation(G)
    draw(G, result.communities)
