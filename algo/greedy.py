from cdlib import algorithms

from utils import draw


def run(G):
    result = algorithms.greedy_modularity(G)
    draw(G, result.communities)
