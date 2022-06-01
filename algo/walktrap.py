from cdlib import algorithms

from utils import draw


def run(G):
    result = algorithms.walktrap(G)
    draw(G, result.communities)
